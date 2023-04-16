#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int trackalpha;
string key;

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        for (int i = 0, len = strlen(argv[1]); i < len; i++) // how many letters
        {
            if (isalpha(argv[1][i]))
            {
                trackalpha += 1;
            }
        }
        if (trackalpha == strlen(argv[1])) // to make sure all chars are letters
        {
            key = argv[1]; //convert str to str
            string plain = get_string("plaintext:  ");
            printf("ciphertext: ");

            for (int j = 0, plain_len = strlen(plain); j < plain_len; j++) // iterate over each character of plaintext
            {
                if (isalpha(plain[j]) && isupper(plain[j])) // if its an uppercase
                {
                    plain[j] =
                    printf("%c", (((plain[j] - 65) + key) % 26) + 65);
                }
                else if (isalpha(plain[j]) && islower(plain[j])) // if its an lowercase
                {
                    printf("%c", (((plain[j] - 97) + key) % 26) + 97);
                }
                else
                {
                    printf("%c", plain[j]); // if its neither print that character
                }
            }
            printf("\n"); // newline
            return 0;
        }
        else
        {
            printf("Usage: ./caesar key\n"); // if argc isn't an number
            return 1;
        }
    }
    else
    {
        printf("Usage: ./caesar key\n"); // if there is more than 1 arguments
        return 1;
    }
}

string key_code(string key)
{
    for (int i = 65; i <= 90; i++)
    {
        key[i] = ;
    }
}