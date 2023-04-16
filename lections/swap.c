#include <stdio.h>

//prototype
void swap(int *a, int *b);

int main(void)
{
    int x = 2;
    int y;
    printf("y: ");
    scanf("%i", &y);
    printf("\nx: %i and y: %i\n", x, y);
    swap(&x, &y);
    printf("x: %i and y: %i\n", x, y);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
