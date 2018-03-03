#include <stdio.h>

void printa(int *A, int n) {
    int i;

    for (i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
     
    printf("\n");
}

void merge(int *A, int n) {

    int *b, *m, i;
    int sorted[n];

    b = &A[0];
    m = &A[n / 2];

    for (i = 0; i < n; i++) {
        if ((*b <= *m && b != &A[n / 2]) || m == &A[n]) {
            sorted[i] = *b;
            b = b + 1;
        } else if (m != &A[n]) {
            sorted[i] = *m;
            m = m + 1;
        }
    }

    for (i = 0; i < n; i++) {
        A[i] = sorted[i];
    }
}

void merge_2(int *A, int n) {
    int mid = n / 2;
    int L[mid], R[n - mid], i, l = 0, r = 0;

    for(i = 0; i < n; i++) {
        if (i < mid) {
            L[i] = A[i];
        } else {
            R[i - mid] = A[i];
        }
    }

    for (i = 0; i < n; i++) {
        if ((L[l] <= R[r] && l < mid) || (r == (n - mid))) {
            A[i] = L[l++];
        } else {
            A[i] = R[r++];
        }
    }
}

void merge_sort(int *A, int n) {
    if (n >= 2) {
        int m = n / 2;
        merge_sort(A, m);
        merge_sort(A + m, m + (n % 2));
        merge(A, n);
    }
}

int main(int argc, char **argv) {

    int MAX_SIZE = 8;
    int A[MAX_SIZE], sorted[MAX_SIZE];
    int i, *b, *m;

    for (i = 0; i < MAX_SIZE; i++) {
        scanf("%d/n", &A[i]);
    }

    merge_sort(A, MAX_SIZE);
    printa(A, MAX_SIZE);
    printf("count: %d\n", 10000000);

    return 0;
}