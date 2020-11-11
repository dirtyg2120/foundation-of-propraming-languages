from initial.src.main.bkit.utils.AST import Id
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()), [], None)])
        var_decl_lst = [element.accept(self)
                        for element in ctx.variable_declaration()]
        func_decl = [e.accept(self) for e in ctx.function_declaration()]

    def visitVariable_declaration(self, ctx: BKITParser.Variable_declarationContext):
        return ctx.variable_list().accept(self)

    def visitVariable_list(self, ctx):
        return [e.accept(self) for e in ctx.variable()]

    def visitVariable(self, ctx):
        if ctx.INT():
            varDimen_lst = [int(e.getText()) for e in ctx.INT()]
        else:
            varDimen_lst = []
        if ctx.literals():
            varInit = ctx.literals().accept(self)
        else:
            varInit = None
        return VarDecl(Id(ctx.ID().getText()), varDimen_lst, varInit)

    def visitFunc_declaration(self, ctx):
        if ctx.param_declaration():
            param = ctx.param_declaration().accept(self)
        else:
            param = []
        body = ctx.body().accept(self)
        return Function(Id(ctx.ID().getText()),param, body)
