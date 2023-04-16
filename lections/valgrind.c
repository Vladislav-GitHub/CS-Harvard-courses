#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int)); // use malloc to get enough memory for 3 times the size of an int, which we can find out with sizeof
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
    free(x);
}