%{
#include <stdio.h>
#include <string.h>
int char_count = 0;
int word_count = 0;
int digit_count = 0;
int line_count = 0;
int space_count = 0;
int tab_count = 0;
int special_char_count = 0;
%}

%%
[a-zA-Z]+   { word_count++; char_count += strlen(yytext);  }
[0-9]       { digit_count++; }
\n          { line_count++; }
[ \t]       { space_count++; }
.           { special_char_count++; }

%%
int yywrap(){}
int main() {
    FILE *fp;
    char filename[50];
    printf("Enter the filename: \n");
    scanf("%s",filename);
    fp = fopen(filename,"r");
    if (!fp) {
        perror("Error opening file");
        getchar();
        return 1;
    }
    yyin = fp;
    yylex();

    fclose(fp);

    printf("Character count: %d\n", char_count);
    printf("Word count: %d\n", word_count);
    printf("Digit count: %d\n", digit_count);
    printf("Line count: %d\n", line_count);
    printf("Space count: %d\n", space_count);
    printf("Tab count: %d\n", space_count);
    printf("Special character count: %d\n", special_char_count);
    getchar();
    getchar();
    return 0;
}
