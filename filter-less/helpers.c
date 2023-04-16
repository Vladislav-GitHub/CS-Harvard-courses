#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float avg;
    int result;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avg = (float)(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            result = round(avg);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = result;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate colors
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
            image[i][j].rgbtRed = round(sepiaRed);

            // Red condition
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else if (sepiaRed == 0)
            {
                image[i][j].rgbtRed = 0;
            }

            // Green condition
            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else if (sepiaGreen == 0)
            {
                image[i][j].rgbtGreen = 0;
            }

            // Blue condition
            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else if (sepiaBlue == 0)
            {
                image[i][j].rgbtBlue = 0;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temp[3];

    // Swap cycle
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp[0] = image[i][j].rgbtRed;
            temp[1] = image[i][j].rgbtGreen;
            temp[2] = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;

            image[i][width - (j + 1)].rgbtRed = temp[0];
            image[i][width - (j + 1)].rgbtGreen = temp[1];
            image[i][width - (j + 1)].rgbtBlue = temp[2];
        }
    }
    return;
}

//Blur function
int blurfunc(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_position)
{
    float counter = 0;
    int sum = 0;

    // Call nested loops for the square's selections around each pixel
    for (int k = i - 1; k < (i + 2); k++)
    {
        for (int h = j - 1; h < (j + 2); h++)
        {
            if (k < 0 || h < 0 || k >= height || h >= width) // restrictions
            {
                continue;
            }
            if (color_position == 0)
            {
                sum += image[k][h].rgbtRed;
            }
            else if (color_position == 1)
            {
                sum += image[k][h].rgbtGreen;
            }
            else
            {
                sum += image[k][h].rgbtBlue;
            }
            counter++;
        }
    }
    return round(sum / counter); // return rounded average of each square of pixels
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Call Blur function
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = blurfunc(i, j, height, width, copy, 0);
            image[i][j].rgbtGreen = blurfunc(i, j, height, width, copy, 1);
            image[i][j].rgbtBlue = blurfunc(i, j, height, width, copy, 2);
        }
    }
    return;
}