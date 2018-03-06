#include <stdio.h>


int binary_search_lower_bound(int *A, int b, int e, int q) {

    int m = (e + b) / 2, i = m;

    if (A[0] > q)
        return -1;

    if (e > b)
        if (A[m] == q) 
            i = m;
        else if (A[m] > q)
            i = binary_search_lower_bound(A, b, (m - 1), q);  
        else 
            i = binary_search_lower_bound(A, (m + 1), e, q);

    if (A[i] > q) 
        i--;    

    return i;
}


int main(int argc, char **argv) {

    int A[11] = {-20, -10, 0, 10, 20, 30, 40, 50};

    printf("%d\n", binary_search_lower_bound(A, 0, 7, -21) == -1);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -20) == 0);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -19) == 0);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -18) == 0);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -11) == 0);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -10) == 1);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -9) == 1);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, -1) == 1);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 0) == 2);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 1) == 2);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 9) == 2);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 10) == 3);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 11) == 3);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 15) == 3);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 19) == 3);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 20) == 4);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 21) == 4);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 29) == 4);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 30) == 5);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 31) == 5);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 39) == 5);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 40) == 6);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 41) == 6);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 49) == 6);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 50) == 7);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 51) == 7);
    printf("%d\n", binary_search_lower_bound(A, 0, 7, 60) == 7);


    return 0;
}