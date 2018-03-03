#include <stdio.h>


int main() {
    
    int i, n_test_cases;

    scanf("%d\n", &n_test_cases);
    
    
    for (i = 0; i < n_test_cases; i++) {
        int j, n, count = 0;
        printf("-> %d", n_test_cases);
        scanf("%d\n", &n);

        int arr[n];
        
        scanf("%d\n", &arr[0]);
        
        for (j = 1; j < n; j++) {
            scanf("%d\n", &arr[j]);
            int key = arr[j];
            int k = j - 1;
            
            while (k >= 0 && arr[k] > arr[k + 1]) {
                arr[k + 1] = arr[k];
                arr[k] = key;
                k--;
                count++;
            }
        }
        
        printf("%d\n", count);
    }

	return 0;
}