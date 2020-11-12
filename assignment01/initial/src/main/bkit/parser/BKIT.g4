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

/*====================================================== PROGRAM STRUCTURE ====================================================== */
program: variable_declaration* func_declaration* EOF;

variable_declaration: VAR COLON variable_list SM;
variable_list: variable (CM variable)*;
variable: ID (LB_SQUARE INT RB_SQUARE)* (ASSIGN literal)?;

func_declaration: FUNCTION COLON ID param_declaration? body;
param_declaration: PARAMETER COLON param_list;
param_list: param (CM param)*;
param: ID (LB_SQUARE INT RB_SQUARE)*;

body: begin_body variable_declaration* stmt* end_body;

/*========== Statements ==========*/
stmt:
	statement_assign
	| statement_if
	| statement_for
	| statement_while
	| statement_do_while
	| statement_break
	| statement_continue
	| statement_call
	| statement_return;

// statement_assign: ID (LB_SQUARE exp RB_SQUARE)* ASSIGN exp SM;
statement_assign: ( ID | array_cell_decl) ASSIGN exp SM;

array_cell_decl: (ID | function_call) (LB_SQUARE exp RB_SQUARE)+;

statement_if: if_then_stmt else_if_stmt* else_stmt? ENDIF DOT;
if_then_stmt: IF exp THEN then_stmt;
else_if_stmt: ELSE IF exp THEN then_stmt;
else_stmt: ELSE then_stmt;
then_stmt: variable_declaration* stmt*;

// statement_if: IF THEN ENDIF DOT;

statement_for:
	FOR LB_ROUND ID ASSIGN exp CM exp CM exp RB_ROUND DO variable_declaration* stmt* ENDFOR DOT;

statement_while:
	WHILE exp DO variable_declaration* stmt* ENDWHILE DOT;

statement_do_while:
	DO variable_declaration* stmt* WHILE exp ENDDO DOT;

statement_break: BREAK SM;
statement_continue: CONTINUE SM;
statement_call: function_call SM;
function_call: ID LB_ROUND (exp (CM exp)*)? RB_ROUND;

statement_return: RETURN exp? SM;

exp: exp1 ( OP_COMPARE_INT | OP_COMPARE_FLOAT) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2:
	exp2 (ADD_INT | ADD_FLOAT | SUB_INT | SUB_FLOAT) exp3
	| exp3;
exp3:
	exp3 (MUL_INT | MUL_FLOAT | DIV_INT | DIV_FLOAT | MOD_INT) exp4
	| exp4;
exp4: NOT exp4 | exp5;
exp5: (SUB_FLOAT | SUB_INT) exp5 | operand;

operand: literal | ID | function_call | LB_ROUND exp RB_ROUND;

literal:
	INT
	| FLOAT
	| BOOLEAN
	| array_literal
	| STRING
	| array_cell_decl;

array_literal: LB_CURLY ( exp (CM exp)*)? RB_CURLY;

begin_body: BODY COLON;
end_body: ENDBODY DOT;

/*================================================================
 LEXER ================================================================
 */

INT: DECIMAL | HEX | OCTAL;
fragment DECIMAL: DIGIT | [1-9]DIGIT*;
fragment HEX: '0' [xX] (DIGIT | [A-F])*;
fragment OCTAL: '0' [oO][0-7]*;

FLOAT: INT (DOT DIGIT* EXPONENT* | EXPONENT);
fragment EXPONENT: [eE][+-]? DIGIT+;

BOOLEAN: TRUE | FALSE;

STRING:
	'"' CHAR_LITERAL_IN_STRING* '"' { 
    value = str(self.text)
    self.text = value[1:-1]
};

// ARRAY: LB_CURLY WS* (WS* LITERALS WS* (CM WS* LITERALS WS*)*)? WS* RB_CURLY;

fragment LITERALS: INT | FLOAT | BOOLEAN | STRING;
COMMENT: '**' .*? '**' -> skip; //** **

/*========== identifiers ==========*/
ID: LOWER_LETTER ('_' | LOWER_LETTER | UPPER_LETTER | DIGIT)*;

/*========== keywords ==========*/
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

/*========= operators ==========*/
ASSIGN: '=';

// INTEGER
ADD_INT: '+';
SUB_INT: '-';
MUL_INT: '*';
DIV_INT: '\\';
MOD_INT: '%';

OP_COMPARE_INT:
	EQUAL
	| NOT_EQUAL_INT
	| LT_INT
	| GT_INT
	| LTE_INT
	| GTE_INT;
EQUAL: '==';
NOT_EQUAL_INT: '!=';
LT_INT: '<';
GT_INT: '>';
LTE_INT: '<=';
GTE_INT: '>=';

// FLOAT
ADD_FLOAT: '+.';
SUB_FLOAT: '-.';
MUL_FLOAT: '*.';
DIV_FLOAT: '\\.';

OP_COMPARE_FLOAT:
	NOT_EQUAL_FLOAT
	| LT_FLOAT
	| GT_FLOAT
	| LTE_FLOAT
	| GTE_FLOAT;
NOT_EQUAL_FLOAT: '=/=';
LT_FLOAT: '<.';
GT_FLOAT: '>.';
LTE_FLOAT: '<=.';
GTE_FLOAT: '>=.';

// BOOLEAN
NOT: '!';
AND: '&&';
OR: '||';

/*========== seperators ==========*/
LB_ROUND: '(';
RB_ROUND: ')';
LB_SQUARE: '[';
RB_SQUARE: ']';
LB_CURLY: '{';
RB_CURLY: '}';
COLON: ':';
SM: ';';
DOT: '.';
CM: ',';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT: [0-9];
fragment UPPER_LETTER: [A-Z];
fragment LOWER_LETTER: [a-z];

fragment CHAR_LITERAL_IN_STRING: (
		'\\' [btnfr'\\]
		| '\'"'
		| ~[\n\\"']
	);

ERROR_CHAR: .;
UNCLOSE_STRING:
	'"' CHAR_LITERAL_IN_STRING* {
        value = str(self.text)
        self.text = value[1:]
    };
ILLEGAL_ESCAPE:
	'"' CHAR_LITERAL_IN_STRING* ('\\' ~[btnfr'\\] | '\'' ~["]) {
        value = str(self.text)
        self.text = value[1:]
    };
UNTERMINATED_COMMENT: '**' .*?;