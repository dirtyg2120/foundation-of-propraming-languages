# Generated from /home/hirito/Documents/HK201/foundation-of-propraming-languages/03-Syntax-Analysys/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u00a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\7\20]\n\20\f\20\16\20`\13\20")
        buf.write("\3\21\3\21\3\22\3\22\7\22f\n\22\f\22\16\22i\13\22\3\22")
        buf.write("\5\22l\n\22\3\23\3\23\5\23p\n\23\3\23\6\23s\n\23\r\23")
        buf.write("\16\23t\5\23w\n\23\3\23\3\23\6\23{\n\23\r\23\16\23|\3")
        buf.write("\23\3\23\5\23\u0081\n\23\3\23\7\23\u0084\n\23\f\23\16")
        buf.write("\23\u0087\13\23\5\23\u0089\n\23\3\23\3\23\6\23\u008d\n")
        buf.write("\23\r\23\16\23\u008e\5\23\u0091\n\23\3\24\3\24\3\24\6")
        buf.write("\24\u0096\n\24\r\24\16\24\u0097\3\25\6\25\u009b\n\25\r")
        buf.write("\25\16\25\u009c\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\2\2\32\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\22%\2\'\23)")
        buf.write("\24+\25-\26/\27\61\30\3\2\t\5\2C\\aac|\5\2\62;C\\c|\3")
        buf.write("\2\62;\3\2\63;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u00b3")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2#\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\3\63\3\2\2\2\5\67\3\2\2\2\7>\3\2\2\2\t@\3\2\2\2\13")
        buf.write("B\3\2\2\2\rD\3\2\2\2\17F\3\2\2\2\21H\3\2\2\2\23J\3\2\2")
        buf.write("\2\25L\3\2\2\2\27N\3\2\2\2\31P\3\2\2\2\33R\3\2\2\2\35")
        buf.write("T\3\2\2\2\37Z\3\2\2\2!a\3\2\2\2#k\3\2\2\2%v\3\2\2\2\'")
        buf.write("\u0092\3\2\2\2)\u009a\3\2\2\2+\u00a0\3\2\2\2-\u00a2\3")
        buf.write("\2\2\2/\u00a4\3\2\2\2\61\u00a6\3\2\2\2\63\64\7k\2\2\64")
        buf.write("\65\7p\2\2\65\66\7v\2\2\66\4\3\2\2\2\678\7t\2\289\7g\2")
        buf.write("\29:\7v\2\2:;\7w\2\2;<\7t\2\2<=\7p\2\2=\6\3\2\2\2>?\7")
        buf.write("}\2\2?\b\3\2\2\2@A\7\177\2\2A\n\3\2\2\2BC\7=\2\2C\f\3")
        buf.write("\2\2\2DE\7.\2\2E\16\3\2\2\2FG\7?\2\2G\20\3\2\2\2HI\7*")
        buf.write("\2\2I\22\3\2\2\2JK\7+\2\2K\24\3\2\2\2LM\7-\2\2M\26\3\2")
        buf.write("\2\2NO\7/\2\2O\30\3\2\2\2PQ\7,\2\2Q\32\3\2\2\2RS\7\61")
        buf.write("\2\2S\34\3\2\2\2TU\7h\2\2UV\7n\2\2VW\7q\2\2WX\7c\2\2X")
        buf.write("Y\7v\2\2Y\36\3\2\2\2Z^\t\2\2\2[]\t\3\2\2\\[\3\2\2\2]`")
        buf.write("\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_ \3\2\2\2`^\3\2\2\2ab\t")
        buf.write("\4\2\2b\"\3\2\2\2cg\t\5\2\2df\5!\21\2ed\3\2\2\2fi\3\2")
        buf.write("\2\2ge\3\2\2\2gh\3\2\2\2hl\3\2\2\2ig\3\2\2\2jl\7\62\2")
        buf.write("\2kc\3\2\2\2kj\3\2\2\2l$\3\2\2\2mo\t\6\2\2np\t\7\2\2o")
        buf.write("n\3\2\2\2op\3\2\2\2pr\3\2\2\2qs\5!\21\2rq\3\2\2\2st\3")
        buf.write("\2\2\2tr\3\2\2\2tu\3\2\2\2uw\3\2\2\2vm\3\2\2\2vw\3\2\2")
        buf.write("\2w\u0090\3\2\2\2xz\7\60\2\2y{\5!\21\2zy\3\2\2\2{|\3\2")
        buf.write("\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\u0080\t\6\2\2\177")
        buf.write("\u0081\t\7\2\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\u0085\3\2\2\2\u0082\u0084\5!\21\2\u0083\u0082\3\2\2\2")
        buf.write("\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3")
        buf.write("\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0088x")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0091\3\2\2\2\u008a")
        buf.write("\u008c\7\60\2\2\u008b\u008d\5!\21\2\u008c\u008b\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0088\3\2\2\2\u0090")
        buf.write("\u008a\3\2\2\2\u0091&\3\2\2\2\u0092\u0093\5#\22\2\u0093")
        buf.write("\u0095\7\60\2\2\u0094\u0096\5!\21\2\u0095\u0094\3\2\2")
        buf.write("\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098(\3\2\2\2\u0099\u009b\t\b\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\b\25\2")
        buf.write("\2\u009f*\3\2\2\2\u00a0\u00a1\13\2\2\2\u00a1,\3\2\2\2")
        buf.write("\u00a2\u00a3\13\2\2\2\u00a3.\3\2\2\2\u00a4\u00a5\13\2")
        buf.write("\2\2\u00a5\60\3\2\2\2\u00a6\u00a7\13\2\2\2\u00a7\62\3")
        buf.write("\2\2\2\21\2^gkotv|\u0080\u0085\u0088\u008e\u0090\u0097")
        buf.write("\u009c\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    RETURN = 2
    LB = 3
    RB = 4
    SM = 5
    CM = 6
    EQ = 7
    LP = 8
    RP = 9
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    FLOAT = 14
    ID = 15
    INTLIT = 16
    FLOATLIT = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21
    UNTERMINATED_COMMENT = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'return'", "'{'", "'}'", "';'", "','", "'='", "'('", 
            "')'", "'+'", "'-'", "'*'", "'/'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", "RP", "ADD", 
            "SUB", "MUL", "DIV", "FLOAT", "ID", "INTLIT", "FLOATLIT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", "RP", 
                  "ADD", "SUB", "MUL", "DIV", "FLOAT", "ID", "DIGIT", "INTLIT", 
                  "EX", "FLOATLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


