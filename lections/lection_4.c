#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; // to store the address of a variable n into a pointer p (ampersand & - get (extract) the address of (from) this variable)
    // asterisk * operator declares a variable as a pointer, as with int *p, indicating that we have a variable called p that points to an int
    printf("address of the n: %p\n", p); // %p is the format code to print an address
    printf("value of the n: %i\n", *p);// The * operator is also the dereference operator, which goes to an address to get the value stored there.

    char *s = "Hehehe"; // string s w/o cs50.h library
    printf("%s\n", s);

    char c = s[0];
    char *pc = &c;
    printf("address of the first character: %p\n", s);
    printf("address of the second character: %p\n", &s[1]);
    printf("address of the third character: %p\n", &s[2]);
    printf("address of the s: %p\n", pc);
}