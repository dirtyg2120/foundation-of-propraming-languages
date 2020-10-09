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

// comment: '**' (options {greedy=false;} : .)* '**';

ID: [a-z][_a-zA-Z0-9]*;

SEMI: ';';

COLON: ':';

VAR: 'Var';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT: [0-9];
fragment UPPER_LETTER: [A-Z];
fragment LOWER_LETTER: [a-z];

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;