def visitBinExpr(self, ctx, o):
    e1 = self.visit(ctx.e1, o)
    e2 = self.visit(ctx.e2, o)
    if ctx.op == "+":
        return (
            e1[0] + e2[0] + self.emit.emitADDOP(ctx.op, IntType(), o.frame),
            IntType(),
        )
    elif ctx.op == "-":
        return (
            e1[0] + e2[0] + self.emit.emitADDOP(ctx.op, IntType(), o.frame),
            IntType(),
        )
    elif ctx.op == "*":
        return (
            e1[0] + e2[0] + self.emit.emitMULOP(ctx.op, IntType(), o.frame),
            IntType(),
        )
    elif ctx.op == "/":
        return (
            e1[0] + e2[0] + self.emit.emitMULOP(ctx.op, IntType(), o.frame),
            IntType(),
        )
    elif ctx.op == "+.":
        return (
            e1[0] + e2[0] + self.emit.emitADDOP("+", FloatType(), o.frame),
            FloatType(),
        )
    elif ctx.op == "-.":
        return (
            e1[0] + e2[0] + self.emit.emitADDOP("-", FloatType(), o.frame),
            FloatType(),
        )
    elif ctx.op == "*.":
        return (
            e1[0] + e2[0] + self.emit.emitMULOP("*", FloatType(), o.frame),
            FloatType(),
        )
    elif ctx.op == "/.":
        return (
            e1[0] + e2[0] + self.emit.emitMULOP("/", FloatType(), o.frame),
            FloatType(),
        )
