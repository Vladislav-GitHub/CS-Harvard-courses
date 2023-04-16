#include <cs50.h>
#include <stdio.h>
#include <math.h>

int k, l, g, check, counter1, counter2;
long Num;

int main(void)
{
    //Prompt user for card's number
    do
    {
        Num = get_long("Number: ");
    }
    while ((Num == '-') || (Num <= 0));
    
    //First digits
    for (long i = Num; i > 1; i /= 100)
    {
        int remain = i % 100;
        remain /= 10;
        k = 2 * round(remain);//multiply by 2
        g += (round(k / 10) + k % 10);//get digits
        counter1++;
    }
        
    //Second digits
    for (long i = Num; i > 1; i /= 100)
    {
        int remain = i % 100;
        remain %= 10;
        l += round(remain);
        counter2++;
    }
    
    int digits = counter1 + counter2;
        
    //VALID CHECK
    check = (g + l) % 10;
    if (check != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        if (((int)(Num / pow(10, 12)) == 4) || ((int)(Num / pow(10, 15)) == 4))
        {
            printf("VISA\n");
        }
        else if (((int)(Num / pow(10, 13)) == 34) || ((int)(Num / pow(10, 13)) == 37))
        {
            printf("AMEX\n");
        }
        else
        {
            printf("MASTERCARD\n");
        }
    }
}