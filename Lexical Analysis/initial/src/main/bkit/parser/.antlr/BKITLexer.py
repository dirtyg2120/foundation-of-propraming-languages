# Generated from /home/hirito/Documents/College/HK201/foundation-of-propraming-languages/Lexical Analysis/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("\u0082\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\3\2\3\3\6\3-\n\3\r\3\16\3.\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\6\7<\n\7\r\7\16\7")
        buf.write("=\3\b\6\bA\n\b\r\b\16\bB\3\t\3\t\3\t\3\n\6\nI\n\n\r\n")
        buf.write("\16\nJ\3\n\3\n\3\13\3\13\7\13Q\n\13\f\13\16\13T\13\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\16\7\16]\n\16\f\16\16\16")
        buf.write("`\13\16\3\17\3\17\3\17\3\17\6\17f\n\17\r\17\16\17g\3\20")
        buf.write("\6\20k\n\20\r\20\16\20l\3\20\5\20p\n\20\3\20\7\20s\n\20")
        buf.write("\f\20\16\20v\13\20\3\20\5\20y\n\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\2\31\2\33\r\35\2\37\16!\17#\20%")
        buf.write("\21\'\22\3\2\b\3\2c|\4\2ZZzz\5\2\62;CHch\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\5\2\"\"\62;c|\2\u008a\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5,\3\2\2\2\7\60\3\2\2\2\t")
        buf.write("\62\3\2\2\2\13\64\3\2\2\2\r8\3\2\2\2\17@\3\2\2\2\21D\3")
        buf.write("\2\2\2\23H\3\2\2\2\25N\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2")
        buf.write("\33Y\3\2\2\2\35a\3\2\2\2\37j\3\2\2\2!z\3\2\2\2#|\3\2\2")
        buf.write("\2%~\3\2\2\2\'\u0080\3\2\2\2)*\7\"\2\2*\4\3\2\2\2+-\t")
        buf.write("\2\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\6\3\2")
        buf.write("\2\2\60\61\7=\2\2\61\b\3\2\2\2\62\63\7<\2\2\63\n\3\2\2")
        buf.write("\2\64\65\7X\2\2\65\66\7c\2\2\66\67\7t\2\2\67\f\3\2\2\2")
        buf.write("89\7\62\2\29;\t\3\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;")
        buf.write("\3\2\2\2=>\3\2\2\2>\16\3\2\2\2?A\t\5\2\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2C\20\3\2\2\2DE\7k\2\2EF\7h\2")
        buf.write("\2F\22\3\2\2\2GI\t\6\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2")
        buf.write("JK\3\2\2\2KL\3\2\2\2LM\b\n\2\2M\24\3\2\2\2NR\t\2\2\2O")
        buf.write("Q\t\7\2\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\26")
        buf.write("\3\2\2\2TR\3\2\2\2UV\t\2\2\2V\30\3\2\2\2WX\t\5\2\2X\32")
        buf.write("\3\2\2\2Y^\5\27\f\2Z]\5\27\f\2[]\5\31\r\2\\Z\3\2\2\2\\")
        buf.write("[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\34\3\2\2\2`")
        buf.write("^\3\2\2\2ab\7g\2\2bc\7/\2\2ce\3\2\2\2df\t\5\2\2ed\3\2")
        buf.write("\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\36\3\2\2\2ik\t\5\2")
        buf.write("\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2n")
        buf.write("p\7\60\2\2on\3\2\2\2op\3\2\2\2pt\3\2\2\2qs\t\5\2\2rq\3")
        buf.write("\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2ux\3\2\2\2vt\3\2\2")
        buf.write("\2wy\5\35\17\2xw\3\2\2\2xy\3\2\2\2y \3\2\2\2z{\13\2\2")
        buf.write("\2{\"\3\2\2\2|}\13\2\2\2}$\3\2\2\2~\177\13\2\2\2\177&")
        buf.write("\3\2\2\2\u0080\u0081\13\2\2\2\u0081(\3\2\2\2\17\2.=BJ")
        buf.write("R\\^glotx\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    SEMI = 3
    COLON = 4
    VAR = 5
    HEX = 6
    INT = 7
    IF = 8
    WS = 9
    IDENTIFIER_01 = 10
    IDENTIFIER_02 = 11
    FLOAT = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15
    UNTERMINATED_COMMENT = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "';'", "':'", "'Var'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "HEX", "INT", "IF", "WS", "IDENTIFIER_01", 
            "IDENTIFIER_02", "FLOAT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "ID", "SEMI", "COLON", "VAR", "HEX", "INT", "IF", 
                  "WS", "IDENTIFIER_01", "LETTER", "DIGIT", "IDENTIFIER_02", 
                  "EXPONENT", "FLOAT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


