import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_00(self):
        """Name"""
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 0))

    def test_01(self):
        input = """ Var: x;
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 1))

    def test_02(self):
        """If statement"""
        input = """ Function: main
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return 2;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2))

    def test_03(self):
        """For statement"""
        input = """ Function: main
                        Body:
                            For (i = 0, i < 10, 2) Do
                                println(i);
                            EndFor.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 3))

    def test_04(self):
        """While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            While (i < 10) Do
                                println(x);
                                i = i + 1;
                            EndWhile.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 4))

    def test_05(self):
        """Do While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            Do 
                                println(x);
                                i = i + 1;
                            While (i < 10) EndDo.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 5))

    def test_06(self):
        """Continue statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            While (i < 10) Do
                                println(x);
                                i = i + 1;
                                Continue;
                            EndWhile.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 6))

    def test_07(self):
        """For and If statement"""
        input = """ Function: main
                        Body:
                            For (i = 0, i < 10, 2) Do
                                If (i % 2 == 0) Then
                                    println("Chan");
                                ElseIf (i % 2 != 0) Then
                                    println("Le");
                                EndIf.
                            EndFor.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 7))

    def test_08(self):
        """COntinue in While statement"""
        input = """ Var: i=0, x;
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 8))

    def test_09(self):
        """Break in Do While statement"""
        input = """ Var: i=0, x;
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 9))

    def test_10(self):
        """Var array"""
        input = """ Var: i=0, x;
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 10))

    def test_11(self):
        """Var Boolean"""
        input = """ Var: tmp0 = True, tmp1 = False, tmp2;
                    Function: main
                        Body:
                            tmp2 = tmp0;
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 11))

    def test_12(self):
        """Working with Boolean"""
        input = """ Var: tmp0 = True, tmp1 = False, tmp2;
                    Function: main
                        Body:
                            tmp0 = !tmp0;
                            tmp2 = tmp0 || !tmp1;
                            tmp1 = tmp2 && !tmp2;
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 12))

    def test_13(self):
        """Working with String"""
        input = """ Var: s;
                    Function: main
                        Body:
                            s = "This is a string containing tab \t";
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 13))

    def test_14(self):
        """Working with String"""
        input = """ Var: s;
                    Function: main
                        Body:
                            s = "This is a string containing tab \t";
                            s = ”He asked me: ’”Where is John?’””;
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 14))