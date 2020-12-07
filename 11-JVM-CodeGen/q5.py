def visitId(self, ctx, o):
    result = ""
    idtype = None
    for sym in o.sym:
        if ctx.name == sym.name:
            idtype = sym.mtype
            if isinstance(sym.value, Index):
                result = self.emit.emitREADVAR(
                    sym.name, sym.mtype, sym.value.value, o.frame
                )
            elif isinstance(sym.value, CName):
                result = self.emit.emitGETSTATIC(
                    sym.value.value + "." + sym.name, sym.mtype, o.frame
                )
            break
    return (result, idtype)
