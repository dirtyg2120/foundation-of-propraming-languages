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
        lst = reduce(lambda environ, decl: decl.accept(self, environ), ctx.param, [])
        reduce(lambda environ, decl: decl.accept(self, environ), ctx.body[0], lst)
        lst1 = lst + o + [ctx]
        reduce(lambda environ, expr: expr.accept(self, environ), ctx.body[1], lst1)
        return o + [ctx]

    # def visitProgram(self, ctx: Program, o: object):
    #     # decl:List[Decl]
    #     o = []
    #     for decl in ctx.decl:
    #         decl.accept(self, o)

    # def visitVarDecl(self, ctx: VarDecl, o: object):
    #     # name:str,typ:Type
    #     if ctx.name in o:
    #         raise RedeclaredVariable(ctx.name)
    #     o.append(ctx.name)
    #     ctx.typ.accept(self, o)

    # def visitConstDecl(self, ctx: ConstDecl, o: object):
    #     # name:str,val:Lit
    #     if ctx.name in o:
    #         raise RedeclaredConstant(ctx.name)
    #     o.append(ctx.name)
    #     ctx.val.accept(self, o)

    # def visitFuncDecl(self, ctx: FuncDecl, o: object):
    #     # name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    #     if ctx.name in o:
    #         raise RedeclaredFunction(ctx.name)
    #     o.append(ctx.name)
    #     lst = []
    #     for _param in ctx.param:
    #         _param.accept(self, lst)
    #     lst = lst + [ctx.name]
    #     for _decl in ctx.body[0]:
    #         _decl.accept(self, lst)
    #     lst1 = lst + o
    #     for _expr in ctx.body[1]:
    #         _expr.accept(self, lst1)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass

    def visitId(self, ctx: Id, o: object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
