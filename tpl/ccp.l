%{
#include <stdio.h>
#include "y.tab.h"
%}

DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT})*
NUMBER      {DIGIT}+
WHITESPACE  [ \t\n]+
STRING      \"(\\.|[^\\"])*\"

%%

"if"        { return IF; }
"else"      { return ELSE; }
"while"     { return WHILE; }
"return"    { return RETURN; }
"int"       { return INT; }

{IDENTIFIER} { return IDENTIFIER; }
{NUMBER}     { return NUMBER; }
{STRING}     { return STRING; }

"+"          { return PLUS; }
"-"          { return MINUS; }
"*"          { return TIMES; }
"/"          { return DIVIDE; }
"="          { return ASSIGN; }

"("          { return LPAREN; }
")"          { return RPAREN; }
"{"          { return LBRACE; }
"}"          { return RBRACE; }
";"          { return SEMICOLON; }

{WHITESPACE} { /* skip whitespace */ }

.            { /* catch-all for any other character */ }

%%

int yywrap(void) {
    return 1;
}

int main(int argc, char **argv) {
    ++argv, --argc;  /* skip over program name */
    if (argc > 0)
        yyin = fopen(argv[0], "r");
    else
        yyin = stdin;

    yylex();
    return 0;
}
