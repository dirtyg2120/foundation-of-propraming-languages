from main.bkit.utils.AST import *
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
# from AST import *
from AST_copy import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()), [], None)])
        var_decl_lst = flatten([element.accept(self)
                                for element in ctx.variable_declaration()])  # cần flatten lại cái thằng này
        func_decl = [e.accept(self) for e in ctx.func_declaration()]
        return Program(var_decl_lst + func_decl)

    def visitVariable_declaration(self, ctx: BKITParser.Variable_declarationContext):
        return ctx.variable_list().accept(self)

    def visitVariable_list(self, ctx):
        # dễ tạo list trong list
        return [e.accept(self) for e in ctx.variable()]

    def visitVariable(self, ctx):
        varDimen_lst = [int(e.getText())
                        for e in ctx.INT()] if ctx.INT() else []
        varInit = ctx.exp().accept(self) if ctx.exp() else None
        return VarDecl(Id(ctx.ID().getText()), varDimen_lst, varInit)

    def visitFunc_declaration(self, ctx):
        param = ctx.param_declaration().accept(self) if ctx.param_declaration() else []
        body = ctx.body().accept(self)
        return FuncDecl(Id(ctx.ID().getText()), param, body)

    def visitParam_declaration(self, ctx):
        return ctx.param_list().accept(self)

    def visitParam_list(self, ctx):
        return [e.accept(self) for e in ctx.param()]

    def visitParam(self, ctx):
        varDimen_lst = [int(e.getText())
                        for e in ctx.INT()] if ctx.INT() else []
        return VarDecl(Id(ctx.ID().getText()), varDimen_lst, None)

    def visitBody(self, ctx):
        mini_body = ctx.mini_body().accept(self)
        return (mini_body[0], mini_body[1])

    def visitMini_body(self, ctx):
        var_decl_lst = []
        stmt_lst = []
        if ctx.variable_declaration():
            var_decl_lst = flatten([element.accept(self)
                                    for element in ctx.variable_declaration()])
        if ctx.stmt():
            stmt_lst = [element.accept(self) for element in ctx.stmt()]
        return [var_decl_lst, stmt_lst]

    def visitStmt(self, ctx):
        return ctx.getChild(0).accept(self)

    def visitStatement_assign(self, ctx):
        lhs = Id(ctx.ID().getText()) if ctx.ID(
        ) else ctx.array_cell_decl().accept(self)
        rhs = ctx.exp().accept(self)
        return Assign(lhs, rhs)

    def visitArray_cell_decl(self, ctx):
        arr = Id(ctx.ID().getText()) if ctx.ID(
        ) else ctx.function_call().accept(self)
        exp_lst = [e.accept(self) for e in ctx.exp()]
        return ArrayCell(arr, exp_lst)

    def visitStatement_if(self, ctx):
        ifThenStmt_lst = [ctx.if_then_stmt().accept(self)]
        if ctx.else_if_stmt():
            ifThenStmt_lst = ifThenStmt_lst + \
                [e.accept(self) for e in ctx.else_if_stmt()]
        elseStmt = (ctx.else_stmt().accept(self)
                    ) if ctx.else_stmt() else ([], [])
        return If(ifThenStmt_lst, elseStmt)

    def visitIf_then_stmt(self, ctx):
        expr = ctx.exp().accept(self)
        then_stmt = ctx.mini_body().accept(self)
        return (expr, then_stmt[0], then_stmt[1])

    def visitElse_if_stmt(self, ctx):
        expr = ctx.exp().accept(self)
        then_stmt = ctx.mini_body().accept(self)
        return (expr, then_stmt[0], then_stmt[1])

    def visitElse_stmt(self, ctx):
        then_stmt = ctx.mini_body().accept(self)
        return (then_stmt[0], then_stmt[1])

    def visitStatement_for(self, ctx):
        mini_body = ctx.mini_body().accept(self)
        loop = (mini_body[0], mini_body[1])
        return For(Id(ctx.ID().getText()), ctx.exp(0).accept(self), ctx.exp(1).accept(self), ctx.exp(2).accept(self), loop)

    def visitStatement_while(self, ctx):
        expr = ctx.exp().accept(self)
        mini_body = ctx.mini_body().accept(self)

        sl = (mini_body[0], mini_body[1])
        return While(expr, sl)

    def visitStatement_do_while(self, ctx):
        mini_body = ctx.mini_body().accept(self)
        sl = (mini_body[0], mini_body[1])
        expr = ctx.exp().accept(self)
        return Dowhile(sl, expr)

    def visitStatement_break(self, ctx):
        return Break()

    def visitStatement_continue(self, ctx):
        return Continue()

    def visitStatement_call(self, ctx):
        func_call = ctx.function_call().accept(self)
        return CallStmt(func_call.method, func_call.param)

    def visitStatement_return(self, ctx):
        expr = ctx.exp().accept(self) if ctx.exp() else None
        return Return(expr)

    def visitFunction_call(self, ctx):
        method = Id(ctx.ID().getText())
        param = [e.accept(self) for e in ctx.exp()]
        return CallExpr(method, param)

    def visitExp(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.exp1(0).accept(self)
        op = ctx.getChild(1).getText()
        left = ctx.exp1(0).accept(self)
        right = ctx.exp1(1).accept(self)
        return BinaryOp(op, left, right)

    def visitExp1(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.exp2().accept(self)
        op = ctx.getChild(1).getText()
        left = ctx.exp1().accept(self)
        right = ctx.exp2().accept(self)
        return BinaryOp(op, left, right)

    def visitExp2(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.exp3().accept(self)
        op = ctx.getChild(1).getText()
        left = ctx.exp2().accept(self)
        right = ctx.exp3().accept(self)
        return BinaryOp(op, left, right)

    def visitExp3(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.exp4().accept(self)
        op = ctx.getChild(1).getText()
        left = ctx.exp3().accept(self)
        right = ctx.exp4().accept(self)
        return BinaryOp(op, left, right)

    def visitExp4(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.exp5().accept(self)
        op = ctx.getChild(0).getText()
        body = ctx.exp4().accept(self)
        return UnaryOp(op, body)

    def visitExp5(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.operand().accept(self)
        op = ctx.getChild(0).getText()
        body = ctx.exp5().accept(self)
        return UnaryOp(op, body)

    def visitOperand(self, ctx):
        if ctx.getChildCount() == 3:
            return ctx.exp().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return ctx.getChild(0).accept(self)

    def visitLiteral(self, ctx):
        if ctx.INT():
            _int = ctx.INT().getText()
            if "o" in _int or "O" in _int:
                return IntLiteral(int(_int,8))
            elif "x" in _int or "X" in _int:
                return IntLiteral(int(_int,16))
            else:
                return IntLiteral(int(_int))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(bool(ctx.BOOLEAN().getText() == 'True'))
        elif ctx.STRING():
            return StringLiteral(str(ctx.STRING().getText()))
        return ctx.getChild(0).accept(self)

    def visitArray_literal(self, ctx):
        value = [e.accept(self) for e in ctx.exp()]
        return ArrayLiteral(value)


def flatten(lst):
    return list(reduce(lambda x, y: x+y, lst, []))
