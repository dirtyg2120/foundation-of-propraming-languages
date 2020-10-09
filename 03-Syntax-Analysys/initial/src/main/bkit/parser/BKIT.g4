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

program: declarations |;

declarations:
	variable_declaration
	| function_declaration
	| variable_declaration declarations
	| function_declaration declarations;

function_declaration: typ ID LP param_list RP LB body RB;

param_list: (para (SM para)*)?;

para: typ variable;

parameter: variable_declaration parameter | typ variable |;

body:
	variable_declaration
	| statements
	| variable_declaration body
	| statements body
	|;

statements: assignment | call SM | retur;

assignment: ID EQ expression SM;

call: ID LP list_expressions RP;

list_expressions: expression | expression CM list_expressions |;

retur: RETURN expression SM;

expression: expression1 ADD expression | expression1;
expression1: expression2 SUB expression2 | expression2;
expression2:
	expression2 MUL expression3
	| expression2 DIV expression3
	| expression3;
expression3: ID | INTLIT | FLOATLIT | call | LP expression RP;

variable_declaration: typ variable SM;

variable: ID | ID CM variable;

typ: (INT | FLOAT);

INT: 'int';

RETURN: 'return';

LB: '{';

RB: '}';

SM: ';';

CM: ',';

EQ: '=';

LP: '(';

RP: ')';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

FLOAT: 'float';

ID: [_a-zA-Z][a-zA-Z0-9]*;

fragment DIGIT: [0-9];

INTLIT: [1-9] DIGIT* | '0';

fragment EX: ([eE][+-]? DIGIT+)? (
		('.' DIGIT+ ([eE][+-]? DIGIT*))?
		| '.' DIGIT+
	);

FLOATLIT: INTLIT '.' DIGIT+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;