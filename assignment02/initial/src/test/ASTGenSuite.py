import unittest
from TestUtils import TestAST
# from AST import *
from AST_copy import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

# ================Test Variable================

    def test_var_00(self):
        input = """
            Var: a = 5;
        """
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_var_01(self):
        input = """
            Var: arr[3] = {0,1,2};
        """
        expect = Program([VarDecl(Id("arr"), [3], ArrayLiteral(
            [IntLiteral(0), IntLiteral(1), IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_var_02(self):
        input = """
            Var: c, d = 6, e, f;
        """
        expect = Program([VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], IntLiteral(
            6)), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_var_03(self):
        input = """
            Var: m, n[10];
        """
        expect = Program([VarDecl(Id("m"), [], None),
                          VarDecl(Id("n"), [10], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_var_04(self):
        input = """
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
        """
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5)), VarDecl(Id("b"), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(
            5), IntLiteral(6)])])), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None), VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_var_05(self):
        input = """
            Var: a = 10;
            Var: b;
            Var: c[100][50];
            Var: d = "Lorem ipsum dolor sit amet";
        """
        expect = Program([VarDecl(Id("a"), [], IntLiteral(10)), VarDecl(Id("b"), [], None), VarDecl(
            Id("c"), [100, 50], None), VarDecl(Id("d"), [], StringLiteral("Lorem ipsum dolor sit amet"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    # def test_var_06(self):
    #     input = """
    #         Var: error_mix = abc * j \\. 123 + ff;
    #     """
    #     expect = "Error on line 2 col 29: abc"
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    # def test_var_07(self):
    #     input = """
    #         Var: v , a[1][2][4] , b = 6 ;
    #         Var: b = 7, v;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    # def test_var_08(self):
    #     input = """
    #         Var: a = "** **" * 4;
    #     """
    #     expect = "Error on line 2 col 29: *"
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    # def test_var_10(self):
    #     input = """
    #         Var: lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at."
    #     """
    #     expect = "Error on line 3 col 8: <EOF>"
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 329))
