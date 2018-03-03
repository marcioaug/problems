#include <stdio.h>

long int count = 0;

void merge(int *A, int n) {

    int *b, *m, i;
    int sorted[n];
    int rest = (n / 2);

    b = &A[0];
    m = &A[n / 2];

    for (i = 0; i < n; i++) {
        if ((*b <= *m && b != &A[n / 2]) || m == &A[n]) {
            sorted[i] = *b;
            b = b + 1;
            rest--;
        } else if (m != &A[n]) {
            sorted[i] = *m;
            m = m + 1;
            if (b != &A[n / 2])
                count += rest;
        }
    }

    for (i = 0; i < n; i++) {
        A[i] = sorted[i];
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


int main() {
    
    int i, n_test_cases;

    scanf("%d\n", &n_test_cases);
        
    for (i = 0; i < n_test_cases; i++) {
        int j, n;
    
        scanf("%d\n", &n);

        int arr[n];
               
        for (j = 0; j < n; j++) {
            scanf("%d\n", &arr[j]);
        }

        merge_sort(arr, n);
        
        printf("%ld\n", count);
        count = 0;
    }

	return 0;
}