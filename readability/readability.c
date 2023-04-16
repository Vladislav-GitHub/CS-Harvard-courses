#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//Prototypes
int count_letters(string text), count_words(string text), count_sentences(string text);

int sum = 0, sentences = 0, words = 1;//initial conditions
float L, S;

int main(void)
{
    //Prompt user for text
    string book = get_string("Text: ");

    //Coleman-Liau index
    float l = count_letters(book);
    float w = count_words(book);
    float s = count_sentences(book);
    L = 100 * (l / w);//letters per 100 words
    S = 100 * (s / w);//sentences per 100 words
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);

    //Check grades
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

//Count letters in text
int count_letters(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (((int)text[i] >= 65 && (int)text[i] <= 90) || ((int)text[i] >= 97 && (int)text[i] <= 122))
        {
            sum++;
        }
    }
    return sum;
}

//Count words in text
int count_words(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }
    return words;
}

//Count sentences in text
int count_sentences(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}