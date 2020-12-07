def visitBinExpr(self, ctx, o):
    e1, type1 = self.visit(ctx.e1, o)
    e2, type2 = self.visit(ctx.e2, o)

    result = ""
    resultType = None

    if ctx.op in ["+", "-"]:
        if isinstance(type1, IntType) and isinstance(type2, IntType):
            result = e1 + e2 + self.emit.emitADDOP(ctx.op, IntType(), o.frame)
            resultType = IntType()
        elif isinstance(type1, FloatType) and isinstance(type2, FloatType):
            result = e1 + e2 + self.emit.emitADDOP(ctx.op, FloatType(), o.frame)
            resultType = FloatType()
        elif isinstance(type1, FloatType) and isinstance(type2, IntType):
            result = (
                e1
                + e2
                + self.emit.emitI2F(o.frame)
                + self.emit.emitADDOP(ctx.op, FloatType(), o.frame)
            )
            resultType = FloatType()
        elif isinstance(type1, IntType) and isinstance(type2, FloatType):
            result = (
                e1
                + self.emit.emitI2F(o.frame)
                + e2
                + self.emit.emitADDOP(ctx.op, FloatType(), o.frame)
            )
            resultType = FloatType()
    elif ctx.op == "*":
        if isinstance(type1, IntType) and isinstance(type2, IntType):
            result = e1 + e2 + self.emit.emitMULOP(ctx.op, IntType(), o.frame)
            resultType = IntType()
        elif isinstance(type1, FloatType) and isinstance(type2, FloatType):
            result = e1 + e2 + self.emit.emitMULOP(ctx.op, FloatType(), o.frame)
            resultType = FloatType()
        elif isinstance(type1, FloatType) and isinstance(type2, IntType):
            result = (
                e1
                + e2
                + self.emit.emitI2F(o.frame)
                + self.emit.emitMULOP(ctx.op, FloatType(), o.frame)
            )
            resultType = FloatType()
        elif isinstance(type1, IntType) and isinstance(type2, FloatType):
            result = (
                e1
                + self.emit.emitI2F(o.frame)
                + e2
                + self.emit.emitMULOP(ctx.op, FloatType(), o.frame)
            )
            resultType = FloatType()
    elif ctx.op == "/":
        if isinstance(type1, IntType):
            e1 += self.emit.emitI2F(o.frame)
        if isinstance(type2, IntType):
            e2 += self.emit.emitI2F(o.frame)
        result = e1 + e2 + self.emit.emitMULOP(ctx.op, FloatType(), o.frame)
        returntype = FloatType()
    elif ctx.op in [">", "<", ">=", "<=", "!=", "=="]:
        if isinstance(type1, IntType):
            e1 += self.emit.emitI2F(o.frame)
        if isinstance(type2, IntType):
            e2 += self.emit.emitI2F(o.frame)
        result = e1 + e2 + self.emit.emitREOP(ctx.op, BoolType(), o.frame)
        returntype = BoolType()

    return (result, resultType)
