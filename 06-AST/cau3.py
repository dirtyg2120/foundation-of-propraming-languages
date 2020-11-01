from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if(ctx.getChildCount() == 2):
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
        return []

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ = ctx.mptype().accept(self)
        return [VarDecl(i, typ) for i in ctx.ids().accept(self)]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return FloatType() if ctx.FLOATTYPE() else IntType()

    def visitIds(self, ctx: MPParser.IdsContext):
        return [Id(ctx.ID().getText())] + ctx.ids().accept(self) if ctx.ids() else [Id(ctx.ID().getText())]
