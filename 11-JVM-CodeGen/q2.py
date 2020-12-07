def visitFloatLiteral(self, ctx, o):
    return (self.emit.emitPUSHFCONST(float(ctx.value), o.frame), FloatType())
