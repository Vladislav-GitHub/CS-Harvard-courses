#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // exclude invalid number of arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r"); // open file
    if (file == NULL)
    {
        fclose(file);
        printf("file open operation error\n");
        return 2;
    }

    typedef uint8_t BYTE; // declaration of byte's type
    BYTE buffer[512];
    char *filename = malloc(sizeof(char) * 8); // allocate memory for string
    int counter = 0;

    // FILE img
    sprintf(filename, "%03i.jpg", counter);
    FILE *img = fopen(filename, "w"); // img - output file

    // exclude file's open error
    if (img == NULL)
    {
        fclose(img);
        printf("image open operation error\n");
        return 3;
    }

    while (fread(buffer, sizeof(BYTE), 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (counter == 0)
            {
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), 512, img);
                counter += 1;
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), 512, img);
                counter += 1;
            }
        }
        else
        {
            if (counter != 0)
            {
                fwrite(buffer, sizeof(BYTE), 512, img);
            }
        }
    }
    fclose(file);
    fclose(img);
}