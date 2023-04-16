#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>



int main(void)//argc - number of words that your user types as a prompt, argv[] - vetor - variable in an array,
// that stores all these strings, which user types
{
    int x = get_int("Enter x: ");
    x %= 27;
    printf("x: %i\n", x);
    string s = get_string("Enter the code: \n");
    int a = atoi(s);
    printf("a: %i\n", a);
    a = a + x;
    printf("new a = %i\n", a);
}