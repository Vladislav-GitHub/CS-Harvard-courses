#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

bool only_digits(string text), k;
char rotate(char letter, int n);
string ciphertext, plaintext;
int l, key;

int main(int argc, string argv[])//argc - number of words that your user types as a prompt, argv[] - vetor - variable in an array,
// that stores all these strings, which user types
{
    bool c = only_digits(argv[1]);

    // Make sure program was run with just one command-line argument && make sure every character in argv[1] is a digit
    if (argc == 2 && c != 0)
    {
        // Convert argv[1] (key) from a `string` to an `int`
        key = atoi(argv[1]);
        printf("key: %i\n", key);
        // Prompt user for plaintext
        plaintext = get_string("plaintext:  \n");

        // For each character in the plaintext:
        printf("ciphertext: ");
        for (int i = 0; plaintext[i] != '\0'; ++i)
        {
            // Rotate the character if it's a letter
            ciphertext[i] = rotate (plaintext[i], key);
            printf("%c", ciphertext[i]);
            ciphertext[i] = 0;
        }
        return 0;
    }
    else if (argc != 2 || c == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

    //Check digits, if digit => c = 1 (true), if NOT digit => c = 0 (false)
    bool only_digits(string text)
    {
        for (int i = 0; i < strlen(text); i++)
        {
            if (isdigit(text[i]))
            {
                k = 1;
            }
            else
            {
                k = 0;
            }
        }
        return k;
    }

    char rotate(char letter, int n)// plaintext[], key
    {
        if (isalpha(letter))//A = 65
        {
            if (isupper(letter))//+
            {
                letter = (int) letter - 65;//A = 0
                printf("letter: %i\n", letter);
                if (letter >= 26)//no
                {
                    letter = (letter + n) % 26;
                }
                //yes (A = 0 < 26)
                letter = (char) (letter + 65);// 65 = A
            }
            else if (islower(letter))
            {
                letter = (int) letter - 97;//a = 0
                printf("letter: %i\n", letter);
                if (letter >= 26)//no
                {
                    letter = (letter + n) % 26;
                }
                //yes (a = 0 < 26)
                letter = (char) (letter + 97);// 97 = a
            }
        }
        else// is not alphabet
        {
            return letter;
        }
        return letter;
    }