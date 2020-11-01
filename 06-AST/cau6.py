from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

from functools import reduce


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return ctx.exp().accept(self)

    def visitExp(self, ctx: MPParser.ExpContext):
        temp_term = ctx.term()
        list_assign = list(zip(ctx.ASSIGN(), temp_term[:-1]))[::-1]
        return reduce(lambda x, y: Binary(y[0].getText(), y[1].accept(self), x),  list_assign, ctx.term()[-1].accept(self))

    def visitTerm(self, ctx: MPParser.TermContext):
        if ctx.COMPARE():
            return Binary(
                ctx.COMPARE().getText(),
                ctx.factor(0).accept(self),
                ctx.factor(1).accept(self)
            )
        else:
            return ctx.factor(0).accept(self)

    def visitFactor(self, ctx: MPParser.FactorContext):
        # if ctx.ANDOR():
        operands = ctx.operand()
        and_or = list(zip(ctx.ANDOR(), operands[1:]))
        return reduce(lambda x, y: Binary(y[0].getText(), x, y[1].accept(self)), and_or, ctx.operand(0).accept(self))
        # else:
        # return ctx.operand(0).accept(self)

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.getChildCount() == 3:
            return ctx.exp().accept(self)
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.BOOLIT():
                return BooleanLiteral(ctx.BOOLIT().getText() == "True")
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
