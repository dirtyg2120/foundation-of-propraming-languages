import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "abc def  """, """Unclosed String: abc def  """, 106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a1pFUO1JHb", "a1pFUO1JHb,<EOF>", 1))

    def test_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            "q7q@930AYp_", "q7q,Error Token @", 2))

    def test_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            "I8wN8dn8WW_", "Error Token I", 3))

    def test_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            "xtj_RD221UOk44Db_", "xtj_RD221UOk44Db_,<EOF>", 4))

    def test_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            "MiFeX5cLSW", "Error Token M", 5))

    def test_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ficaIyMewRJuIjCp", "ficaIyMewRJuIjCp,<EOF>", 6))

    def test_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            "dNsF_KZX_zCD", "dNsF_KZX_zCD,<EOF>", 7))

    def test_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Lgu0LLj9em", "Error Token L", 8))

    def test_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            "t4hcOkB___jUrt5p2WP", "t4hcOkB___jUrt5p2WP,<EOF>", 9))

    def test_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "_dfFJzx9wf8OzkMQ", "Error Token _", 10))

    def test_11(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 11))

    def test_12(self):
        self.assertTrue(TestLexer.checkLexeme("199", "199,<EOF>", 12))

    def test_13(self):
        self.assertTrue(TestLexer.checkLexeme("0xEF", "0xEF,<EOF>", 13))

    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC", "0XABC,<EOF>", 14))

    def test_15(self):
        self.assertTrue(TestLexer.checkLexeme("0o567", "0o567,<EOF>", 15))

    def test_16(self):
        self.assertTrue(TestLexer.checkLexeme("0O77", "0O77,<EOF>", 16))

    # def test_17(self):
    #     self.assertTrue(TestLexer.checkLexeme("23872394087a123", "23872394087,Error Token a", 17))

    def test_18(self):
        self.assertTrue(TestLexer.checkLexeme(
            "28913798#fads", "28913798,Error Token #", 18))

    # def test_19(self):
    #     self.assertTrue(TestLexer.checkLexeme("012912", "0,Error Token 1", 19))

    def test_20(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xDDG", "0xDD,Error Token G", 20))

    def test_21(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0X101$DEF", "0X101,Error Token $", 21))

    def test_22(self):
        self.assertTrue(TestLexer.checkLexeme("0P123", "0,Error Token P", 22))

    def test_23(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3", "12.0e3,<EOF>", 23))

    def test_24(self):
        self.assertTrue(TestLexer.checkLexeme("12e3", "12e3,<EOF>", 24))

    def test_25(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5", "12.e5,<EOF>", 25))

    def test_26(self):
        self.assertTrue(TestLexer.checkLexeme("12.0E3", "12.0E3,<EOF>", 26))

    def test_27(self):
        self.assertTrue(TestLexer.checkLexeme("12000.", "12000.,<EOF>", 27))

    def test_28(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12000e-1", "12000e-1,<EOF>", 28))

    # def test_29(self):

    #     self.assertTrue(TestLexer.checkLexeme(
    #         "12..0202", "12.,Error Token .", 29))

    # def test_30(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         "12.0eE3", "12.0e,Error Token E", 30))

    # def test_31(self):
    #     self.assertTrue(TestLexer.checkLexeme(".0101", ",Error Token .", 31))

    # def test_32(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         "12.02e&1", "12.02e,Error Token &", 32))

    # def test_33(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         "12.a5", "12.,Error Token a", 33))

    def test_34(self):
        self.assertTrue(TestLexer.checkLexeme("** comment **", "<EOF>", 34))

    # def test_35(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 35))

    # def test_36(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 36))

    # def test_37(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 37))

    # def test_38(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 38))

    # def test_39(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 39))

    # def test_40(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 40))

    # def test_41(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 41))

    # def test_42(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 42))

    # def test_43(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 43))

    # def test_44(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 44))

    # def test_45(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 45))

    # def test_46(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 46))

    # def test_47(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 47))

    # def test_48(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 48))

    # def test_49(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 49))

    # def test_50(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 50))

    # def test_51(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 51))

    # def test_52(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 52))

    # def test_53(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 53))

    # def test_54(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 54))

    # def test_55(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 55))

    # def test_56(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 56))

    # def test_57(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 57))

    # def test_58(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 58))

    # def test_59(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 59))

    # def test_60(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 60))

    # def test_61(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 61))

    # def test_62(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 62))

    # def test_63(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 63))

    # def test_64(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 64))

    # def test_65(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 65))

    # def test_66(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 66))

    # def test_67(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 67))

    # def test_68(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 68))

    # def test_69(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 69))

    # def test_70(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 70))

    # def test_71(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 71))

    # def test_72(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 72))

    # def test_73(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 73))

    # def test_74(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 74))

    # def test_75(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 75))

    # def test_76(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 76))

    # def test_77(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 77))

    # def test_78(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 78))

    # def test_79(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 79))

    # def test_80(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 80))

    # def test_81(self):

    #     self.assertTrue(TestLexer.checkLexeme("", "", 81))

    # def test_82(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 82))

    # def test_83(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 83))

    # def test_84(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 84))

    # def test_85(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 85))

    # def test_86(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 86))

    # def test_87(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 87))

    # def test_88(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 88))

    # def test_89(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 89))

    # def test_90(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 90))

    # def test_91(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 91))

    # def test_92(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 92))

    # def test_93(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 93))

    # def test_94(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 94))

    # def test_95(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 95))

    # def test_96(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 96))

    # def test_97(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 97))

    # def test_98(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 98))

    # def test_99(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 99))

    # def test_100(self):
    #     self.assertTrue(TestLexer.checkLexeme("", "", 40))
