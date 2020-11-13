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

    def test_var_06(self):
        input = """
            Var: arr_string = {"abc", "xyz", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at."};
        """
        expect = Program([VarDecl(Id("arr_string"), [], ArrayLiteral([StringLiteral("abc"), StringLiteral(
            "xyz"), StringLiteral("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at.")]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_var_07(self):
        input = """
            Var: v , a[1][2][4] , b = 6 ;
            Var: b = 7, v;
        """
        expect = Program([VarDecl(Id("v"), [], None), VarDecl(Id("a"), [1, 2, 4], None), VarDecl(
            Id("b"), [], IntLiteral(6)), VarDecl(Id("b"), [], IntLiteral(7)), VarDecl(Id("v"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_var_08(self):
        input = """
            Var: b[2][3] = {{2.99,3.99,4.99},{4.99,5.99,6.99}};
        """
        expect = Program([VarDecl(Id("b"), [2, 3], ArrayLiteral([ArrayLiteral([FloatLiteral(2.99), FloatLiteral(
            3.99), FloatLiteral(4.99)]), ArrayLiteral([FloatLiteral(4.99), FloatLiteral(5.99), FloatLiteral(6.99)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_var_10(self):
        input = """
            Var: lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at.";
        """
        expect = Program([VarDecl(Id("lorem"), [], StringLiteral(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at."))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
# ================Test Assignment================

    def test_assignment_00(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    i = 0;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple(
            [[VarDecl(Id("i"), [], None)], [Assign(Id("i"), IntLiteral(0))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_assignment_01(self):
        input = """
            Var: a, c, d, m;
            Function: foo
                Parameter: a, c, d, m
                Body:
                    Var: b[2][3], n[10];
                    a = 5;
                    b[2][3] = {{2,3,4},{4,5,6}};
                EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("m"), [], None), FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("m"), [], None)], tuple(
            [[VarDecl(Id("b"), [2, 3], None), VarDecl(Id("n"), [10], None)], [Assign(Id("a"), IntLiteral(5)), Assign(ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)]), ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_assignment_02(self):
        input = """
            Function: foo
                Body:
                    Var: boo;
                    boo = !!!True || False;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("boo"), [], None)], [Assign(Id("boo"), BinaryOp(
            "||", UnaryOp("!", UnaryOp("!", UnaryOp("!", BooleanLiteral(True)))), BooleanLiteral(True)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_assignment_03(self):
        input = """
            Function: foo
                Parameter: a , v , lst[10]
                Body:
                    Var: i = 10;
                    lst[i * a + v] = a;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None), VarDecl(Id("v"), [], None), VarDecl(Id("lst"), [10], None)], tuple(
            [[VarDecl(Id("i"), [], IntLiteral(10))], [Assign(ArrayCell(Id("lst"), [BinaryOp("+", BinaryOp("*", Id("i"), Id("a")), Id("v"))]), Id("a"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_assignment_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2
                Body:
                    Var: boo;
                    boo = !(tmp1 || !!tmp2) && tmp0;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [], None)], tuple(
            [[VarDecl(Id("boo"), [], None)], [Assign(Id("boo"), BinaryOp("&&", UnaryOp("!", BinaryOp("||", Id("tmp1"), UnaryOp("!", UnaryOp("!", Id("tmp2"))))), Id("tmp0")))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_assignment_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = tmp1 + lst[tmp1 - 2 * tmp1];
                    lst[tmp1 - 2 * tmp1] = 0;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("lst"), [10], None)], tuple([[], [Assign(Id("tmp0"), BinaryOp("+", Id("tmp1"), ArrayCell(
            Id("lst"), [BinaryOp("-", Id("tmp1"), BinaryOp("*", IntLiteral(2), Id("tmp1")))]))), Assign(ArrayCell(Id("lst"), [BinaryOp("-", Id("tmp1"), BinaryOp("*", IntLiteral(2), Id("tmp1")))]), IntLiteral(0))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_assignment_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    lst[0] = tmp0;
                    lst[2] = tmp1;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("lst"), [10], None)], tuple(
            [[], [Assign(ArrayCell(Id("lst"), [IntLiteral(0)]), Id("tmp0")), Assign(ArrayCell(Id("lst"), [IntLiteral(2)]), Id("tmp1"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_assignment_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = lst[2];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(
            Id("lst"), [10], None)], tuple([[], [Assign(Id("tmp0"), ArrayCell(Id("lst"), [IntLiteral(2)]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_assignment_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = True && tmp1;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(
            Id("lst"), [10], None)], tuple([[], [Assign(Id("tmp0"), BinaryOp("&&", BooleanLiteral(True), Id("tmp1")))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_assignment_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = !tmp1 && lst[0];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("lst"), [10], None)], tuple(
            [[], [Assign(Id("tmp0"), BinaryOp("&&", UnaryOp("!", Id("tmp1")), ArrayCell(Id("lst"), [IntLiteral(0)])))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
# ================Test If statement================

    def test_if_00(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [Assign(
            Id("tmp1"), IntLiteral(2))]]), tuple([BinaryOp("==", Id("tmp0"), IntLiteral(2)), [], [Assign(Id("tmp1"), IntLiteral(3))]])], tuple([[], [Assign(Id("tmp1"), IntLiteral(100))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_if_01(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(
            1)), [], [CallStmt(Id("println"), [StringLiteral("tmp0 = 1")])]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1 & tmp1 != 1")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_if_02(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [CallStmt(
            Id("println"), [StringLiteral("tmp0 = 1")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 1")])]])], tuple([[], []]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_if_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple(
            [[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp0 = 1")])]])], tuple([[], []]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If (tmp0 == 1) || (tmp0 == 2) Then println("tmp0 = 1 or 2");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [If([tuple([BinaryOp("||", BinaryOp("==", Id("tmp0"), IntLiteral(1)), BinaryOp("==", Id("tmp0"), IntLiteral(2))), [], [CallStmt(
            Id("println"), [StringLiteral("tmp0 = 1 or 2")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 1")])]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1 & tmp1 != 1")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_if_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If (tmp0 == 1) && (tmp1 != 1) Then println("tmp0 == 1 & tmp1 != 1");
                    ElseIf (tmp0 != 1) && (tmp1 == 1) Then println("tmp0 != 1 & tmp1 = 1");
                    Else println("IDK");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [If([tuple([BinaryOp("&&", BinaryOp("==", Id("tmp0"), IntLiteral(1)), BinaryOp("!=", Id("tmp1"), IntLiteral(1))), [], [CallStmt(Id("println"), [StringLiteral(
            "tmp0 == 1 & tmp1 != 1")])]]), tuple([BinaryOp("&&", BinaryOp("!=", Id("tmp0"), IntLiteral(1)), BinaryOp("==", Id("tmp1"), IntLiteral(1))), [], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1 & tmp1 = 1")])]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("IDK")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_if_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then tmp1 = 1;
                    ElseIf tmp0 == 2 Then tmp1 = 2;
                    ElseIf tmp0 == 3 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [Assign(Id("tmp1"), IntLiteral(1))]]), tuple(
            [BinaryOp("==", Id("tmp0"), IntLiteral(2)), [], [Assign(Id("tmp1"), IntLiteral(2))]]), tuple([BinaryOp("==", Id("tmp0"), IntLiteral(3)), [], [Assign(Id("tmp1"), IntLiteral(3))]])], tuple([[], [Assign(Id("tmp1"), IntLiteral(100))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_if_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    ElseIf tmp1 == 2 Then println("tmp1 = 2");
                    ElseIf tmp1 == 3 Then println("tmp1 = 3");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp0 = 1")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(1)), [], [CallStmt(Id("println"), [
                         StringLiteral("tmp1 = 1")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 2")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 3")])]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1 & tmp1 != 1")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_if_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then
                        If tmp1 == 1 Then println("tmp1 = 1");
                        ElseIf tmp1 == 2 Then println("tmp1 = 2");
                        ElseIf tmp1 == 3 Then println("tmp1 = 3");
                        Else println("tmp0 != 1 & tmp1 != 1");
                        EndIf.
                    Else println("tmp0 != 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [If([tuple([BinaryOp("==", Id("tmp1"), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 1")])]]), tuple([BinaryOp("==", Id(
            "tmp1"), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 2")])]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 3")])]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1 & tmp1 != 1")])]]))]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_if_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then
                        If tmp1 == 1 Then
                            If tmp2[10][0] == 1 Then println("tmp2[10][0] = 1");
                            ElseIf tmp2[10][0] == 2 Then println("tmp2[10][0] = 2");
                            ElseIf tmp2[10][0] == 3 Then println("tmp2[10][0] = 3");
                            EndIf.
                        ElseIf tmp1 == 2 Then
                            If tmp2[10][4] == 1 Then println("tmp2[10][4] = 1");
                            ElseIf tmp2[10][4] == 2 Then println("tmp2[10][4] = 2");
                            ElseIf tmp2[10][4] == 3 Then println("tmp2[10][4] = 3");
                            EndIf.
                        ElseIf tmp1 == 3 Then println("tmp1 = 3");
                        EndIf.
                    Else println("tmp0 != 1");
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[], [If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [If([tuple([BinaryOp("==", Id("tmp1"), IntLiteral(1)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(0)]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][0] = 1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(0)]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][0] = 2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(0)]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][0] = 3")])]])], tuple([[], []]))]]), tuple(
            [BinaryOp("==", Id("tmp1"), IntLiteral(2)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(4)]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][4] = 1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(4)]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][4] = 2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), IntLiteral(4)]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("tmp2[10][4] = 3")])]])], tuple([[], []]))]]), tuple([BinaryOp("==", Id("tmp1"), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("tmp1 = 3")])]])], tuple([[], []]))]])], tuple([[], [CallStmt(Id("println"), [StringLiteral("tmp0 != 1")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

# ================Test For statement================

    def test_for_00(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None)], [For(Id("i"), IntLiteral(
            0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), tuple([[], [CallStmt(Id("writeln"), [Id("i")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_for_01(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None)], [For(
            Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), tuple([[], []]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_for_02(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        For (j = 0, j < 10, 2) Do
                            writeln(i + j);
                        EndFor.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), tuple(
            [[], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(2), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("+", Id("i"), Id("j"))])]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_for_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , i < tmp0 * tmp1 , tmp2[4]) Do
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [10], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("tmp"), [], IntLiteral(1))], [For(
            Id("i"), BinaryOp("+", Id("tmp0"), Id("tmp1")), BinaryOp("<", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp1"))), ArrayCell(Id("tmp2"), [IntLiteral(4)]), tuple([[], [Assign(Id("tmp"), BinaryOp("*", Id("tmp"), Id("i")))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_for_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [10], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("tmp"), [], IntLiteral(1))], [For(Id("i"), BinaryOp("+", Id("tmp0"), Id("tmp1")),
                                                                                                                                                                                                                                BinaryOp("||", BinaryOp("<", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp1"))), BinaryOp("!=", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp0")))), ArrayCell(Id("tmp2"), [IntLiteral(4)]), tuple([[], [Assign(Id("tmp"), BinaryOp("*", Id("tmp"), Id("i")))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_for_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        If i % 2 == 0 Then Continue;EndIf.
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [10], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("tmp"), [], IntLiteral(1))], [For(Id("i"), BinaryOp("+", Id("tmp0"), Id("tmp1")), BinaryOp("||", BinaryOp("<", Id("i"), BinaryOp("*", Id(
            "tmp0"), Id("tmp1"))), BinaryOp("!=", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp0")))), ArrayCell(Id("tmp2"), [IntLiteral(4)]), tuple([[], [If([tuple([BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [Continue()]])], tuple([[], []])), Assign(Id("tmp"), BinaryOp("*", Id("tmp"), Id("i")))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_for_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        If i % 2 == 0 Then Continue;
                        ElseIf (i == tmp0 * 2) || (i == tmp1 * 2) Then Break; 
                        EndIf.
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [10], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("tmp"), [], IntLiteral(1))], [For(Id("i"), BinaryOp("+", Id("tmp0"), Id("tmp1")), BinaryOp("||", BinaryOp("<", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp1"))), BinaryOp("!=", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp0")))),
                                                                                                                                                                                                                                ArrayCell(Id("tmp2"), [IntLiteral(4)]), tuple([[], [If([tuple([BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [Continue()]]), tuple([BinaryOp("||", BinaryOp("==", Id("i"), BinaryOp("*", Id("tmp0"), IntLiteral(2))), BinaryOp("==", Id("i"), BinaryOp("*", Id("tmp1"), IntLiteral(2)))), [], [Break()]])], tuple([[], []])), Assign(Id("tmp"), BinaryOp("*", Id("tmp"), Id("i")))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_for_07(self):
        input = """
            Function: foo
                Body:
                    Var: i, j;
                    For (i = 0, i < 10, 2) Do
                        For (j = 0, j < 10, 2) Do
                            writeln(i * j);
                        EndFor.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(
            2), tuple([[], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(2), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("*", Id("i"), Id("j"))])]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_for_08(self):
        input = """
            Function: foo
                Body:
                    Var: i, j, k;
                    For (i = 0, i < 10, 1) Do
                        For (j = 0, j < 10, 1) Do
                            For (k = 0, k < 10, 1) Do
                                writeln(i * j * k);
                            EndFor.
                        EndFor.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None), VarDecl(Id("k"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("j"), IntLiteral(
            0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(10)), IntLiteral(1), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("*", BinaryOp("*", Id("i"), Id("j")), Id("k"))])]]))]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_for_09(self):
        input = """
            Function: foo
                Body:
                    Var: i,j,k;
                    For (i = 0, i < 10, 2) Do
                        writeln(i);
                    EndFor.
                    For (i = 0, i < 10, 1) Do
                        For (j = 0, j < 10, 1) Do
                            For (k = 0, k < 10, 1) Do
                                writeln(i * j * k);
                            EndFor.
                        EndFor.
                    EndFor.
                    For (i = 0, i < 10, 1) Do
                        For (j = 0, j < 10, 1) Do
                            For (k = 0, k < 10, 1) Do
                                writeln(i * j * k);
                            EndFor.
                        EndFor.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None), VarDecl(Id("k"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), tuple([[], [CallStmt(Id("writeln"), [Id("i")])]])), For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(
            10)), IntLiteral(1), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("*", BinaryOp("*", Id("i"), Id("j")), Id("k"))])]]))]]))]])), For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(1), tuple([[], [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(10)), IntLiteral(1), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("*", BinaryOp("*", Id("i"), Id("j")), Id("k"))])]]))]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

# ================Test while statement================

    def test_while_00(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        writeln(i);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[CallStmt(Id("writeln"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_while_01(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0, j;
                    While i < 10 Do
                        For (j = i, j < 10, i) Do
                            writeln(j);
                        EndFor.
                        i = i + 1;
                   EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[For(Id("j"),Id("i"),BinaryOp("<",Id("j"),IntLiteral(10)),Id("i"),tuple([[],[CallStmt(Id("writeln"),[Id("j")])]])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_while_02(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    While (i < 10) Do
                        Var: tmp = i * i;
                        writeln(tmp);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[VarDecl(Id("tmp"),[],BinaryOp("*",Id("i"),Id("i")))],[CallStmt(Id("writeln"),[Id("tmp")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_while_03(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    While (i < 100) && i % 2 > 3 Do
                        Var: tmp = i * i;
                        writeln(tmp);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],None)],[While(BinaryOp(">",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(100)),BinaryOp("%",Id("i"),IntLiteral(2))),IntLiteral(3)),tuple([[VarDecl(Id("tmp"),[],BinaryOp("*",Id("i"),Id("i")))],[CallStmt(Id("writeln"),[Id("tmp")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_while_04(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0, j;
                    While (i < 10)
                        For (j = 0, j < 10, 2) Do
                            writeln(i * j);
                        EndFor.
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None)],[]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_while_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 0, tmp[10][10];
                    While (i <= 10) Do
                        If tmp2[10][i] == 1 Then println("1");
                        ElseIf tmp2[10][i] == 2 Then println("2");
                        ElseIf tmp2[10][i] == 3 Then println("3");
                        EndIf.
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp0"),[],None),VarDecl(Id("tmp1"),[],None),VarDecl(Id("tmp2"),[12,4],None)],tuple([[VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("tmp"),[10,10],None)],[While(BinaryOp("<=",Id("i"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(1)),[],[CallStmt(Id("println"),[StringLiteral("1")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(2)),[],[CallStmt(Id("println"),[StringLiteral("2")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(3)),[],[CallStmt(Id("println"),[StringLiteral("3")])]])],tuple([[],[]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_while_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        If i % 2 != 0 Then writeln(i);EndIf.
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp0"),[],None),VarDecl(Id("tmp1"),[],None),VarDecl(Id("tmp2"),[12,4],None)],tuple([[VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("writeln"),[Id("i")])]])],tuple([[],[]])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_while_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        If i % 2 != 0 Then
                            If tmp2[10][i] == 1 Then println("1");
                            ElseIf tmp2[10][i] == 2 Then println("2");
                            ElseIf tmp2[10][i] == 3 Then println("3");
                            EndIf.
                        EndIf.
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp0"),[],None),VarDecl(Id("tmp1"),[],None),VarDecl(Id("tmp2"),[12,4],None)],tuple([[VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[If([tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(1)),[],[CallStmt(Id("println"),[StringLiteral("1")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(2)),[],[CallStmt(Id("println"),[StringLiteral("2")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(3)),[],[CallStmt(Id("println"),[StringLiteral("3")])]])],tuple([[],[]]))]])],tuple([[],[]])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_while_08(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        Var: j = 0;
                        writeln(i);
                        While (j < 10) Do
                            If (i + j) % 2 != 0 Then
                                If tmp2[10][i] == 1 Then println("1");
                                ElseIf tmp2[10][i] == 2 Then println("2");
                                ElseIf tmp2[10][i] == 3 Then println("3");
                                EndIf.
                            EndIf.
                            j = j + 1;
                        EndWhile.
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[VarDecl(Id("j"),[],IntLiteral(0))],[CallStmt(Id("writeln"),[Id("i")]),While(BinaryOp("<",Id("j"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("!=",BinaryOp("%",BinaryOp("+",Id("i"),Id("j")),IntLiteral(2)),IntLiteral(0)),[],[If([tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(1)),[],[CallStmt(Id("println"),[StringLiteral("1")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(2)),[],[CallStmt(Id("println"),[StringLiteral("2")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(3)),[],[CallStmt(Id("println"),[StringLiteral("3")])]])],tuple([[],[]]))]])],tuple([[],[]])),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_while_09(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        If i % 2 != 0 Then
                            If tmp2[10][i] == 1 Then println("1");
                            ElseIf tmp2[10][i] == 2 Then println("2");
                            ElseIf tmp2[10][i] == 3 Then println("3");
                            Else
                                Var: i;
                                While (i < 10) Do
                                    Var: tmp = i * i;
                                    writeln(tmp);
                                    i = i + 1;
                                EndWhile.
                            EndIf.
                        EndIf.
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[If([tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(1)),[],[CallStmt(Id("println"),[StringLiteral("1")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(2)),[],[CallStmt(Id("println"),[StringLiteral("2")])]]),tuple([BinaryOp("==",ArrayCell(Id("tmp2"),[IntLiteral(10),Id("i")]),IntLiteral(3)),[],[CallStmt(Id("println"),[StringLiteral("3")])]])],tuple([[VarDecl(Id("i"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[VarDecl(Id("tmp"),[],BinaryOp("*",Id("i"),Id("i")))],[CallStmt(Id("writeln"),[Id("tmp")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))]])],tuple([[],[]])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
