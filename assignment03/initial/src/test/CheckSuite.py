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

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 405))

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

    def test_check_undeclared_02(self):
        input = """ Var: x, y, z;
                    Function: main
                    Body:
                        x = 0;
                        tmp = x;
                    EndBody."""
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_lorem_00(self):
        input = """ Var: x, y, z;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_lorem_01(self):
        input = """ Var: x, y, z, main;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_lorem_02(self):
        input = """ Var: x, y, z;
                    Function: foo
                    Parameter: main
                    Body:
                    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_lorem_03(self):
        input = """ Var: x, y, z;
                    Function: mAIn
                    Parameter: param
                    Body:
                    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclared_variable_00(self):
        input = """
            Var:x;
            Function: main
                Body:
                    Var: x, y;
                    Var: y;
                EndBody.
        """
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_redeclared_variable_01(self):
        input = """
            Var:x = 0;
            Var: x = "hello";
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_redeclared_variable_02(self):
        input = """
            Var: a,b,c,d,e,f;
            Var: tmp = 0;
            Function: main
                Body:
                    Var:x = 0;
                    Var: x = "hello";
                EndBody.
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_redeclared_variable_03(self):
        input = """
            Var: a,b,c,d,e,f;
            Var: tmp = 0;
            Function: main
                Body:
                EndBody.
            Function: foo
                Body:
                    Var:x = 0;
                    Var: x = "hello";
                EndBody.
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_redeclared_variable_04(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        Var: tmp;
                        Var: tmp;
                    EndFor.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_redeclared_variable_05(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    Do
                        Var: tmp;
                        Var: tmp;
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_redeclared_variable_06(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    While i < 10 Do
                        Var: tmp;
                        Var: tmp;
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_redeclared_variable_07(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then
                        Var: tmp;
                        Var: tmp;
                        tmp1 = 2;
                    ElseIf tmp0 == 2 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_redeclared_variable_08(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        Var: tmp;
                        Var: tmp;
                        tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_redeclared_variable_09(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        tmp1 = 3;
                    Else 
                        Var: tmp;
                        Var: tmp;
                        tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Redeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_undeclared_variable_00(self):
        input = """
            Var:x;
            Function: main
                Body:
                    y = 0;
                EndBody.
        """
        expect = str(Undeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_undeclared_variable_01(self):
        input = """
            Var:x = 0;
            Function: main
                Body:
                    Var: y = 0;
                    y = tmp;
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_undeclared_variable_02(self):
        input = """
            Function: main
                Body:
                    Var: tmp = 0;
                EndBody.
            Function: foo
                Body:
                    tmp = 1;
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_undeclared_variable_03(self):
        input = """
            Function: main
                Body:
                    Var: tmp = 0;
                EndBody.
            Function: foo
                Parameter: param
                Body:
                    param = tmp;
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_undeclared_variable_04(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        tmp = i;
                    EndFor.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_undeclared_variable_05(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    Do
                        tmp = tmp + 1;
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_undeclared_variable_06(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    While i < 10 Do
                        tmp = tmp + 1;
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_undeclared_variable_07(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    tmp0 = 1;
                    tmp1 = 1;
                    If tmp0 == 1 Then
                        tmp = tmp + 1;
                        tmp1 = 2;
                    ElseIf tmp0 == 2 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_undeclared_variable_08(self):
        input = """
            Var: tmp0, tmp1;
            Function: main
                Body:
                    tmp0 = 1;
                    tmp1 = 1;
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        tmp = tmp + 1;
                        tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_undeclared_variable_09(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    tmp0 = 0;
                    tmp1 = 2;
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        tmp1 = 3;
                    Else 
                        tmp = tmp + 1;
                        tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Variable(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_undeclared_function_00(self):
        input = """
            Var:x;
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_undeclared_function_01(self):
        input = """
            Var:x = 0;
            Function: foo
                Body:
                    tmp();
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_undeclared_function_02(self):
        input = """
            Var:x = 0;
            Function: foo0
                Body:
                EndBody.
            Function: foo1
                Body:
                    foo0();
                    tmp(param);
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_undeclared_function_03(self):
        input = """
            Var:x = 0;
            Function: foo0
                Parameter: param
                Body:
                EndBody.
            Function: foo1
                Body:
                    foo0();
                    tmp(param);
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_undeclared_function_04(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        i = tmp();
                    EndFor.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_undeclared_function_05(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    Do
                        Var: x = tmp();
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_undeclared_function_06(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    While i < 10 Do
                        Var: x = tmp();
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_undeclared_function_07(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then
                        Var: x = tmp();
                        tmp1 = 2;
                    ElseIf tmp0 == 2 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_undeclared_function_08(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        Var: x = tmp();
                        tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_undeclared_function_09(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then
                        tmp1 = 3;
                    Else 
                        Var: x = tmp();
                        tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(Undeclared(Function(), "tmp"))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_type_mismatch_in_statement_00(self):
        input = """
            Var:x;
            Function: foo
                Body:
                EndBody.
            Function: main
                Body:
                    foo(1);
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id("foo"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_type_mismatch_in_statement_01(self):
        input = """
            Var:x = 0;
            Function: foo0
                Body:
                EndBody.
            Function: foo1
                Body:
                    foo0(1, 2);
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id("foo0"), [IntLiteral(1), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_type_mismatch_in_statement_02(self):
        input = """
            Var:x = 0;
            Function: foo0
                Body:
                EndBody.
            Function: foo1
                Body:
                    foo0(2.1);
                EndBody.
            Function: main
                Body:
                    foo0();
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id("foo0"), [FloatLiteral(2.1)])))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_type_mismatch_in_statement_03(self):
        input = """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == 0.2 Then
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_type_mismatch_in_statement_04(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0.3, i < 10, 2) Do
                    EndFor.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("i"), FloatLiteral(
            0.3), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), tuple([[], []]))))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_mismatch_in_statement_05(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    Var: tmp;
                    tmp = 100;
                    Do
                        i = i + 1;
                    While tmp EndDo.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Dowhile(
                tuple([[], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]), Id("tmp"))
        ))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_mismatch_in_statement_06(self):
        input = """
            Function: main
                Body:
                    Var: i = 0;
                    Var: tmp;
                    tmp = 100;
                    While tmp Do
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            While(Id("tmp"), tuple(
                [[], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]]))
        ))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_type_mismatch_in_statement_07(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    Var: tmp;
                    tmp = 100;
                    If tmp Then tmp1 = 2;
                    ElseIf tmp0 == 2 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            If([tuple([Id("tmp"), [], [Assign(
                Id("tmp1"), IntLiteral(2))]]), tuple([BinaryOp("==", Id("tmp0"), IntLiteral(2)), [], [Assign(Id("tmp1"), IntLiteral(3))]])], tuple([[], [Assign(Id("tmp1"), IntLiteral(100))]]))
        ))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_type_mismatch_in_statement_08(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    Var: tmp;
                    tmp = 100;
                    If tmp0 == 1 Then tmp1 = 2;
                    ElseIf tmp Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(
            If([tuple([BinaryOp("==", Id("tmp0"), IntLiteral(1)), [], [Assign(
                Id("tmp1"), IntLiteral(2))]]), tuple([Id("tmp"), [], [Assign(Id("tmp1"), IntLiteral(3))]])], tuple([[], [Assign(Id("tmp1"), IntLiteral(100))]]))
        ))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_type_mismatch_in_statement_09(self):
        input = """
            Var: x;
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    Return "Hello";
                EndBody.
            Function: main
                Body:
                    foo(x);
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mismatch_in_expression_00(self):
        input = """
            Function: main
                Body:
                    bool_of_string(4.5);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("bool_of_string"), [FloatLiteral(4.5)])
        ))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_type_mismatch_in_expression_01(self):
        input = """
            Function: main
                Body:
                    string_of_bool(4.5);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("string_of_bool"), [FloatLiteral(4.5)])
        ))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_type_mismatch_in_expression_02(self):
        input = """
            Function: main
                Body:
                    string_of_bool(2.1);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("string_of_bool"), [FloatLiteral(2.1)])))
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_type_mismatch_in_expression_03(self):
        input = """
            Function: main
                Body:
                    printStr(4);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("printStr"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_type_mismatch_in_expression_04(self):
        input = """
            Function: main
                Body:
                    int_of_string(4);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("int_of_string"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_type_mismatch_in_expression_05(self):
        input = """
            Function: main
                Body:
                    float_of_int(4.5);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("float_of_int"), [FloatLiteral(4.5)])))
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_type_mismatch_in_expression_06(self):
        input = """
            Function: main
                Body:
                    int_of_float(400);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("int_of_float"), [IntLiteral(400)])))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_type_mismatch_in_expression_07(self):
        input = """
            Function: main
                Body:
                    printStrLn(400);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("printStrLn"), [IntLiteral(400)])))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_type_mismatch_in_expression_08(self):
        input = """
            Function: main
                Parameter: tmp0, tmp1
                Body:
                    Var: tmp;
                    tmp = 100;
                    If tmp0 == 1 Then
                        tmp1 = 2;
                        printStrLn(400);
                    ElseIf tmp == 100 Then tmp1 = 3;
                    Else tmp1 = 100;
                    EndIf.
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("printStrLn"), [IntLiteral(400)])))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_type_mismatch_in_expression_09(self):
        input = """
            Function: foo
                Body:
                    printStrLn(400);
                    Return "Hello";
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(TypeMismatchInExpression(
            CallStmt(Id("printStrLn"), [IntLiteral(400)])))
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_random_00(self):
        input = """
            Var:x;
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_random_01(self):
        input = """
            Var:x;
            Function: main
                Parameter: param
                Body:
                    y = x;
                EndBody.
        """
        expect = str(Undeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_random_02(self):
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
                    x = 10.1;
                    fact (x);
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_random_03(self):
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
        expect = str(Undeclared(Variable(), "n"))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_random_04(self):
        input = """
            Var: x;
            Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    x = (0 + 199) * i;
                    println(x);
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Function(), "println"))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_random_05(self):
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    While (i < 10) Do
                        printLn(x);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_random_06(self):
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    Var: x = "This is a string", y = "";
                    Var: z = **comment** "This \\n is \\t a '" string '"";
                    Do
                        int_of_string(100);
                        i = i + 1;
                    While (i < 10) EndDo.
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallStmt(Id("int_of_string"),[IntLiteral(100)])))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_random_07(self):
        input = """
            Var: i=0, x;
            Function: main
                Body:
                    x = 100;
                    While (i < 10) Do
                        read(string_of_int(x));
                        i = i + 1;
                        Continue;
                    EndWhile.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("read"),[CallExpr(Id("string_of_int"),[Id("x")])])))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_random_08(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0.2, i + 10, 2) Do
                        If (i - 2 == 0) Then
                            printStrLn("Chan");
                        ElseIf (i - 2 != 0) Then
                            printLn("Le");
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[StringLiteral("Le")])))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_random_09(self):
        input = """
            Function: main
                Body:
                    Var: i;
                    For (i = 0, i + 10, 2) Do
                        If (i - 2 == 0) Then
                            printStrLn("Chan");
                        ElseIf (i - 2 != 0) Then
                            printStrLn(i);
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallStmt(Id("printStrLn"),[Id("i")])))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_random_10(self):
        input = """
            Var: x;
            Function: main
                Body:
                    x = !3;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp("!",IntLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_random_11(self):
        input = """
            Var: i, x;
            Function: main
                Body:
                    While (i < 10) Do
                        If (i - 2 == 0) Then
                            Continue;
                        EndIf.
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("<",Id("i"),IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_random_12(self):
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
        expect = str(Undeclared(Function(), "println"))
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_random_13(self):
        input = """
            Var: x;
            Function: main
                Body:
                    x = 3 + True;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(3),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_random_14(self):
        input = """
            Var: x, y;
            Function: main
                Body:
                    x = y;
                EndBody.
        """
        expect = str(TypeCannotBeInferred( Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_random_15(self):
        input = """
            Var: x, y, z;
            Function: main
                Body:
                    x = False *. 4.2;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("*.",BooleanLiteral("false"),FloatLiteral(4.2))))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_random_16(self):
        input = """
            Var: x, y, z;
            Function: foo
                Body:
                    x = 0;
                    x = x + 1;
                EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_random_17(self):
        input = """
            Var: i=0, x;
            Var: a[5] = {1,4,3,2,0};
            Var: b[2][3]={{1,2,3},{4,5,6}};
            Function: main
                Body:
                    x = 100;
                    Do
                        print(x);
                        i = i + 1;
                        If (i == 8) Then
                            Break;
                        EndIf.
                    While (i < 10) EndDo.
                EndBody.
        """
        expect = str(Undeclared(Function(), "print"))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_random_18(self):
        input = """

        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_random_19(self):
        input = """
            Var: tmp0 = 1, tmp1 = False, tmp2;
            Function: main
                Body:
                    tmp2 = tmp0 + True;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("tmp0"),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_random_20(self):
        input = """
            Var: s;
            Function: main
                Body:
                    s = "This is a string containing tab \t";
                    s = 2;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(Assign(Id("s"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_random_21(self):
        input = """
            Var: tmp0 = 2, tmp1 = False, tmp2;
            Function: main
                Body:
                    tmp0 = !tmp0;
                    tmp2 = tmp1 && !tmp1;
                EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp("!",Id("tmp0"))))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_random_22(self):
        input = """
            Var: tmp0 = 2, tmp1 = False, tmp2;
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    tmp0 = False;
                    Return True;
                EndBody.
            Function: main
                Body:
                    foo(tmp0, tmp1);
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("tmp0"),Id("tmp1")])))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_random_23(self):
        input = """
            Var: x;
            Function: foo
                Parameter: a , v
                Body:
                    a = 100;
                    v = False;
                    x = a * v;
                EndBody.
            Function: main
                Body:
                    foo(tmp0, tmp1);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("*",Id("a"),Id("v"))))
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_random_24(self):
        input = """
            Function: foo
                Parameter: a , v
                Body:
                    a = 100;
                    v = False;
                    Return True;
                EndBody.
            Function: main
                Body:
                    foo(False, True);
                EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[BooleanLiteral("false"),BooleanLiteral("true")])))
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_random_25(self):
        input = """
            Var: x;
            Function: foo
                Body:
                    Return i;
                EndBody.
            Function: main
                Body:
                    foo();
                EndBody.
        """
        expect = str(Undeclared(Variable(), "i"))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_random_26(self):
        input = """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == True Then
                        Return 1;
                    Else
                        Return 0;
                    EndIf.
                EndBody.
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("n"),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_random_27(self):
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
        expect = str(Undeclared(Function(), "writeln"))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_random_28(self):
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
                    printLn(True);
                EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("n"),IntLiteral(0))))
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_random_29(self):
        input = """
            Function: foo
                Parameter: a 
                Body:
                    Var: i;
                    Return a*i;
                EndBody.
            Function: main
                Body:
                    Var: a = foo();
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_tmp_00(self):
    #     input = """

    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 4))
