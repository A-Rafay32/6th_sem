%{
#include <stdio.h>
%}

EMAIL    [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
DOB      [0-9]{2}\/[0-9]{2}\/[0-9]{4}
NIC      [0-9]{5}-[0-9]{7}-[0-9]{1}

%%

{EMAIL}    { printf("Email: %s\n", yytext); }
{DOB}      { printf("DOB: %s\n", yytext); }
{NIC}      { printf("NIC: %s\n", yytext); }
.          ;

%%

int main() {
    // Open file here
    yyin = fopen("file3.txt", "r");
    yylex();
    fclose(yyin);
    getchar();
    getchar();
    return 0;
}

// Handle EOF
int yywrap() {
    return 1;
}


