#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int scores[3]; // We declare an array, scores, but we didn’t initialize it with any values
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", scores[i]); // The values in the array are garbage values
        //, or whatever unknown values that were in memory, from whatever program was running in our computer before
    }
}