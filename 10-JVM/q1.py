""" 
class Program:  # decl:List[VarDecl],stmts:List[Assign]

class VarDecl:  # name:str

class Assign: #lhs:Id,rhs:Exp

class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str

and the Visitor class is declared as follows:
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

    def visitBinOp(self, ctx: BinOp, o):
        e1_type = self.visit(ctx.e1, o)
        e2_type = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/']:
            # type inference
            if e1_type == '':
                e1_type = 'int'
                o[ctx.e1.name] = e1_type
            if e2_type == '':
                e2_type = 'int'
                o[ctx.e2.name] = e2_type
            # type checking
            if e1_type != 'int' or e2_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op in ['+.', '-.', '*.', '/.']:
            # type inference
            if e1_type == '':
                e1_type = 'float'
                o[ctx.e1.name] = e1_type
            if e2_type == '':
                e2_type = 'float'
                o[ctx.e2.name] = e2_type
            # type checking
            if e1_type != 'float' or e2_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op in ['>', '=']:
            # type inference
            if e1_type == '':
                e1_type = 'int'
                o[ctx.e1.name] = e1_type
            if e2_type == '':
                e2_type = 'int'
                o[ctx.e2.name] = e2_type
            # type checking
            if e1_type != 'int' or e2_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif ctx.op in ['>.', '=.']:
            # type inference
            if e1_type == '':
                e1_type = 'float'
                o[ctx.e1.name] = e1_type
            if e2_type == '':
                e2_type = 'float'
                o[ctx.e2.name] = e2_type
            # type checking
            if e1_type != 'float' or e2_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif ctx.op in ['&&', '||', '>b', '=b']:
            # type inference
            if e1_type == '':
                e1_type = 'bool'
                o[ctx.e1.name] = e1_type
            if e2_type == '':
                e2_type = 'bool'
                o[ctx.e2.name] = e2_type
            # type checking
            if e1_type != 'bool' or e2_type != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self, ctx: UnOp, o):
        e_type = self.visit(ctx.e, o)
        if ctx.op == '-':
            # type inference
            if e_type == '':
                e_type = 'int'
                o[ctx.e.name] = e_type
            # type checking
            if e_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op == '-.':
            # type inference
            if e_type == '':
                e_type = 'float'
                o[ctx.e.name] = e_type
            # type checking
            if e_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op == 'i2f':
            # type inference
            if e_type == '':
                e_type = 'int'
                o[ctx.e.name] = e_type
            # type checking
            if e_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op == 'floor':
            # type inference
            if e_type == '':
                e_type = 'float'
                o[ctx.e.name] = e_type
            # type checking
            if e_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op == '!':
            # type inference
            if e_type == '':
                e_type = 'bool'
                o[ctx.e.name] = e_type
            # type checking
            if e_type != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'

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
