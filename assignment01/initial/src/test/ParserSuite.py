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

    def test_01(self):
        input = """ Var: x;
                    Function: fact
                        Parameter: n
                        Body:
                            **If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.**
                        EndBody.

                    Function: main
                        Body:
                            x = 10;
                            fact (x);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 1))

    # def test_02(self):
    #     """If statement"""
    #     input = """If n == 0 Then Return 1; Else Return 2; EndIf."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 2))

    def test_03(self):
        """If statement"""
        input = """If Then EndIf."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 3))
