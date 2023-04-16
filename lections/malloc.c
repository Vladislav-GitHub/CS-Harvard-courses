#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: \n");
    char *t = malloc(strlen(s) + 1); // function, malloc, to allocate some number of bytes in memory

    if (t == NULL) // error checking
    {
        return 1; // if our computer is out of memory, malloc will return NULL
        // , the null pointer, or a special value of all 0 bits that indicates there isn’t an address to point to
    }

    for (int i = 0, n = strlen(s) + 1; i < n; i++) // instead of this cycle we can use strcpy(t, s);
    {
        t[i] = s[i];
    }

    if (strlen(t) > 0) // check that t has a length, before trying to capitalize the first character
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t); // call free on t, since we allocated it ourselves
}
