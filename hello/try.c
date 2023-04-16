#include <stdio.h>
#include <cs50.h>

void hash(int l);//prototype

    //Prompt user for height
int get_height(void)
{
    int n;
    do
    {
        n = get_int("Choose height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

        int main(void)
        {
          //Pyramid's cycle
          int h = get_height();
          int i;
          for (i = 1; i < (h + 1); i++)
          {
              for (int j = 0; j < (2 * h) - 1; j++)
              {
                  if (j == (h - i) || j == (h + 2))
                  {
                      hash(i);
                  }
                  else if (j == h || j == (h + 1))
                  {
                      printf(" ");
                  }
                  else
                  {
                      printf(" ");
                  }
              }
              printf("\n");
          }
        }
        
            //Hash # function
            void hash(int l)
            {
                for (int k = 0; k < l; k++)
                {
                printf("#");
                }
            }