class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 1 + ctx.vardecls().accept(self)

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if(ctx.getChildCount() == 2):
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
        else:
            return 0

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 2 + ctx.ids().accept(self)

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if(ctx.getChildCount() == 1):
            return 1
        if(ctx.getChildCount() == 3):
            return 2 + ctx.ids().accept(self)
