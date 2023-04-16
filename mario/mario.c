#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt user for height
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    //Pyramid's cycle
    //new line
    for (int i = 0; i < height; i++)
    {
        //spaces
        int spaces = height - (i + 1);

        for (int j = 0; j < spaces; j++)
        {
            printf(" ");
        }

        //right-aligned pyramid
        int stairs = i + 1;

        for (int r = 0; r < stairs; r++)
        {
            printf("#");
        }

        printf("  ");

        //left-aligned pyramid
        for (int l = 0; l < stairs; l++)
        {
            printf("#");
        }

        printf("\n");

    }
}