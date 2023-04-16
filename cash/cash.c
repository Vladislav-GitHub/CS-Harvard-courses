#include <cs50.h>
#include <stdio.h>
#include <math.h>

int k, cents, remain;
float dollars, coins;

int main(void)
{
    //Prompt user for values
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars <= 0);
    
    cents = round(dollars * 100);
    
    
        if ((int)cents % 25 != 0)
        {
            for (int i = cents; i > 0; i /= 25)
            {
                (int) cents /= 25;
                remain = (cents % 25) * 100;
                coins++;
            }
            cents = remain;
        }
        
        else if ((int)cents % 10 != 0)
        {
            for (int i = cents; i > 0; i /= 10)
            {
                cents /= 10;
                coins++;
            }
        }
        
        else if ((int)cents % 5 != 0)
        {
            for (int i = cents; i > 0; i /= 5)
            {
                cents /= 5;
                coins++;
            }
        }
        else
        {
            for (int i = cents; i > 0; i--)
            {
                cents--;
                coins++;
            }
        }
}