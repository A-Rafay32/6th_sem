%{
int givenNumber = 0;
int frequency = 0;
%}

%%
[0-9]+  {
            
            int num = atoi(yytext);
            if (num == givenNumber)
                frequency++;
        }

%%

int yywrap() {
    return 1; // Indicate that there are no more files to parse
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <filename.txt> <number>\n", argv[0]);
        getchar();
        return 1;
    }

    givenNumber = atoi(argv[2]);

    
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        getchar();

        return 1;
    }

    yyin = file;
    yylex();

    fclose(file);

    printf("Frequency of %d: %d\n", givenNumber, frequency);
    getchar();
    getchar();

    return 0;
}
