""" class Program: #decl:List[VarDecl],stmts:List[Assign]

class VarDecl: #name:str

class Assign: #lhs:Id,rhs:Exp

class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str


Type Mismatch In Expression: BinOp("-",Id("x"),FloatLit(2.1))
Type Mismatch In Statement: Assign(Id("z"),Id("x")) -> 2 ben khong cung kieu
Type Cannot Be Inferred: Assign(Id("x"),Id("y"))

"""


from functools import reduce


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        env = reduce(lambda x, y: y.accept(self, x) + x, ctx.decl, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return [ctx.name]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)

        env = reduce(lambda x, y: y.accept(self, x) + x, ctx.param, [])
        env = reduce(lambda x, y: y.accept(self, x) +
                     x, ctx.body[0], env+[ctx.name])

        scope = env + o
        exp = reduce(lambda x, y: y.accept(self, scope), ctx.body[1], scope)

        return [ctx.name]

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
