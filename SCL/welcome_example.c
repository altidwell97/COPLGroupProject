#include "scl.h"
#include <stdio.h>

int main(){
    double x;
    printf("Welcome to the world of SCL");
    // Can also use puts(). Puts can't do strings and variables though so printf
    // for consistency. Printf also does not automatically do a newline.
    x = 45.95;
    printf("Value of x: %f", x);

    return 0;
}