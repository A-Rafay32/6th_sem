%{
#include <stdio.h>
%}

DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT})*
NUMBER      {DIGIT}+
WHITESPACE  [ \t\n]+
STRING      \"(\\.|[^\\"])*\"

%%

"if"        { printf("IF\n"); }
"else"      { printf("ELSE\n"); }
"while"     { printf("WHILE\n"); }
"return"    { printf("RETURN\n"); }
"int"       { printf("INT\n"); }

{IDENTIFIER} { printf("IDENTIFIER(%s)\n", yytext); }
{NUMBER}     { printf("NUMBER(%s)\n", yytext); }
{STRING}     { printf("STRING(%s)\n", yytext); }

"+"          { printf("PLUS\n"); }
"-"          { printf("MINUS\n"); }
"*"          { printf("TIMES\n"); }
"/"          { printf("DIVIDE\n"); }
"="          { printf("ASSIGN\n"); }

"("          { printf("LPAREN\n"); }
")"          { printf("RPAREN\n"); }
"{"          { printf("LBRACE\n"); }
"}"          { printf("RBRACE\n"); }
";"          { printf("SEMICOLON\n"); }

{WHITESPACE} { /* skip whitespace */ }

.            { printf("UNKNOWN(%s)\n", yytext); }

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
