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

and the Visitor class is declared as follows:
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