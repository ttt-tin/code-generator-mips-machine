grammar ZCode;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: exp ADDITION exp
	| funcall
	| INTLIT
	| ID
	;

funcall: ID LB exp? RB ;

INTTYPE: 'int';

VOIDTYPE: 'void';

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

ADDITION: '+';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;