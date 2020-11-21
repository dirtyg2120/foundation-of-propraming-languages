""" class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

class UnOp(Exp): #op:str,e:Exp #op is -, !

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

and the Visitor class is declared as follows.

If the expression does not conform the type constraints,
the StaticCheck will raise exception TypeMismatchInExpression with
the innermost sub-expression that contains type mismatch.

"""


class StaticCheck(Visitor):

    def visitBinOp(self, ctx: BinOp, o):
        type1 = self.visit(ctx.e1, o)
        type2 = self.visit(ctx.e2, o)

        op = ctx.op
        if op in ('+', '-', '*', '/'):
            if 'bool' in (type1, type2):
                raise TypeMismatchInExpression(ctx)
            if op == '/' or 'float' in (type1, type2):
                return 'float'
            return 'int'
        elif op in ('&&', '||'):
            if 'bool' not in (type1, type2):
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif op in ('<', '>', '==', '!='):
            if type1 != type2:
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        return

    def visitUnOp(self, ctx: UnOp, o):
        type0 = self.visit(ctx.e, o)
        op = ctx.op

        if op == '!' and type0 != 'bool':
            raise TypeMismatchInExpression(ctx)
        elif op =='-' and type0 not in ('int','float'):
            raise TypeMismatchInExpression(ctx)
        return type0

    def visitIntLit(self, ctx: IntLit, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"
