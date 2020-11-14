import unittest
from TestUtils import TestAST
from AST import *
# from AST_copy import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_random_01(self):
        input = """**Empty program**"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_random_02(self):
        input = """
            Var:x;
            Function: foo
                Parameter: param
                Body:
                EndBody.
"""
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[VarDecl(Id("param"),[],None)],tuple([[],[]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_random_03(self):
        input = """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.

            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],tuple([[],[If([tuple([BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]])],tuple([[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]]))]])),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_random_04(self):
        """If statement"""
        input = """
            Function: main
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return 2;
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],tuple([[],[If([tuple([BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]])],tuple([[],[Return(IntLiteral(2))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_random_05(self):
        """For statement"""
        input = """
            Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    x = (0 + 199 - 0xFF * 0XABC \ 0o567 % 0O77) * i;
                    println(x);
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],tuple([[],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),tuple([[],[Assign(Id("x"),BinaryOp("*",BinaryOp("-",BinaryOp("+",IntLiteral(0),IntLiteral(199)),BinaryOp("%",BinaryOp("\\",BinaryOp("*",IntLiteral(255),IntLiteral(2748)),IntLiteral(375)),IntLiteral(63))),Id("i"))),CallStmt(Id("println"),[Id("x")])]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_random_06(self):
        """While statement"""
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    While (i < 10) Do
                        println(x);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(100)),While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))


    def test_literal_4(self):
        """Simple program: int main() {} """
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    Var: x = "This is a string", y = "";
                    Var: z = **comment** "This \\n is \\t a '" string '"";
                    x = 100;
                    Do
                        println(x);
                        i = i + 1;
                    While (i < 10) EndDo.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],tuple([[VarDecl(Id("x"),[],StringLiteral("This is a string")),VarDecl(Id("y"),[],StringLiteral("")),VarDecl(Id("z"),[],StringLiteral("This \\n is \\t a '\" string '\""))],[Assign(Id("x"),IntLiteral(100)),Dowhile(tuple([[],[CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]),BinaryOp("<",Id("i"),IntLiteral(10)))]]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))


    def test_random_08(self):
        """Continue statement"""
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    While (i < 10) Do
                        println(x);
                        i = i + 1;
                        Continue;
                    EndWhile.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(100)),While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Continue()]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_random_09(self):
        """For and If statement"""
        input = """
            Function: main
                Body:
                    For (i = 0, i < 10, 2) Do
                        If (i % 2 == 0) Then
                            println("Chan");
                        ElseIf (i % 2 != 0) Then
                            println("Le");
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],tuple([[],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),tuple([[],[If([tuple([BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("println"),[StringLiteral("Chan")])]]),tuple([BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("println"),[StringLiteral("Le")])]])],tuple([[],[]]))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_random_10(self):
        """COntinue in While statement"""
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    While (i < 10) Do
                        If (i % 2 == 0) Then
                            Continue;
                        EndIf.
                        println(x);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(100)),While(BinaryOp("<",Id("i"),IntLiteral(10)),tuple([[],[If([tuple([BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[Continue()]])],tuple([[],[]])),CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_random_11(self):
        """Break in Do While statement"""
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    Do
                        println(x);
                        i = i + 1;
                        If (i == 8) Then
                            Break;
                        EndIf.
                    While (i < 10) EndDo.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(100)),Dowhile(tuple([[],[CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If([tuple([BinaryOp("==",Id("i"),IntLiteral(8)),[],[Break()]])],tuple([[],[]]))]]),BinaryOp("<",Id("i"),IntLiteral(10)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_random_12(self):
        """Var array"""
        input = """
            Var: i=0, x;
            Var: a[5] = {1,4,3,2,0};
            Var: b[2][3]={{1,2,3},{4,5,6}};
            Function: main
                Body:
                    x = 100;
                    Do
                        println(x);
                        i = i + 1;
                        If (i == 8) Then
                            Break;
                        EndIf.
                    While (i < 10) EndDo.
                EndBody.
        """
        expect = Program([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("x"),[],None),VarDecl(Id("a"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0)])),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("x"),IntLiteral(100)),Dowhile(tuple([[],[CallStmt(Id("println"),[Id("x")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If([tuple([BinaryOp("==",Id("i"),IntLiteral(8)),[],[Break()]])],tuple([[],[]]))]]),BinaryOp("<",Id("i"),IntLiteral(10)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_random_13(self):
        """Var Boolean"""
        input = """
            Var: tmp0 = True, tmp1 = False, tmp2;
            Function: main
                Body:
                    tmp2 = tmp0;
                EndBody.
        """
        expect = Program([VarDecl(Id("tmp0"),[],BooleanLiteral(True)),VarDecl(Id("tmp1"),[],BooleanLiteral(False)),VarDecl(Id("tmp2"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("tmp2"),Id("tmp0"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_random_14(self):
        """Working with Boolean"""
        input = """
            Var: tmp0 = True, tmp1 = False, tmp2;
            Function: main
                Body:
                    tmp0 = !tmp0;
                    tmp2 = tmp0 || !tmp1;
                    tmp1 = tmp2 && !tmp2;
                EndBody.
        """
        expect = Program([VarDecl(Id("tmp0"),[],BooleanLiteral(True)),VarDecl(Id("tmp1"),[],BooleanLiteral(False)),VarDecl(Id("tmp2"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("tmp0"),UnaryOp("!",Id("tmp0"))),Assign(Id("tmp2"),BinaryOp("||",Id("tmp0"),UnaryOp("!",Id("tmp1")))),Assign(Id("tmp1"),BinaryOp("&&",Id("tmp2"),UnaryOp("!",Id("tmp2"))))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_random_15(self):
        """Working with String"""
        input = """
            Var: s;
            Function: main
                Body:
                    s = "This is a string containing tab \t";
                EndBody.
        """
        expect = Program([VarDecl(Id("s"),[],None),FuncDecl(Id("main"),[],tuple([[],[Assign(Id("s"),StringLiteral("This is a string containing tab 	"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_random_16(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Return True;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp0"),[],None),VarDecl(Id("tmp1"),[],None),VarDecl(Id("tmp2"),[12,4],None)],tuple([[],[Return(BooleanLiteral(True))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_random_17(self):
        input = """
            Function: foo
                Parameter: a , v
                Body:
                    x = a * v *(a + v);
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("v"),[],None)],tuple([[],[Assign(Id("x"),BinaryOp("*",BinaryOp("*",Id("a"),Id("v")),BinaryOp("+",Id("a"),Id("v"))))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_random_18(self):
        input = """
            Function: foo
                Parameter: a , v
                Body:
                    Return foo;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("v"),[],None)],tuple([[],[Return(Id("foo"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_random_19(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 123;
                    Return i;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp0"),[],None),VarDecl(Id("tmp1"),[],None),VarDecl(Id("tmp2"),[12,4],None)],tuple([[VarDecl(Id("i"),[],IntLiteral(123))],[Return(Id("i"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))


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
        expect = Program([FuncDecl(Id("foo"),[],tuple([[VarDecl(Id("boo"),[],None)],[Assign(Id("boo"),BinaryOp("||",UnaryOp("!",UnaryOp("!",UnaryOp("!",BooleanLiteral(True)))),BooleanLiteral(False)))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(
            10)), tuple([[], [CallStmt(Id("writeln"), [Id("i")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0)), VarDecl(Id("j"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple(
            [[], [For(Id("j"), Id("i"), BinaryOp("<", Id("j"), IntLiteral(10)), Id("i"), tuple([[], [CallStmt(Id("writeln"), [Id("j")])]])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple(
            [[VarDecl(Id("tmp"), [], BinaryOp("*", Id("i"), Id("i")))], [CallStmt(Id("writeln"), [Id("tmp")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], None)], [While(BinaryOp(">", BinaryOp("&&", BinaryOp("<", Id("i"), IntLiteral(100)), BinaryOp("%", Id("i"), IntLiteral(
            2))), IntLiteral(3)), tuple([[VarDecl(Id("tmp"), [], BinaryOp("*", Id("i"), Id("i")))], [CallStmt(Id("writeln"), [Id("tmp")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_while_04(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0, j;
                    While (i < 10) Do
                        For (j = 0, j < 10, 2) Do
                            writeln(i * j);
                        EndFor.
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0)), VarDecl(Id("j"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple(
            [[], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(2), tuple([[], [CallStmt(Id("writeln"), [BinaryOp("*", Id("i"), Id("j"))])]]))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(0)), VarDecl(Id("tmp"), [10, 10], None)], [While(BinaryOp("<=", Id("i"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(1)), [], [
                         CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[], []]))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(
            10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [CallStmt(Id("writeln"), [Id("i")])]])], tuple([[], []])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(1)), [], [CallStmt(
            Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[], []]))]])], tuple([[], []])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("j"), [], IntLiteral(0))], [CallStmt(Id("writeln"), [Id("i")]), While(BinaryOp("<", Id("j"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", BinaryOp("+", Id("i"), Id("j")), IntLiteral(2)), IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]),
                                                                                                                                                                                                                                                                                                                                                                                                                              IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[], []]))]])], tuple([[], []])), Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))]]))]]))]]))])
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
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [
                         StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[VarDecl(Id("i"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("tmp"), [], BinaryOp("*", Id("i"), Id("i")))], [CallStmt(Id("writeln"), [Id("tmp")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))]])], tuple([[], []])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

# ================Test do while statement================

    def test_do_while_00(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    Do
                        writeln(i);
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [Dowhile(tuple([[], [CallStmt(
            Id("writeln"), [Id("i")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]), BinaryOp("<", Id("i"), IntLiteral(10)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_do_while_01(self):
        input = """
            Function: foo
                Parameter: tmp0
                Body:
                    Var: i = 0;
                    Do
                        writeln(i);
                        If i == tmp0 Then Break;EndIf.
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [Dowhile(tuple([[], [CallStmt(Id("writeln"), [Id("i")]), If(
            [tuple([BinaryOp("==", Id("i"), Id("tmp0")), [], [Break()]])], tuple([[], []])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]), BinaryOp("<", Id("i"), IntLiteral(10)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_do_while_02(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i,j;
                    Do 
                        writeln(i);
                        For(j = 2 , j < 10 , 1) Do
                            tmp = tmp + j;
                        EndFor.
                    While !True EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None)], [Dowhile(tuple(
            [[], [CallStmt(Id("writeln"), [Id("i")]), For(Id("j"), IntLiteral(2), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(1), tuple([[], [Assign(Id("tmp"), BinaryOp("+", Id("tmp"), Id("j")))]]))]]), UnaryOp("!", BooleanLiteral(True)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_do_while_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Do some_thing();
                    While(!condition())
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [
                         12, 4], None)], tuple([[], [Dowhile(tuple([[], [CallStmt(Id("some_thing"), [])]]), UnaryOp("!", CallExpr(Id("condition"), [])))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_do_while_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Do
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
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[], [Dowhile(tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(
            2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[VarDecl(Id("i"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("tmp"), [], BinaryOp("*", Id("i"), Id("i")))], [CallStmt(Id("writeln"), [Id("tmp")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]))]])], tuple([[], []])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_do_while_05(self):
        input = """
            Function: foo
                Body:
                    Do
                        Var: i;
                        While (i < 10) Do
                            Var: tmp = i * i;
                            writeln(tmp);
                            i = i + 1;
                        EndWhile.
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[], [Dowhile(tuple([[VarDecl(Id("i"), [], None)], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("tmp"), [
        ], BinaryOp("*", Id("i"), Id("i")))], [CallStmt(Id("writeln"), [Id("tmp")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_do_while_06(self):
        input = """
            Function: foo
                Body:
                    Do
                        Do func();
                        While condition()
                        EndDo.
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[], [Dowhile(tuple([[], [Dowhile(tuple(
            [[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_do_while_07(self):
        input = """
            Function: foo
                Body:
                    Do
                        Do func();
                        While condition()
                        EndDo.
                        Do
                            Do func();
                            While condition()
                            EndDo.
                        While condition()
                        EndDo.
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[], [Dowhile(tuple([[], [Dowhile(tuple([[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), [])), Dowhile(
            tuple([[], [Dowhile(tuple([[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_do_while_08(self):
        input = """
            Function: foo
                Body:
                    Do
                        Do func();
                        While condition()
                        EndDo.
                        Do
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
                        While condition()
                        EndDo.
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], tuple([[], [Dowhile(tuple([[], [Dowhile(tuple([[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), [])), Dowhile(tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("j"), [], IntLiteral(0))], [CallStmt(Id("writeln"), [Id("i")]), While(BinaryOp("<", Id("j"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", BinaryOp("+", Id("i"), Id("j")), IntLiteral(2)), IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [
                         IntLiteral(10), Id("i")]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[], []]))]])], tuple([[], []])), Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))]]))]]))]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_do_while_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    Do
                        Do func();
                        While condition()
                        EndDo.
                        Do
                            Do
                                Var: i, tmp = 1;
                                For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                                    tmp = tmp * i;
                                EndFor.
                            While condition()
                            EndDo.
                        While condition()
                        EndDo.
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[], [Dowhile(tuple([[], [Dowhile(tuple([[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), [])), Dowhile(tuple([[], [Dowhile(tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("tmp"), [], IntLiteral(1))], [For(Id("i"), BinaryOp("+", Id("tmp0"), Id("tmp1")),
                                                                                                                                                                                                                                                                                                                                            BinaryOp("||", BinaryOp("<", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp1"))), BinaryOp("!=", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp0")))), ArrayCell(Id("tmp2"), [IntLiteral(4)]), tuple([[], [Assign(Id("tmp"), BinaryOp("*", Id("tmp"), Id("i")))]]))]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

# ================Test expression statement================

    def test_expression_00(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1[10]
                Body:
                    tmp0 = tmp0 + tmp1[9];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [10], None)], tuple(
            [[], [Assign(Id("tmp0"), BinaryOp("+", Id("tmp0"), ArrayCell(Id("tmp1"), [IntLiteral(9)])))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_expression_01(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    Var: tmp;
                    tmp = tmp0 + tmp1 - tmp0 * tmp1 + 1321312;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None)], tuple([[VarDecl(Id("tmp"), [], None)], [Assign(
            Id("tmp"), BinaryOp("+", BinaryOp("-", BinaryOp("+", Id("tmp0"), Id("tmp1")), BinaryOp("*", Id("tmp0"), Id("tmp1"))), IntLiteral(1321312)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_expression_02(self):
        input = """
            Function: foo
                Parameter: a, b
                Body:
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], tuple([[], [Assign(ArrayCell(Id("a"), [BinaryOp(
            "+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]), BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]), IntLiteral(4)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_expression_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    tmp0 = tmp1 && tmp0;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [
        ], None)], tuple([[], [Assign(Id("tmp0"), BinaryOp("&&", Id("tmp1"), Id("tmp0")))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_expression_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    tmp0 = tmp1 || !tmp2[2];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple(
            [[], [Assign(Id("tmp0"), BinaryOp("||", Id("tmp1"), UnaryOp("!", ArrayCell(Id("tmp2"), [IntLiteral(2)]))))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_expression_05(self):
        input = """
            Function: foo
                Parameter: tmp[200]
                Body:
                    tmp0 = tmp1 && tmp0 || (True && True) || (False && False && (tmp[1]&&tmp[2])) ;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp"),[200],None)],tuple([[],[Assign(Id("tmp0"),BinaryOp("||",BinaryOp("||",BinaryOp("&&",Id("tmp1"),Id("tmp0")),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True))),BinaryOp("&&",BinaryOp("&&",BooleanLiteral(False),BooleanLiteral(False)),BinaryOp("&&",ArrayCell(Id("tmp"),[IntLiteral(1)]),ArrayCell(Id("tmp"),[IntLiteral(2)])))))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_expression_06(self):
        input = """
            Function: foo
                Parameter: tmp
                Body:
                    Var: i           = tmp;
                    Var: tmp0 = tmp1 && tmp0 || (True && True) || (False && False && (tmp[1]&&tmp[2])) ;
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("tmp"),[],None)],tuple([[VarDecl(Id("i"),[],Id("tmp")),VarDecl(Id("tmp0"),[],BinaryOp("||",BinaryOp("||",BinaryOp("&&",Id("tmp1"),Id("tmp0")),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True))),BinaryOp("&&",BinaryOp("&&",BooleanLiteral(False),BooleanLiteral(False)),BinaryOp("&&",ArrayCell(Id("tmp"),[IntLiteral(1)]),ArrayCell(Id("tmp"),[IntLiteral(2)])))))],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_expression_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i = True;
                    i = (((i < tmp0 * tmp1) || (i != tmp0 * tmp0)) && (i !=tmp2[4]));
                    Return i;
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [10], None)], tuple([[VarDecl(Id("i"), [], BooleanLiteral(True))], [Assign(Id("i"), BinaryOp("&&", BinaryOp(
            "||", BinaryOp("<", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp1"))), BinaryOp("!=", Id("i"), BinaryOp("*", Id("tmp0"), Id("tmp0")))), BinaryOp("!=", Id("i"), ArrayCell(Id("tmp2"), [IntLiteral(4)])))), Return(Id("i"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_expression_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i;
                    tmp0 = tmp2[0] * tmp1 + tmp2[1];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple(
            [[VarDecl(Id("i"), [], None)], [Assign(Id("tmp0"), BinaryOp("+", BinaryOp("*", ArrayCell(Id("tmp2"), [IntLiteral(0)]), Id("tmp1")), ArrayCell(Id("tmp2"), [IntLiteral(1)])))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_expression_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: tmp_0, tmp_1, tmp_2;
                    tmp_0 = tmp0;
                    tmp_1 = !(tmp1+tmp2[tmp0][tmp_0 * 3]);
                    tmp_2 = tmp_1 + tmp_0 * tmp2[tmp1][tmp0];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("tmp_0"), [], None), VarDecl(Id("tmp_1"), [], None), VarDecl(Id("tmp_2"), [], None)], [Assign(Id("tmp_0"), Id("tmp0")), Assign(
            Id("tmp_1"), UnaryOp("!", BinaryOp("+", Id("tmp1"), ArrayCell(Id("tmp2"), [Id("tmp0"), BinaryOp("*", Id("tmp_0"), IntLiteral(3))])))), Assign(Id("tmp_2"), BinaryOp("+", Id("tmp_1"), BinaryOp("*", Id("tmp_0"), ArrayCell(Id("tmp2"), [Id("tmp1"), Id("tmp0")]))))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

# ================Test completed program================

    def test_program_00(self):
        input = """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], tuple([[], [If([tuple([BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]])], tuple(
            [[], [Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]]))]])), FuncDecl(Id("main"), [], tuple([[], [Assign(Id("x"), IntLiteral(10)), CallStmt(Id("fact"), [Id("x")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_program_01(self):
        input = """
            Function: square
                Parameter: n
                Body:
                    Return n * n;
                EndBody.
            Function: main
                Body:
                    writeln(square(3));
                EndBody.
        """
        expect = Program([FuncDecl(Id("square"), [VarDecl(Id("n"), [], None)], tuple([[], [Return(BinaryOp("*", Id("n"), Id("n")))]])),
                          FuncDecl(Id("main"), [], tuple([[], [CallStmt(Id("writeln"), [CallExpr(Id("square"), [IntLiteral(3)])])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_program_02(self):
        input = """
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else Return n * fact(n-1); 
                    EndIf.                   
                EndBody.
            ** This is a single-line comment. **
            ** This is a
            * multi-line
            * comment.
            **
            Function: main
                Body:
                    Var: fact_4;
                    fact_4 = fact(4);
                    printLn(a);
                EndBody.
        """
        expect = Program([FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], tuple([[], [If([tuple([BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]])], tuple([[], [Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"),
                                                                                                                                                                                                                               [BinaryOp("-", Id("n"), IntLiteral(1))])))]]))]])), FuncDecl(Id("main"), [], tuple([[VarDecl(Id("fact_4"), [], None)], [Assign(Id("fact_4"), CallExpr(Id("fact"), [IntLiteral(4)])), CallStmt(Id("printLn"), [Id("a")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_program_03(self):
        input = """
            Function: sum
                Parameter: n
                Body:
                    Var: i , sum = 0;
                    For(i = 1 , i <= n , 1) Do
                        sum = sum + i;
                    EndFor.
                    Return sum;
                EndBody.
        """
        expect = Program([FuncDecl(Id("sum"), [VarDecl(Id("n"), [], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("sum"), [], IntLiteral(0))], [For(
            Id("i"), IntLiteral(1), BinaryOp("<=", Id("i"), Id("n")), IntLiteral(1), tuple([[], [Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))]])), Return(Id("sum"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_program_04(self):
        input = """
            Function: result
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 1, result;
                    While i <= n Do
                        result = result * i;
                        i = i + 1;
                    EndWhile.
                    Return result;
                EndBody.
        """
        expect = Program([FuncDecl(Id("result"), [VarDecl(Id("tmp0"), [], None), VarDecl(Id("tmp1"), [], None), VarDecl(Id("tmp2"), [12, 4], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(1)), VarDecl(Id("result"), [], None)], [
                         While(BinaryOp("<=", Id("i"), Id("n")), tuple([[], [Assign(Id("result"), BinaryOp("*", Id("result"), Id("i"))), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]])), Return(Id("result"))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_program_05(self):
        input = """
            Function: foo
                Parameter: a 
                Body:
                    Var: i;
                    Return a*i;
                EndBody.
            Function: main
                Body:
                    Var: a = foo(z);
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None)], tuple([[VarDecl(Id("i"), [], None)], [Return(BinaryOp(
            "*", Id("a"), Id("i")))]])), FuncDecl(Id("main"), [], tuple([[VarDecl(Id("a"), [], CallExpr(Id("foo"), [Id("z")]))], []]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_program_06(self):
        input = """
            Function: foo
                Parameter: a[5] , n
                Body:
                    Var: i, sum = 0;
                    For(i = 0 , i <= n, 1) Do
                        sum = sum + a[i];
                    EndFor.
                    Return sum;
                EndBody.
            Function: main
                Body:
                    Var: a = 10;
                    xx = foo(a);
                    printLn(xx);
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(Id("n"), [], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("sum"), [], IntLiteral(0))], [For(Id("i"), IntLiteral(0), BinaryOp("<=", Id("i"), Id("n")), IntLiteral(1), tuple(
            [[], [Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("a"), [Id("i")])))]])), Return(Id("sum"))]])), FuncDecl(Id("main"), [], tuple([[VarDecl(Id("a"), [], IntLiteral(10))], [Assign(Id("xx"), CallExpr(Id("foo"), [Id("a")])), CallStmt(Id("printLn"), [Id("xx")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_program_07(self):
        input = """
            Function: double
                Parameter: tmp
                Body:
                    Var: i = 2;
                    Return tmp * i;
                EndBody.
            Function: main
                Body:
                    Return double(12000);
                EndBody.
        """
        expect = Program([FuncDecl(Id("double"), [VarDecl(Id("tmp"), [], None)], tuple([[VarDecl(Id("i"), [], IntLiteral(2))], [Return(
            BinaryOp("*", Id("tmp"), Id("i")))]])), FuncDecl(Id("main"), [], tuple([[], [Return(CallExpr(Id("double"), [IntLiteral(12000)]))]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_program_08(self):
        input = """
            Function: foo
                Parameter: a[5] , n
                Body:
                    Var: i, result = 0;
                    For(i = 0, i < n , 1) Do
                        If(a[i] % 2 == 0) Then 
                            result = result + a[i];
                        EndIf.
                    EndFor.
                EndBody.
            Function: foo1
                Body:
                    Do
                        Do func();
                        While condition()
                        EndDo.
                        Do
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
                        While condition()
                        EndDo.
                    While condition()
                    EndDo.
                EndBody.
            Function: main
                Body:
                    Var: a[5] = {1,2,3,4,5} , result;
                    result = foo(a[5]);
                    printLn(x);
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(Id("n"), [], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("result"), [], IntLiteral(0))], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), tuple([[], [If([tuple([BinaryOp("==", BinaryOp("%", ArrayCell(Id("a"), [Id("i")]), IntLiteral(2)), IntLiteral(0)), [], [Assign(Id("result"), BinaryOp("+", Id("result"), ArrayCell(Id("a"), [Id("i")])))]])], tuple([[], []]))]]))]])), FuncDecl(Id("foo1"), [], tuple([[], [Dowhile(tuple([[], [Dowhile(tuple([[], [CallStmt(Id("func"), [])]]), CallExpr(Id("condition"), [])), Dowhile(tuple([[VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<", Id("i"), IntLiteral(10)), tuple([[VarDecl(Id("j"), [], IntLiteral(0))], [CallStmt(Id("writeln"), [Id("i")]), While(BinaryOp("<", Id("j"), IntLiteral(10)), tuple([[], [If([tuple([BinaryOp("!=", BinaryOp("%", BinaryOp("+", Id("i"), Id("j")), IntLiteral(2)),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             IntLiteral(0)), [], [If([tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(1)), [], [CallStmt(Id("println"), [StringLiteral("1")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(2)), [], [CallStmt(Id("println"), [StringLiteral("2")])]]), tuple([BinaryOp("==", ArrayCell(Id("tmp2"), [IntLiteral(10), Id("i")]), IntLiteral(3)), [], [CallStmt(Id("println"), [StringLiteral("3")])]])], tuple([[], []]))]])], tuple([[], []])), Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))]]))]]))]]), CallExpr(Id("condition"), []))]]), CallExpr(Id("condition"), []))]])), FuncDecl(Id("main"), [], tuple([[VarDecl(Id("a"), [5], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("result"), [], None)], [Assign(Id("result"), CallExpr(Id("foo"), [ArrayCell(Id("a"), [IntLiteral(5)])])), CallStmt(Id("printLn"), [Id("x")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_program_09(self):
        input = """
            Function: foo
                Parameter: a[5] , n
                Body:
                    Var: i, result = 0;
                    For(i = 0, i < n , 1) Do
                        If(a[i] % 2 == 0) Then 
                            result = result + a[i];
                        EndIf.
                    EndFor.
                EndBody.
            Function: main
                Body:
                    Var: a[5] = {1,2,3,4,5} , result;
                    result = foo(a[5]);
                    printLn(x);
                EndBody.          
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(Id("n"), [], None)], tuple([[VarDecl(Id("i"), [], None), VarDecl(Id("result"), [], IntLiteral(0))], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), tuple([[], [If([tuple([BinaryOp("==", BinaryOp("%", ArrayCell(Id("a"), [Id("i")]), IntLiteral(2)), IntLiteral(0)), [], [Assign(Id("result"), BinaryOp(
            "+", Id("result"), ArrayCell(Id("a"), [Id("i")])))]])], tuple([[], []]))]]))]])), FuncDecl(Id("main"), [], tuple([[VarDecl(Id("a"), [5], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("result"), [], None)], [Assign(Id("result"), CallExpr(Id("foo"), [ArrayCell(Id("a"), [IntLiteral(5)])])), CallStmt(Id("printLn"), [Id("x")])]]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
