#include <stdio.h>
#include <cs50.h>

//Constant
const int N = 3;

// Prototype10
float average(int length, int array[]);

int main(void)
{
    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score");
    }
    printf("Average: %f\n", average(N, scores));

    //prompt user for their name and show it on the terminal window
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}

float average(int length, float array[])
{
    //Calculate average
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}