import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                    Body:
                        foo();
                    EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))

    def test_no_entry_point_00(self):
        input = Program([])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_no_entry_point_01(self):
        input = """Function: foo
                    Body:
                    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_check_redeclared_00(self):
        input = """Function: main
                    Body:
                    EndBody.
                    Function: foo
                    Body:
                    EndBody.
                    Function: foo
                    Body:
                    EndBody."""
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_check_redeclared_01(self):
        input = """Var: x;
                    Var: x;
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_check_redeclared_02(self):
        input = """Function: main
                    Body:
                    EndBody.
                    Function: foo0
                    Body:
                    EndBody.
                    Function: foo1
                    Body:
                    EndBody.
                    Function: foo2
                    Body:
                    EndBody.
                    Function: foo3
                    Body:
                    EndBody.
                    Function: foo0
                    Body:
                    EndBody."""
        expect = str(Redeclared(Function(), "foo0"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_check_redeclared_03(self):
        input = """Function: main
                    Body:
                    EndBody.
                    Function: foo0
                    Body:
                    EndBody.
                    Function: foo1
                    Body:
                        Var: foo0;
                        Var: foo0;
                    EndBody."""
        expect = str(Redeclared(Variable(), "foo0"))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_check_redeclared_04(self):
        input = """ Var: x, y, z;
                    Var: y;
                    Function: main
                    Body:
                    EndBody.
                    Function: foo0
                    Body:
                        Var: random;
                    EndBody."""
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_check_undeclared_00(self):
        input = """ Var: x, y, z;
                    Var: tmp0 = tmp1;
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Undeclared(Variable(), "tmp1"))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_check_undeclared_01(self):
        input = """ Var: x, y, z;
                    Function: main
                    Body:
                        x = tmp;
                    EndBody."""
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 414))

    # def test01(self):
    #     input = """Function: main
    #                 Body:
    #                 EndBody."""
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 499))
