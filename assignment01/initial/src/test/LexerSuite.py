import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
# ================Test Random================
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 100))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 101))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 102))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 103))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 104))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 105))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 106))

    def test_string_with_quotes_1(self):
        """test_string_with_quotes"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\' def: 'abc\'" """, """Illegal Escape In String: abc\' """, 107))

    def test_string_with_quotes_2(self):
        """test_string_with_quotes"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abcdf\' def: 'abc\\'" """, """Illegal Escape In String: abcdf\' """, 108))

    def test_unterminated_comment(self):
        """test_string_with_quotes"""
        self.assertTrue(TestLexer.checkLexeme("""a * b""", "a,*,b,<EOF>", 109))

# ================Test Identifier================
    def test_identifier_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a1pFUO1JHb", "a1pFUO1JHb,<EOF>", 110))

    def test_identifier_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            "q7q@930AYp_", "q7q,Error Token @", 111))

    def test_identifier_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            "I8wN8dn8WW_", "Error Token I", 112))

    def test_identifier_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            "xtj_RD221UOk44Db_", "xtj_RD221UOk44Db_,<EOF>", 113))

    def test_identifier_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            "MiFeX5cLSW", "Error Token M", 114))

    def test_identifier_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ficaIyMewRJuIjCp", "ficaIyMewRJuIjCp,<EOF>", 115))

    def test_identifier_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            "dNsF_KZX_zCD", "dNsF_KZX_zCD,<EOF>", 116))

    def test_identifier_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Lgu0LLj9em", "Error Token L", 117))

    def test_identifier_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            "t4hcOkB___jUrt5p2WP", "t4hcOkB___jUrt5p2WP,<EOF>", 118))

    def test_identifier_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            "_dfFJzx9wf8OzkMQ", "Error Token _", 119))

# ================Test Integer================

    def test_integer_00(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 120))

    def test_integer_01(self):
        self.assertTrue(TestLexer.checkLexeme("199", "199,<EOF>", 121))

    def test_integer_02(self):
        self.assertTrue(TestLexer.checkLexeme("0xEF", "0xEF,<EOF>", 122))

    def test_integer_03(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC", "0XABC,<EOF>", 123))

    def test_integer_04(self):
        self.assertTrue(TestLexer.checkLexeme("0o567", "0o567,<EOF>", 124))

    def test_integer_05(self):
        self.assertTrue(TestLexer.checkLexeme("0O77", "0O77,<EOF>", 125))

    def test_integer_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            "23872394087", "23872394087,<EOF>", 126))

    def test_integer_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            "28913798#fads", "28913798,Error Token #", 127))

    def test_integer_08(self):
        self.assertTrue(TestLexer.checkLexeme("0O21", "0O21,<EOF>", 128))

    def test_integer_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xDDG", "0xDD,Error Token G", 129))

# ================Test Float================

    def test_float_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            ".123", ".,123,<EOF>", 130))

    def test_float_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0X101$DEF", "0X101,Error Token $", 131))

    def test_float_02(self):
        self.assertTrue(TestLexer.checkLexeme("0P123", "0,Error Token P", 132))

    def test_float_03(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3", "12.0e3,<EOF>", 133))

    def test_float_04(self):
        self.assertTrue(TestLexer.checkLexeme("12e3", "12e3,<EOF>", 134))

    def test_float_05(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5", "12.e5,<EOF>", 135))

    def test_float_06(self):
        self.assertTrue(TestLexer.checkLexeme("12.0E3", "12.0E3,<EOF>", 136))

    def test_float_07(self):
        self.assertTrue(TestLexer.checkLexeme("12000.", "12000.,<EOF>", 137))

    def test_float_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12000e-1", "12000e-1,<EOF>", 138))

    def test_float_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12e+1", "12e+1,<EOF>", 139))

# ================Test String================

    def test_string_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Give a Man a Fish" """, """Give a Man a Fish,<EOF>""", 140))

    def test_string_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Hello what\\'s your name?" """, """Hello what\\'s your name?,<EOF>""", 141))

    def test_string_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Not the Sharpest Tool\\t in the Shed" """,
            """Not the Sharpest Tool\\t in the Shed,<EOF>""", 142))

    def test_string_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "This\\t is\\t a\\t string\\t containing\\t tabs\\t" """,
            """This\\t is\\t a\\t string\\t containing\\t tabs\\t,<EOF>""", 143))

    def test_string_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Long \\bIn \\bThe \\bTooth" """,
            """Long \\bIn \\bThe \\bTooth,<EOF>""", 144))

    def test_string_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "The beauty of the sunset\\\\ was obscured\\\\ by the industrial cranes." """,
            """The beauty of the sunset\\\\ was obscured\\\\ by the industrial cranes.,<EOF>""", 145))

    def test_string_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "He asked me: '"Where is John?'"" """,
            """He asked me: '"Where is John?'",<EOF>""", 146))

    def test_string_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Are you OK?\\nI ain\\'t\\n" """, """Are you OK?\\nI ain\\'t\\n,<EOF>""", 147))

    def test_string_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem\\b ipsum\\f dolor\\r sit\\n amet." """, """Lorem\\b ipsum\\f dolor\\r sit\\n amet.,<EOF>""", 148))

    def test_string_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem\\t ipsum\\' dolor\\\\ sit\\n amet." """, """Lorem\\t ipsum\\' dolor\\\\ sit\\n amet.,<EOF>""", 149))

# ================Test Array================

    def test_array_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{1, 5,7, 12}", "{,1,,,5,,,7,,,12,},<EOF>", 150))

    def test_array_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1, 2}, {4, 5}, {3, 5}}",
            "{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},<EOF>", 151))

    def test_array_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{True,False,True,False,True}",
            "{,True,,,False,,,True,,,False,,,True,},<EOF>", 152))

    def test_array_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{861836334, 380248978, 445167430, 675130170, 389776614}",
            "{,861836334,,,380248978,,,445167430,,,675130170,,,389776614,},<EOF>", 153))

    def test_array_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{50.683   ,75.217   ,95.988  ,   41.887,89.818}",
            "{,50.683,,,75.217,,,95.988,,,41.887,,,89.818,},<EOF>", 154))

    def test_array_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{99.9997854484,65.e4,25.5353608451e15}",
            "{,99.9997854484,,,65.e4,,,25.5353608451e15,},<EOF>", 155))

    def test_array_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{\"tmp1\", \"tmp2\", \"tmp3\"}",
            "{,tmp1,,,tmp2,,,tmp3,},<EOF>", 156))

    def test_array_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{\"tmp1\", \"tmp2\"},{\"tmp3\", \"tmp4\"},{\"tmp5\", \"tmp6\"}}",
            "{,{,tmp1,,,tmp2,},,,{,tmp3,,,tmp4,},,,{,tmp5,,,tmp6,},},<EOF>", 157))

    def test_array_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{1,2,**tmp**3,4}", "{,1,,,2,,,3,,,4,},<EOF>", 158))

    def test_array_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{True,False},{True,False}}",
            "{,{,True,,,False,},,,{,True,,,False,},},<EOF>", 159))
# ================Test Unclose String================

    def test_unclose_string_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Give a Man a Fish """, """Unclosed String: Give a Man a Fish """, 160))

    def test_unclose_string_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Hello what\\'s your name? """, """Unclosed String: Hello what\\'s your name? """, 161))

    def test_unclose_string_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Not the Sharpest Tool\\t in the Shed """,
            """Unclosed String: Not the Sharpest Tool\\t in the Shed """, 162))

    def test_unclose_string_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "This\\t is\\t a\\t string\\t containing\\t tabs\\t """,
            """Unclosed String: This\\t is\\t a\\t string\\t containing\\t tabs\\t """, 163))

    def test_unclose_string_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Long \\bIn \\bThe \\bTooth """,
            """Unclosed String: Long \\bIn \\bThe \\bTooth """, 164))

    def test_unclose_string_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "The beauty of the sunset\\\\ was obscured\\\\ by the industrial cranes. """,
            """Unclosed String: The beauty of the sunset\\\\ was obscured\\\\ by the industrial cranes. """, 165))

    def test_unclose_string_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "He asked me: '"Where is John?'" """,
            """Unclosed String: He asked me: '"Where is John?'" """, 166))

    def test_unclose_string_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Are you OK?\\nI ain\\'t\\n """, """Unclosed String: Are you OK?\\nI ain\\'t\\n """, 167))

    def test_unclose_string_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem\\b ipsum\\f dolor\\r sit\\n amet. """, """Unclosed String: Lorem\\b ipsum\\f dolor\\r sit\\n amet. """, 168))

    def test_unclose_string_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem\\t ipsum\\' dolor\\\\ sit\\n amet. """, """Unclosed String: Lorem\\t ipsum\\' dolor\\\\ sit\\n amet. """, 169))

# ================Test illigal escape================

    def test_illigal_escape_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ipsum dolor sit amet.\\" """, """Illegal Escape In String: Lorem ipsum dolor sit amet.\\\"""", 170))

    def test_illigal_escape_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ip\\sum dolor sit amet." """, """Illegal Escape In String: Lorem ip\\s""", 171))

    def test_illigal_escape_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ipsum dol\\or sit amet." """, """Illegal Escape In String: Lorem ipsum dol\\o""", 172))

    def test_illigal_escape_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ipsum dolor sit amet\\." """, """Illegal Escape In String: Lorem ipsum dolor sit amet\\.""", 173))

    def test_illigal_escape_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem '"ipsum do\\lor'" sit amet." """, """Illegal Escape In String: Lorem '"ipsum do\\l""", 174))

    def test_illigal_escape_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ipsum dolor si\'t amet." """, """Illegal Escape In String: Lorem ipsum dolor si't""", 175))

    def test_illigal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ip\\sum dolor s\\it amet." """, """Illegal Escape In String: Lorem ip\\s""", 176))

    def test_illigal_escape_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem\\ ipsum dol\\or sit amet." """, """Illegal Escape In String: Lorem\\ """, 177))

    def test_illigal_escape_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lorem ipsum dol\\or sit amet\\." """, """Illegal Escape In String: Lorem ipsum dol\\o""", 178))

    def test_illigal_escape_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "Lor\\em '"ipsum do\\lor'" sit'" amet." """, """Illegal Escape In String: Lor\\e""", 179))

# ================Test Comment================

    def test_comment_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**a1pFUO1JHb**""", """<EOF>""", 180))

    def test_comment_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**12e3**""", """<EOF>""", 181))

    def test_comment_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**Hello what\\'s your name?**""", """<EOF>""", 182))

    def test_comment_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**{{1, 2}, {4, 5}, {3, 5}}**""", """<EOF>""", 183))

    def test_comment_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**"Give a Man a Fish"**""", """<EOF>""", 184))

    def test_comment_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**"Lorem ipsum dol\\or sit amet\\."**""", """<EOF>""", 185))

    def test_comment_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            """****""", """<EOF>""", 186))

    def test_comment_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**            **""", """<EOF>""", 187))

    def test_comment_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**Var: a; **""", """<EOF>""", 188))

    def test_comment_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** ***************** **""", """<EOF>""", 189))

# ================Test Unterminated Comment================

    def test_unterminated_comment_00(self):
        self.assertTrue(TestLexer.checkLexeme(
            """*a1pFUO1JHb**""", """*,a1pFUO1JHb,Unterminated Comment""", 190))

    def test_unterminated_comment_01(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**12e3*""", """Unterminated Comment""", 191))

    def test_unterminated_comment_02(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**Hello what\\'s your name?""", """Unterminated Comment""", 192))

    def test_unterminated_comment_03(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**{{1, 2}, {4, 5}, {3, 5}}""", """Unterminated Comment""", 193))

    def test_unterminated_comment_04(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**"Give a Man a Fish" """, """Unterminated Comment""", 194))

    def test_unterminated_comment_05(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**"Lorem ipsum dol\\or sit amet\\."*""", """Unterminated Comment""", 195))

    def test_unterminated_comment_06(self):
        self.assertTrue(TestLexer.checkLexeme(
            """***""", """Unterminated Comment""", 196))

    def test_unterminated_comment_07(self):
        self.assertTrue(TestLexer.checkLexeme(
            """*            **""", """*,Unterminated Comment""", 197))

    def test_unterminated_comment_08(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**Var: a; *""", """Unterminated Comment""", 198))

    def test_unterminated_comment_09(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**===========*""", """Unterminated Comment""", 199))

