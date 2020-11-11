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

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
