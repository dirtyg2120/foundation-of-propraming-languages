# Generated from /home/hirito/Documents/College/HK201/foundation-of-propraming-languages/Lexical Analysis/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("\33\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\16")
        buf.write("\n\3\r\3\16\3\17\3\3\3\3\5\3\24\n\3\3\3\6\3\27\n\3\r\3")
        buf.write("\16\3\30\3\3\2\2\4\2\4\2\2\2\33\2\6\3\2\2\2\4\r\3\2\2")
        buf.write("\2\6\7\7\7\2\2\7\b\7\6\2\2\b\t\7\4\2\2\t\n\7\5\2\2\n\13")
        buf.write("\7\2\2\3\13\3\3\2\2\2\f\16\7\23\2\2\r\f\3\2\2\2\16\17")
        buf.write("\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21\23")
        buf.write("\7\3\2\2\22\24\7\3\2\2\23\22\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\26\3\2\2\2\25\27\7\23\2\2\26\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\5\17\23\30")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "<INVALID>", "';'", "':'", "'Var'", 
                     "<INVALID>", "<INVALID>", "'if'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "SEMI", "COLON", "VAR", 
                      "HEX", "INT", "IF", "WS", "IDENTIFIER_01", "IDENTIFIER_02", 
                      "FLOAT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT", "LETTER" ]

    RULE_program = 0
    RULE_strings = 1

    ruleNames =  [ "program", "strings" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    SEMI=3
    COLON=4
    VAR=5
    HEX=6
    INT=7
    IF=8
    WS=9
    IDENTIFIER_01=10
    IDENTIFIER_02=11
    FLOAT=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15
    UNTERMINATED_COMMENT=16
    LETTER=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(BKITParser.VAR)
            self.state = 5
            self.match(BKITParser.COLON)
            self.state = 6
            self.match(BKITParser.ID)
            self.state = 7
            self.match(BKITParser.SEMI)
            self.state = 8
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LETTER)
            else:
                return self.getToken(BKITParser.LETTER, i)

        def getRuleIndex(self):
            return BKITParser.RULE_strings




    def strings(self):

        localctx = BKITParser.StringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_strings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.match(BKITParser.LETTER)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LETTER):
                    break

            self.state = 15
            self.match(BKITParser.T__0)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.T__0:
                self.state = 16
                self.match(BKITParser.T__0)


            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.match(BKITParser.LETTER)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LETTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





