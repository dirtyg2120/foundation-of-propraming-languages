from dataclasses import dataclass
from abc import ABC
from typing import List


@dataclass
class Program:
    decl: List[Decl]


class Decl(ABC):  # abstract class
    pass


class VarDecl(Decl):
    name: str
    typ: Type


class ConstDecl(Decl):
    name: str
    val: Lit


class Type(ABC):  # abstract class
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class Lit(ABC):  # abstract class
    pass


class IntLit(Lit):
    val: int


class RedeclaredDeclaration(Exception):
    name: str


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decl:
            decl.accept(self, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o.append(ctx.name)
        ctx.typ.accept(self, o)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o.append(ctx.name)
        ctx.val.accept(self, o)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
