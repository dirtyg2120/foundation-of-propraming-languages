""" class Program: #decl:List[VarDecl],stmts:List[Assign]

class VarDecl: #name:str

class Assign: #lhs:Id,rhs:Exp

class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str


Type Mismatch In Expression: BinOp("-",Id("x"),FloatLit(2.1))
Type Mismatch In Statement: Assign(Id("z"),Id("x")) -> 2 ben khong cung kieu
Type Cannot Be Inferred: Assign(Id("x"),Id("y"))

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
        type2 = self.visit(ctx.rhs, o)
        type1 = self.visit(ctx.lhs, o)
        if type2 == '':
            raise TypeCannotBeInferred(ctx)
        if type1 == '':
            type1 = type2
            o[ctx.lhs.name] = type1
        else:
            if type1 != type2:
                raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        type1 = self.visit(ctx.e1, o)
        type2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/']:
            # type inference
            if type1 == '':
                type1 = 'int'
                o[ctx.e1.name] = type1
            if type2 == '':
                type2 = 'int'
                o[ctx.e2.name] = type2
            # type checking
            if type1 != 'int' or type2 != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op in ['+.', '-.', '*.', '/.']:
            # type inference
            if type1 == '':
                type1 = 'float'
                o[ctx.e1.name] = type1
            if type2 == '':
                type2 = 'float'
                o[ctx.e2.name] = type2
            # type checking
            if type1 != 'float' or type2 != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op in ['>', '=']:
            # type inference
            if type1 == '':
                type1 = 'int'
                o[ctx.e1.name] = type1
            if type2 == '':
                type2 = 'int'
                o[ctx.e2.name] = type2
            # type checking
            if type1 != 'int' or type2 != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif ctx.op in ['>.', '=.']:
            # type inference
            if type1 == '':
                type1 = 'float'
                o[ctx.e1.name] = type1
            if type2 == '':
                type2 = 'float'
                o[ctx.e2.name] = type2
            # type checking
            if type1 != 'float' or type2 != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif ctx.op in ['&&', '||', '>b', '=b']:
            # type inference
            if type1 == '':
                type1 = 'bool'
                o[ctx.e1.name] = type1
            if type2 == '':
                type2 = 'bool'
                o[ctx.e2.name] = type2
            # type checking
            if type1 != 'bool' or type2 != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self, ctx: UnOp, o):
        operand_type = self.visit(ctx.e, o)
        if ctx.op == '-':
            # type inference
            if operand_type == '':
                operand_type = 'int'
                o[ctx.e.name] = operand_type
            # type checking
            if operand_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op == '-.':
            # type inference
            if operand_type == '':
                operand_type = 'float'
                o[ctx.e.name] = operand_type
            # type checking
            if operand_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op == 'i2f':
            # type inference
            if operand_type == '':
                operand_type = 'int'
                o[ctx.e.name] = operand_type
            # type checking
            if operand_type != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        elif ctx.op == 'floor':
            # type inference
            if operand_type == '':
                operand_type = 'float'
                o[ctx.e.name] = operand_type
            # type checking
            if operand_type != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        elif ctx.op == '!':
            # type inference
            if operand_type == '':
                operand_type = 'bool'
                o[ctx.e.name] = operand_type
            # type checking
            if operand_type != 'bool':
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


""" from functools import reduce


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        o = {}
        env = reduce(lambda x, y: dict(
            y.accept(self, x).items() | x.items()), ctx.decl, o)
        stmts = reduce(lambda x, y: y.accept(self, x), ctx.stmts, env)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        return {ctx.name: None}

    def visitAssign(self, ctx: Assign, o):
        rhs_type = ctx.rhs.accept(self, o)
        lhs_type = ctx.lhs.accept(self, o)

        if None == rhs_type:
            raise TypeCannotBeInferred(ctx)

        if None != rhs_type and None == lhs_type:
            o[ctx.lhs.name] = rhs_type
            lhs_type = rhs_type

        if rhs_type != lhs_type:
            raise TypeMismatchInStatement(ctx)

        return o

    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]

    def visitBinOp(self, ctx: BinOp, o):
        type1 = ctx.e1.accept(self, o)
        type2 = ctx.e2.accept(self, o)
        join_type = set([type1, type2])

        if (ctx.op == '+' or ctx.op == '-' or ctx.op == '*' or ctx.op == '/'):
            if 'float' in join_type or 'bool' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'int'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'int'})
                return ctx.accept(self, o)
            return 'int'

        elif (ctx.op == '>' or ctx.op == '='):
            if 'float' in join_type or 'bool' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'int'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'int'})
                return ctx.accept(self, o)
            return 'bool'

        elif (ctx.op == '>.' or ctx.op == '=.'):
            if 'bool' in join_type or 'int' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'float'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'float'})
                return ctx.accept(self, o)
            return 'bool'

        elif (ctx.op == '&&' or ctx.op == '||' or ctx.op == '>b' or ctx.op == '=b'):
            if 'float' in join_type or 'int' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'bool'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'bool'})
                return ctx.accept(self, o)
            return 'bool'

    def visitUnOp(self, ctx: UnOp, o):
        join_type = ctx.e.accept(self, o)

        if (ctx.op == '!'):
            if 'float' == join_type or 'int' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'bool'})
                return ctx.accept(self, o)
            return 'bool'

        elif (ctx.op == '-'):
            if 'float' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'int'})
                return ctx.accept(self, o)
            return 'int'

        elif (ctx.op == '-.'):
            if 'int' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'float'})
                return ctx.accept(self, o)
            return 'float'

        elif (ctx.op == 'i2f'):
            if 'float' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'int'})
                return ctx.accept(self, o)
            return 'float'

        elif (ctx.op == 'floor'):
            if 'int' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'float'})
                return ctx.accept(self, o)
            return 'int'

    def visitIntLit(self, ctx: IntLit, o):
        return 'int'

    def visitFloatLit(self, ctx, o):
        return 'float'

    def visitBoolLit(self, ctx, o):
        return 'bool'
 """
