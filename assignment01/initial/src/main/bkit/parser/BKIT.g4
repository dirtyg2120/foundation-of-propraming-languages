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

program: VAR COLON ID SM EOF;

// comment: '**' (options {greedy=false;} : .)* '**';

// identifiers
ID: [a-z][_a-zA-Z0-9]*;

// keywords
VAR: 'Var';
FUNCTION: 'Function';
PARAMETER: 'Parameter';

BODY: 'Body';
ENDBODY: 'EndBody';

IF: 'If';
THEN: 'Then';
ELSEIF: 'ElseIf';
ELSE: 'Else';
ENDIF: 'EndIf';

FOR: 'For';
ENDFOR: 'EndFor';

WHILE: 'While';
DO: 'Do';
ENDWHILE: 'EndWhile';
ENDDO: 'EndDo';

BREAK: 'Break';
CONTINUE: 'Continue';
RETURN: 'Return';

TRUE: 'True';
FALSE: 'False';

// seperators
LB_ROUND: '(';
RB_ROUND: ')';
LB_SQUARE: '[';
RB_SQUARE: ']';
LB_CURLY: '{';
RB_CURLY: '}';
COLON: ':';
SM: ';';
DOT: '.';
COMMA: ',';



WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT: [0-9];
fragment UPPER_LETTER: [A-Z];
fragment LOWER_LETTER: [a-z];

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;