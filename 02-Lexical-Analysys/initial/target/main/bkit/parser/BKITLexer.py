# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("\u008e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\6\2+\n\2\r\2\16\2,\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\6\6:\n\6\r\6\16\6;\3\7\6")
        buf.write("\7?\n\7\r\7\16\7@\3\b\3\b\3\b\3\t\6\tG\n\t\r\t\16\tH\3")
        buf.write("\t\3\t\3\n\3\n\7\nO\n\n\f\n\16\nR\13\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\r\7\r[\n\r\f\r\16\r^\13\r\3\16\3\16\3\16")
        buf.write("\3\16\6\16d\n\16\r\16\16\16e\3\17\6\17i\n\17\r\17\16\17")
        buf.write("j\3\17\5\17n\n\17\3\17\7\17q\n\17\f\17\16\17t\13\17\3")
        buf.write("\17\5\17w\n\17\3\20\6\20z\n\20\r\20\16\20{\3\20\3\20\5")
        buf.write("\20\u0080\n\20\3\20\6\20\u0083\n\20\r\20\16\20\u0084\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\2\2\25\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33\2")
        buf.write("\35\r\37\16!\17#\20%\21\'\22\3\2\b\3\2c|\4\2ZZzz\5\2\62")
        buf.write(";CHch\3\2\62;\5\2\13\f\17\17\"\"\5\2\"\"\62;c|\2\u0099")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3*\3\2\2\2\5.\3\2")
        buf.write("\2\2\7\60\3\2\2\2\t\62\3\2\2\2\13\66\3\2\2\2\r>\3\2\2")
        buf.write("\2\17B\3\2\2\2\21F\3\2\2\2\23L\3\2\2\2\25S\3\2\2\2\27")
        buf.write("U\3\2\2\2\31W\3\2\2\2\33_\3\2\2\2\35h\3\2\2\2\37y\3\2")
        buf.write("\2\2!\u0086\3\2\2\2#\u0088\3\2\2\2%\u008a\3\2\2\2\'\u008c")
        buf.write("\3\2\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2")
        buf.write("\2\2-\4\3\2\2\2./\7=\2\2/\6\3\2\2\2\60\61\7<\2\2\61\b")
        buf.write("\3\2\2\2\62\63\7X\2\2\63\64\7c\2\2\64\65\7t\2\2\65\n\3")
        buf.write("\2\2\2\66\67\7\62\2\2\679\t\3\2\28:\t\4\2\298\3\2\2\2")
        buf.write(":;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\f\3\2\2\2=?\t\5\2\2>=")
        buf.write("\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\16\3\2\2\2BC\7")
        buf.write("k\2\2CD\7h\2\2D\20\3\2\2\2EG\t\6\2\2FE\3\2\2\2GH\3\2\2")
        buf.write("\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\t\2\2K\22\3\2\2\2")
        buf.write("LP\t\2\2\2MO\t\7\2\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3")
        buf.write("\2\2\2Q\24\3\2\2\2RP\3\2\2\2ST\t\2\2\2T\26\3\2\2\2UV\t")
        buf.write("\5\2\2V\30\3\2\2\2W\\\5\25\13\2X[\5\25\13\2Y[\5\27\f\2")
        buf.write("ZX\3\2\2\2ZY\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]")
        buf.write("\32\3\2\2\2^\\\3\2\2\2_`\7g\2\2`a\7/\2\2ac\3\2\2\2bd\5")
        buf.write("\27\f\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\34\3")
        buf.write("\2\2\2gi\5\27\f\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2")
        buf.write("\2\2km\3\2\2\2ln\7\60\2\2ml\3\2\2\2mn\3\2\2\2nr\3\2\2")
        buf.write("\2oq\5\27\f\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2")
        buf.write("sv\3\2\2\2tr\3\2\2\2uw\5\33\16\2vu\3\2\2\2vw\3\2\2\2w")
        buf.write("\36\3\2\2\2xz\5\25\13\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2")
        buf.write("{|\3\2\2\2|}\3\2\2\2}\177\7\"\2\2~\u0080\7\"\2\2\177~")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\u0083")
        buf.write("\5\25\13\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085 \3\2\2\2\u0086")
        buf.write("\u0087\13\2\2\2\u0087\"\3\2\2\2\u0088\u0089\13\2\2\2\u0089")
        buf.write("$\3\2\2\2\u008a\u008b\13\2\2\2\u008b&\3\2\2\2\u008c\u008d")
        buf.write("\13\2\2\2\u008d(\3\2\2\2\22\2,;@HPZ\\ejmrv{\177\u0084")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    HEX = 5
    INT = 6
    IF = 7
    WS = 8
    IDENTIFIER_01 = 9
    IDENTIFIER_02 = 10
    FLOAT = 11
    STRINGS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15
    UNTERMINATED_COMMENT = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "HEX", "INT", "IF", "WS", "IDENTIFIER_01", 
            "IDENTIFIER_02", "FLOAT", "STRINGS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "HEX", "INT", "IF", "WS", 
                  "IDENTIFIER_01", "LETTER", "DIGIT", "IDENTIFIER_02", "EXPONENT", 
                  "FLOAT", "STRINGS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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


