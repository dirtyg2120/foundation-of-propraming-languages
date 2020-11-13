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

    def test_tmp(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))
