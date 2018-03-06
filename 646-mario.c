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

    int n, l;

    scanf("%d %d\n", &n, &l);
    
    while (n != 0 || l != 0) {
        int i, last_locker, changes, min_changes = -1, empty_lockers[l];

        for (i = 0; i < l; i++) {
            scanf("%d ", &empty_lockers[i]);
        }

        for (i = 0; i < l; i++) {
            last_locker = binary_search_lower_bound(empty_lockers, 0, l, (empty_lockers[i] + n - 1));
            
            if (last_locker != -1) {
                changes = last_locker - i;

                if (min_changes == -1 || min_changes > changes) 
                    min_changes = changes;
            }

            printf("> %d %d\n", last_locker, min_changes);
        }

        printf("%d\n", min_changes);
        scanf("%d %d\n", &n, &l);
    }

    return 0;
}