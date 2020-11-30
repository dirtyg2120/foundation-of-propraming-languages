""" class Program: #decl:List[Decl],stmts:List[Stmt]

class Decl(ABC): #abstract class

class VarDecl(Decl): #name:str

class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]

class Stmt(ABC): #abstract class

class Assign(Stmt): #lhs:Id,rhs:Exp

class CallStmt(Stmt): #name:str,args:List[Exp]

class Exp(ABC): #abstract class

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str

In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign

The type of an Id is inferred from the above constraints in the
first usage, 
    If the Id is not in the declarations, exception UndeclaredIdentifier
    should be raised together with the name of the Id, or

    If the Id cannot be inferred in the first usage, exception
    TypeCannotBeInferred should be raised together with the statement

For static referencing environment, this language applies 
he scope rules of block-structured programming language where
a function is a block. When there is a declaration duplication of
a name in a scope, exception Redeclared should be raised together
with the second declaration.

In a call statement, the argument type must be the same as
the parameter type. If there is no function declaration in
the static referencing environment, exception UndeclaredIdentifier
should be raised together with the function call name. If the numbers
of parameters and arguments are not the same or at least one argument
type is not the same as the type of the corresponding parameter,
exception TypeMismatchInStatement should be raise with the call
statement. If there is at least one parameter type cannot be resolved,
exception TypeCannotBeInferred should be raised together with
the call statement.

 """


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        o = {}
        for decl in ctx.decl:
            self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        o[ctx.name] = ''

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
        if ctx.name in o:
            raise Redeclared(ctx)

        param_list = {}
        for param in ctx.param:
            self.visit(param, param_list)

        local_list = param_list.copy()
        local_list[ctx.name] = param_list.copy()
        for local in ctx.local:
            self.visit(local, local_list)

        total_envir = o.copy()
        for name in local_list:
            total_envir[name] = local_list[name]
        for stmt in ctx.stmts:
            self.visit(stmt, total_envir)

        for name in o:
            if name not in local_list:
                o[name] = total_envir[name]
        o[ctx.name] = total_envir[ctx.name]    

    def visitCallStmt(self, ctx: CallStmt, o):
        # name:str,args:List[Exp]
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        
        if type(o[ctx.name]) is not dict:
            raise UndeclaredIdentifier(ctx.name)

        if len(o[ctx.name]) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)

    def visitAssign(self, ctx: Assign, o):
        exp_type = self.visit(ctx.rhs, o)
        id_type = self.visit(ctx.lhs, o)
        if exp_type == '' and id_type == '':
            raise TypeCannotBeInferred(ctx)
        elif exp_type == '' and id_type != '':
            exp_type = id_type
            o[ctx.rhs.name] = exp_type
        elif exp_type != '' and id_type == '':
            id_type = exp_type
            o[ctx.lhs.name] = id_type
        elif id_type != exp_type:
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return 'int'

    def visitFloatLit(self, ctx, o):
        return 'float'

    def visitBoolLit(self, ctx, o):
        return 'bool'

    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]
