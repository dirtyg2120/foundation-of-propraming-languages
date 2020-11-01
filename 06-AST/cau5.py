from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools


class ASTGeneration(MPVisitor):

    def flatten(self, lst):
        flatten = [x for sublist in lst for x in sublist]
        return flatten

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(self.flatten([item.accept(self) for item in ctx.vardecl()]))

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return [VarDecl(
            item,
            ctx.mptype().accept(self)
        ) for item in ctx.ids().accept(self)]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        return [Id(item.getText()) for item in ctx.ID()]
