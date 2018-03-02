#include <stdio.h>


int binary_search(int *A, int b, int e, int q) {

    int i = -1, m = (e + b) / 2;

    if (e >= b)
        if (A[m] == q) 
            i = m;
        else if (A[m] > q)
            i = binary_search(A, b, (m - 1), q);  
        else 
            i = binary_search(A, (m + 1), e, q);
    

    return i;
}


int main(int argc, char **argv) {

    int A[11] = {-20, -10, 0, 10, 20, 30, 40, 50};

    printf("%d\n", binary_search(A, 0, 7, 50));


    return 0;
}