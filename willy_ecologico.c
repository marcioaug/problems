#include <stdio.h>


int solution = -1;

int wood_collected(int *trees, int n, int height) {

    int i, collected = 0;

    for (i = 0; i < n; i++) {
        int over = trees[i] - height;

        if (over > 0) 
            collected += over;
    }

    return collected;
}

int is_solution(int *trees, int n, int height, int m) {

    int collected = wood_collected(trees, n, height);

    if (collected == m) 
        return 0;
    else if(collected > m) 
        return 1;
    
    return -1;
}

void binary_search(int *trees, int n, int b, int e, int m) {

    int status, i = -1, mid = (e + b) / 2;

    if (e >= b) {

        status = is_solution(trees, n, trees[mid], m);

        if (status == 0) {
            solution = trees[mid];
            return;
        } else if (status == 1) {
            if (solution == -1 || trees[mid] > solution)
                solution = trees[mid];

            binary_search(trees, n, (mid + 1), e, m);
        } else {
            binary_search(trees, n, b, (mid - 1), m); 
        }
    }

    return;
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

void merge_sort(int *A, int n) {
    if (n >= 2) {
        int m = n / 2;
        merge_sort(A, m);
        merge_sort(A + m, m + (n % 2));
        merge(A, n);
    }
}

int main(int argc, char **argv) {

    int n, m, i;

    scanf("%d %d\n", &n, &m);

    int trees[n];

    for (i = 0; i < n; i++) {
        scanf("%d ", &trees[i]);
    }

    merge_sort(trees, n);
    binary_search(trees, n, 0, (n - 1), m);

    printf("%d\n", solution);

    return 0;
}


