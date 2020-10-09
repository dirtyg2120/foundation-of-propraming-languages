# Generated from /home/hirito/Documents/HK201/foundation-of-propraming-languages/03-Syntax-Analysys/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("\u00b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\5\2+\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\65\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5C\n\5\f\5\16\5F\13\5\5\5H\n\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7T\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\b_\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\tf\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\fx\n\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u0083\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u008a\n\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\7\20\u0095\n\20\f\20\16\20\u0098\13\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00a2\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00ac")
        buf.write("\n\23\3\24\3\24\3\24\2\3\36\25\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&\2\3\4\2\3\3\20\20\2\u00b5\2*\3\2")
        buf.write("\2\2\4\64\3\2\2\2\6\66\3\2\2\2\bG\3\2\2\2\nI\3\2\2\2\f")
        buf.write("S\3\2\2\2\16^\3\2\2\2\20e\3\2\2\2\22g\3\2\2\2\24l\3\2")
        buf.write("\2\2\26w\3\2\2\2\30y\3\2\2\2\32\u0082\3\2\2\2\34\u0089")
        buf.write("\3\2\2\2\36\u008b\3\2\2\2 \u00a1\3\2\2\2\"\u00a3\3\2\2")
        buf.write("\2$\u00ab\3\2\2\2&\u00ad\3\2\2\2(+\5\4\3\2)+\3\2\2\2*")
        buf.write("(\3\2\2\2*)\3\2\2\2+\3\3\2\2\2,\65\5\"\22\2-\65\5\6\4")
        buf.write("\2./\5\"\22\2/\60\5\4\3\2\60\65\3\2\2\2\61\62\5\6\4\2")
        buf.write("\62\63\5\4\3\2\63\65\3\2\2\2\64,\3\2\2\2\64-\3\2\2\2\64")
        buf.write(".\3\2\2\2\64\61\3\2\2\2\65\5\3\2\2\2\66\67\5&\24\2\67")
        buf.write("8\7\21\2\289\7\n\2\29:\5\b\5\2:;\7\13\2\2;<\7\5\2\2<=")
        buf.write("\5\16\b\2=>\7\6\2\2>\7\3\2\2\2?D\5\n\6\2@A\7\7\2\2AC\5")
        buf.write("\n\6\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EH\3\2\2")
        buf.write("\2FD\3\2\2\2G?\3\2\2\2GH\3\2\2\2H\t\3\2\2\2IJ\5&\24\2")
        buf.write("JK\5$\23\2K\13\3\2\2\2LM\5\"\22\2MN\5\f\7\2NT\3\2\2\2")
        buf.write("OP\5&\24\2PQ\5$\23\2QT\3\2\2\2RT\3\2\2\2SL\3\2\2\2SO\3")
        buf.write("\2\2\2SR\3\2\2\2T\r\3\2\2\2U_\5\"\22\2V_\5\20\t\2WX\5")
        buf.write("\"\22\2XY\5\16\b\2Y_\3\2\2\2Z[\5\20\t\2[\\\5\16\b\2\\")
        buf.write("_\3\2\2\2]_\3\2\2\2^U\3\2\2\2^V\3\2\2\2^W\3\2\2\2^Z\3")
        buf.write("\2\2\2^]\3\2\2\2_\17\3\2\2\2`f\5\22\n\2ab\5\24\13\2bc")
        buf.write("\7\7\2\2cf\3\2\2\2df\5\30\r\2e`\3\2\2\2ea\3\2\2\2ed\3")
        buf.write("\2\2\2f\21\3\2\2\2gh\7\21\2\2hi\7\t\2\2ij\5\32\16\2jk")
        buf.write("\7\7\2\2k\23\3\2\2\2lm\7\21\2\2mn\7\n\2\2no\5\26\f\2o")
        buf.write("p\7\13\2\2p\25\3\2\2\2qx\5\32\16\2rs\5\32\16\2st\7\b\2")
        buf.write("\2tu\5\26\f\2ux\3\2\2\2vx\3\2\2\2wq\3\2\2\2wr\3\2\2\2")
        buf.write("wv\3\2\2\2x\27\3\2\2\2yz\7\4\2\2z{\5\32\16\2{|\7\7\2\2")
        buf.write("|\31\3\2\2\2}~\5\34\17\2~\177\7\f\2\2\177\u0080\5\32\16")
        buf.write("\2\u0080\u0083\3\2\2\2\u0081\u0083\5\34\17\2\u0082}\3")
        buf.write("\2\2\2\u0082\u0081\3\2\2\2\u0083\33\3\2\2\2\u0084\u0085")
        buf.write("\5\36\20\2\u0085\u0086\7\r\2\2\u0086\u0087\5\36\20\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u008a\5\36\20\2\u0089\u0084\3\2\2")
        buf.write("\2\u0089\u0088\3\2\2\2\u008a\35\3\2\2\2\u008b\u008c\b")
        buf.write("\20\1\2\u008c\u008d\5 \21\2\u008d\u0096\3\2\2\2\u008e")
        buf.write("\u008f\f\5\2\2\u008f\u0090\7\16\2\2\u0090\u0095\5 \21")
        buf.write("\2\u0091\u0092\f\4\2\2\u0092\u0093\7\17\2\2\u0093\u0095")
        buf.write("\5 \21\2\u0094\u008e\3\2\2\2\u0094\u0091\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\37\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u00a2\7\21")
        buf.write("\2\2\u009a\u00a2\7\22\2\2\u009b\u00a2\7\23\2\2\u009c\u00a2")
        buf.write("\5\24\13\2\u009d\u009e\7\n\2\2\u009e\u009f\5\32\16\2\u009f")
        buf.write("\u00a0\7\13\2\2\u00a0\u00a2\3\2\2\2\u00a1\u0099\3\2\2")
        buf.write("\2\u00a1\u009a\3\2\2\2\u00a1\u009b\3\2\2\2\u00a1\u009c")
        buf.write("\3\2\2\2\u00a1\u009d\3\2\2\2\u00a2!\3\2\2\2\u00a3\u00a4")
        buf.write("\5&\24\2\u00a4\u00a5\5$\23\2\u00a5\u00a6\7\7\2\2\u00a6")
        buf.write("#\3\2\2\2\u00a7\u00ac\7\21\2\2\u00a8\u00a9\7\21\2\2\u00a9")
        buf.write("\u00aa\7\b\2\2\u00aa\u00ac\5$\23\2\u00ab\u00a7\3\2\2\2")
        buf.write("\u00ab\u00a8\3\2\2\2\u00ac%\3\2\2\2\u00ad\u00ae\t\2\2")
        buf.write("\2\u00ae\'\3\2\2\2\20*\64DGS^ew\u0082\u0089\u0094\u0096")
        buf.write("\u00a1\u00ab")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'return'", "'{'", "'}'", "';'", 
                     "','", "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'float'" ]

    symbolicNames = [ "<INVALID>", "INT", "RETURN", "LB", "RB", "SM", "CM", 
                      "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", "FLOAT", 
                      "ID", "INTLIT", "FLOATLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_function_declaration = 2
    RULE_param_list = 3
    RULE_para = 4
    RULE_parameter = 5
    RULE_body = 6
    RULE_statements = 7
    RULE_assignment = 8
    RULE_call = 9
    RULE_list_expressions = 10
    RULE_retur = 11
    RULE_expression = 12
    RULE_expression1 = 13
    RULE_expression2 = 14
    RULE_expression3 = 15
    RULE_variable_declaration = 16
    RULE_variable = 17
    RULE_typ = 18

    ruleNames =  [ "program", "declarations", "function_declaration", "param_list", 
                   "para", "parameter", "body", "statements", "assignment", 
                   "call", "list_expressions", "retur", "expression", "expression1", 
                   "expression2", "expression3", "variable_declaration", 
                   "variable", "typ" ]

    EOF = Token.EOF
    INT=1
    RETURN=2
    LB=3
    RB=4
    SM=5
    CM=6
    EQ=7
    LP=8
    RP=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    FLOAT=14
    ID=15
    INTLIT=16
    FLOATLIT=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21
    UNTERMINATED_COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(BKITParser.DeclarationsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT, BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.declarations()
                pass
            elif token in [BKITParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(BKITParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(BKITParser.Function_declarationContext,0)


        def declarations(self):
            return self.getTypedRuleContext(BKITParser.DeclarationsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declarations




    def declarations(self):

        localctx = BKITParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.function_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.variable_declaration()
                self.state = 45
                self.declarations()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.function_declaration()
                self.state = 48
                self.declarations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKITParser.TypContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_function_declaration




    def function_declaration(self):

        localctx = BKITParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.typ()
            self.state = 53
            self.match(BKITParser.ID)
            self.state = 54
            self.match(BKITParser.LP)
            self.state = 55
            self.param_list()
            self.state = 56
            self.match(BKITParser.RP)
            self.state = 57
            self.match(BKITParser.LB)
            self.state = 58
            self.body()
            self.state = 59
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParaContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParaContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SM)
            else:
                return self.getToken(BKITParser.SM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 61
                self.para()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.SM:
                    self.state = 62
                    self.match(BKITParser.SM)
                    self.state = 63
                    self.para()
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKITParser.TypContext,0)


        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para




    def para(self):

        localctx = BKITParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.typ()
            self.state = 72
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(BKITParser.Variable_declarationContext,0)


        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext,0)


        def typ(self):
            return self.getTypedRuleContext(BKITParser.TypContext,0)


        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.variable_declaration()
                self.state = 75
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.typ()
                self.state = 78
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(BKITParser.Variable_declarationContext,0)


        def statements(self):
            return self.getTypedRuleContext(BKITParser.StatementsContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.variable_declaration()
                self.state = 86
                self.body()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.statements()
                self.state = 89
                self.body()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BKITParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def retur(self):
            return self.getTypedRuleContext(BKITParser.ReturContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statements




    def statements(self):

        localctx = BKITParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.call()
                self.state = 96
                self.match(BKITParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.retur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignment




    def assignment(self):

        localctx = BKITParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKITParser.ID)
            self.state = 102
            self.match(BKITParser.EQ)
            self.state = 103
            self.expression()
            self.state = 104
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def list_expressions(self):
            return self.getTypedRuleContext(BKITParser.List_expressionsContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BKITParser.ID)
            self.state = 107
            self.match(BKITParser.LP)
            self.state = 108
            self.list_expressions()
            self.state = 109
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def list_expressions(self):
            return self.getTypedRuleContext(BKITParser.List_expressionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_expressions




    def list_expressions(self):

        localctx = BKITParser.List_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expressions)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.expression()
                self.state = 113
                self.match(BKITParser.CM)
                self.state = 114
                self.list_expressions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_retur




    def retur(self):

        localctx = BKITParser.ReturContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_retur)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKITParser.RETURN)
            self.state = 120
            self.expression()
            self.state = 121
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(BKITParser.Expression1Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.expression1()
                self.state = 124
                self.match(BKITParser.ADD)
                self.state = 125
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expression2Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expression2Context,i)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression1




    def expression1(self):

        localctx = BKITParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression1)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.expression2(0)
                self.state = 131
                self.match(BKITParser.SUB)
                self.state = 132
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(BKITParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(BKITParser.Expression2Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expression3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 146
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 140
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 141
                        self.match(BKITParser.MUL)
                        self.state = 142
                        self.expression3()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 143
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 144
                        self.match(BKITParser.DIV)
                        self.state = 145
                        self.expression3()
                        pass

             
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression3




    def expression3(self):

        localctx = BKITParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression3)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(BKITParser.LP)
                self.state = 156
                self.expression()
                self.state = 157
                self.match(BKITParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKITParser.TypContext,0)


        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = BKITParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.typ()
            self.state = 162
            self.variable()
            self.state = 163
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_variable)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BKITParser.ID)
                self.state = 167
                self.match(BKITParser.CM)
                self.state = 168
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_typ




    def typ(self):

        localctx = BKITParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




