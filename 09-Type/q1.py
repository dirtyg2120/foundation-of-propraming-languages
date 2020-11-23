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
        if ctx.op in ['+', '-', '*', '/']:
            if 'bool' in [type1,type2]:
                raise TypeMismatchInExpression(ctx)
            if 'float' in [type1,type2] or ctx.op == '/':
                return 'float'
            return 'int'
        elif ctx.op in ['&&', '||']:
            if type1 != 'bool' or type2 != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        elif ctx.op in ['<', '>', '==', '!=']:
            if type1 != type2:
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self, ctx: UnOp, o):
        operand_type = self.visit(ctx.e, o)
        if ctx.op == '-' and operand_type == 'bool':
            raise TypeMismatchInExpression(ctx)
        elif ctx.op == '!' and operand_type != 'bool':
            raise TypeMismatchInExpression(ctx)
        return operand_type

    def visitIntLit(self, ctx: IntLit, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"
