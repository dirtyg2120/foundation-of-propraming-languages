grammar Tutor03;

// @lexer::header { from lexererr import * }

// @lexer::members { def emit(self): tk = self.type result = super().emit() if tk ==
// self.UNCLOSE_STRING: raise UncloseString(result.text[1:]) elif tk == self.ILLEGAL_ESCAPE: raise
// IllegalEscape(result.text[1:]) elif tk == self.ERROR_CHAR: raise ErrorToken(result.text) elif tk
// == self.UNTERMINATED_COMMENT: raise UnterminatedComment() else: return result; }

options {
	language = Python3;
}

program: (var_declare | func_declare)*;
type_bkit: INT | FLOAT;
func_declare: type_bkit ID param_declare body;
param_declare:
	LP (type_bkit idlists ( SM type_bkit idlists)*)? RP;
body: LB (var_declare | stmt) RB;
stmt: stmt_assign | stmt_call | stmt_return;
stmt_assign: ID EQ exp SM;
stmt_call: func_call SM;
stmt_return: RETURN exp SM;
func_call: ID LP (exp (CM exp)*)? RP;
exp:
	operands
	| exp (MULOP | DIVOP) exp
	| <assoc = right>exp ADDOP exp
	| exp SUBOP exp;
operands: INTLIT | FLOATLIT | ID | func_call | LP exp RP;
var_declare: type_bkit idlists SM;
idlists: ID (CM ID)*;

//Lexer
ID: LETTER (DIGIT | LETTER | UNDERSCORE)*;

fragment DIGIT: [0-9];
fragment LETTER: [a-z];
fragment UNDERSCORE: '_';

INTLIT: DECIMAL | HEX | OCTAL;
fragment DECIMAL: '0' | [1-9]+;
fragment HEX: '0' [Xx][0-9A-F]+;
fragment OCTAL: '0' [Oo][0-7]+;

FLOATLIT:
	[0-9]+ (
		DECIMAL_PART
		| EXPONENT_PART
		| DECIMAL_PART EXPONENT_PART
	);
fragment DECIMAL_PART: '.' [0-9]*;
fragment EXPONENT_PART: [Ee][+-]? [0-9]+;

INT: 'int';
FLOAT: 'float';
RETURN: 'return';
LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines