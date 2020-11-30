def tmp():
    def visitIntLiteral(self, ctx, o):
        return (self.emit.emitPUSHICONST(self, ctx.frame, ctx.frame.))
