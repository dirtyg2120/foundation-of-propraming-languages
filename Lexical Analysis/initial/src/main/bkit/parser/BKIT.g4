grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
	language = Python3;
}

program: VAR COLON ID SEMI EOF;

ID: [a-z]+;

SEMI: ';';

COLON: ':';

VAR: 'Var';
HEX: '0' [xX] [0-9a-fA-F]+;
INT: [0-9]+;
IF: 'if';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

/* begin Tutorial Answer */
// Question 1
IDENTIFIER_01: [a-z] [a-z 0-9]*;

//question 2
fragment LETTER: [a-z];
fragment DIGIT: [0-9];
IDENTIFIER_02: LETTER (LETTER | DIGIT)*;

//question 3
fragment EXPONENT: 'e-' DIGIT+;
FLOAT: DIGIT+ '.'? DIGIT* EXPONENT?;

STRINGS: LETTER+ ' ' ' '? LETTER+;
/*************************/

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
