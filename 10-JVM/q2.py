""" class Program: #decl:List[VarDecl],stmts:List[Stmt]

class VarDecl: #name:str

class Stmt(ABC): #abstract class

class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]

class Assign(Stmt): #lhs:Id,rhs:Exp

class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str


In an assignment statement, the type of lhs must be the same as that
of rhs, otherwise, the exception TypeMismatchInStatement should be
raised together with the assignment statement.


The type of an Id is inferred from the above constraints in the first
usage, 
    If the Id is not in the declarations, exception
    UndeclaredIdentifier should be raised together with the name
    of the Id, or

    If the Id cannot be inferred in the first usage, exception
    TypeCannotBeInferred should be raised together with the
    assignment statement which contains the type-unresolved identifier.


For static referencing environment, this language applies the scope rules of block-structured programming language. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
If an expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the expression.

Test:
Program([VarDecl("x")],[Assign(Id("x"),IntLit(3)),Block([VarDecl("y")],[Assign(Id("x"),Id("y")),Assign(Id("y"),BoolLit(True))])])

Result:
Type Mismatch In Statement: Assign(Id("y"),BoolLit(True))

 """
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):pass

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitBlock(self,ctx:Block,o): pass

    def visitAssign(self,ctx:Assign,o): pass

    def visitBinOp(self,ctx:BinOp,o): pass

    def visitUnOp(self,ctx:UnOp,o):pass

    def visitIntLit(self,ctx:IntLit,o): pass 

    def visitFloatLit(self,ctx,o): pass

    def visitBoolLit(self,ctx,o): pass

    def visitId(self,ctx,o): pass