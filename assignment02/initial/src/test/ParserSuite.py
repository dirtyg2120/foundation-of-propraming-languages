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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))
