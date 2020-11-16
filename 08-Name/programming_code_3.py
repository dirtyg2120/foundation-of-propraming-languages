from functools import reduce


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda acc, ele: ele.accept(self, acc), ctx.decl, [])

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if len(list(filter(lambda x: x.name == ctx.name, o))):
            raise RedeclaredVariable(ctx.name)
        return o + [ctx]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if len(list(filter(lambda x: x.name == ctx.name, o))):
            raise RedeclaredConstant(ctx.name)
        return o + [ctx]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if len(list(filter(lambda x: x.name == ctx.name, o))):
            raise RedeclaredFunction(ctx.name)
        o = o + [ctx]
        lst = reduce(lambda acc, ele: ele.accept(self, acc), ctx.param, [])
        reduce(lambda environ, decl: decl.accept(self, environ), ctx.body, lst)
        return o

    # def visitProgram(self, ctx: Program, o: object):
    #     o = []
    #     for decl in ctx.decl:
    #         decl.accept(self, o)

    # def visitVarDecl(self, ctx: VarDecl, o: object):
    #     if ctx.name in o:
    #         raise RedeclaredVariable(ctx.name)
    #     o.append(ctx.name)
    #     ctx.typ.accept(self, o)

    # def visitConstDecl(self, ctx: ConstDecl, o: object):
    #     if ctx.name in o:
    #         raise RedeclaredConstant(ctx.name)
    #     o.append(ctx.name)
    #     ctx.val.accept(self, o)

    # def visitFuncDecl(self, ctx: FuncDecl, o: object):
    #     if ctx.name in o:
    #         raise RedeclaredFunction(ctx.name)
    #     o.append(ctx.name)
    #     lst = []
    #     for param in ctx.param:
    #         param.accept(self, lst)
    #     for body in ctx.body:
    #         body.accept(self, lst)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
