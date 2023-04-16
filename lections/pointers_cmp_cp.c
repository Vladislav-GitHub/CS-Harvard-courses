#include <stdio.h>
#include <cs50.h> // for get_string
#include <string.h> // for strcmp
#include <ctype.h> // for toupper
#include <stdlib.h> // for malloc and free

int main(void)
{
    char *s = "HI!";
    printf("1 character: %c\n", *s);
    printf("2 character: %c\n", *(s + 1)); // goes to the location in memory with the next character, an address that is one byte higher
    printf("3 character: %c\n", *(s + 2)); // equivalent to s[2]

    char *k = get_string("k: ");
    char *t = get_string("t: ");

    if (strcmp(k, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
    printf("Different\n");
    }
    printf("k address: %p\n", k);
    printf("t address: %p\n", t);

    char *g = malloc((strlen(k) + 1));
    strcpy(g, k);
    if (g == NULL)
    {
        return 1;
    }
    g[0] = toupper(g[0]);
    printf("%s\n", g); // Since we set g and k to the same value, or the same address
    printf("%s\n", k); // they’re both pointing to the same character, and so we capitalized the same character in memory
    free(k);
}