#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * main - Entry point
 * Description: Assigns a random signed number to a variable and
 * prints the last digit of that number.
 * Return: Always 0 (Success)
 */
int main(void)
{
    int number;

    srand(time(0));
    number = rand() - RAND_MAX / 2;

    printf("Last digit of %d is %d and is ", number, abs(number % 10));

    if (abs(number % 10) > 5)
        printf("greater than 5\n");
    else if (abs(number % 10) == 0)
        printf("0\n");
    else
        printf("less than 6 and not 0\n");

    return (0);
}
