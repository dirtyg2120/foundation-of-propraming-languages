""" class Program: #decl:List[Decl],stmts:List[Stmt]

class Decl(ABC): #abstract class

class VarDecl(Decl): #name:str

class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]

class Stmt(ABC): #abstract class

class Assign(Stmt): #lhs:Id,rhs:Exp

class CallStmt(Stmt): #name:str,args:List[Exp]

class Exp(ABC): #abstract class

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str

and the Visitor class is declared as follows:
 """
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):pass

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitFuncDecl(self,ctx:FuncDecl,o): pass

    def visitCallStmt(self,ctx:CallStmt,o):pass

    def visitAssign(self,ctx:Assign,o): pass

    def visitIntLit(self,ctx:IntLit,o): pass 

    def visitFloatLit(self,ctx,o): pass

    def visitBoolLit(self,ctx,o): pass

    def visitId(self,ctx,o): pass