// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <cs50.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = (LENGTH + 1) * 'z';

// Hash table
int total_words = 0;
node *table[N]; // [node1, node2, new_node, ... nodeN]
                //                   |
                //                new_node2

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // get the hash index
    int index = hash(word);

    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for(int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return (sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen("dictionary", "r");
    if (file == NULL)
    {
        return false;
    }

    // read 1 word at a time
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        // create a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }

        // copy to the new_node
        strcpy(new_node->word, word);
        new_node->next = NULL;

        // hash word to a number index
        int index = hash(word);
        if (table[index] == NULL)
        {
            table[index] = new_node;
        }
        else
        {
            new_node->next = table[index];
            table[index] = new_node;
        }
        total_words++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Free the linked list
    for(int i = 0; i < N; i++)
    {
        node *head = table[i];
        node *cursor = head;
        node *tmp = head;

        while(cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}