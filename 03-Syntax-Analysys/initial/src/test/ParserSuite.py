import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """
        int a,b,c;
        float foo (int a;) {
            int e;
            e = a+ 4;
            c = a * d  / 2.0;
            return c + 1;
        }
        float goo(float a,b) {
            return foo(1,a,b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input, expect, 202))
