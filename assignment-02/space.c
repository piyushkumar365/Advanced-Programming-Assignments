#include <stdio.h>
#include <stdlib.h>

// find max in array

int constantSpaceSum(int arr[], int n, size_t *auxMem) {
    int max = arr[0];
    int i;

    *auxMem = sizeof(int) + sizeof(int);  // max + i

    for (i = 1; i < n; i++) {
        if (arr[i] > max)
            max = arr[i];
    }

    return max;
}

// calculating prefix sum

int linearSpaceCopy(int arr[], int n, size_t *auxMem) {
   int *prefix = (int *)malloc(n * sizeof(int));               
    if (!prefix) return -1;

    prefix[0] = arr[0];

    for (int i = 1; i < n; i++)
        prefix[i] = prefix[i - 1] + arr[i];

    *auxMem = n * sizeof(int);      // new prefix array

    int result = prefix[n - 1];

    free(prefix);
    return result;
}

// creating 2d matrix in with single pointer

int quadraticSpaceMatrix(int n, size_t *auxMem) {
    int *matrix = (int *)malloc(n * n * sizeof(int));
    if (!matrix) return -1;

    *auxMem = n * n * sizeof(int);      // new memory storing n*n elements

    int count = 0;

    for (int i = 0; i < n * n; i++)
        matrix[i] = count++;

    free(matrix);
    return count;
}

int main() {
    int n = 10000;
    int *arr;
    size_t auxMem;

    arr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        arr[i] = i;

    printf("Constant Space Result: %d\n",
           constantSpaceSum(arr, n, &auxMem));
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Auxiliary Space Complexity: O(1)\n\n");

    printf("Linear Space Result: %d\n",
           linearSpaceCopy(arr, n, &auxMem));
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Auxiliary Space Complexity: O(n)\n\n");

    quadraticSpaceMatrix(1000, &auxMem);
    printf("Quadratic Space Done (n = 1000)\n");
    printf("Auxiliary Memory Used: %zu bytes\n", auxMem);
    printf("Auxiliary Space Complexity: O(n^2)\n");

    free(arr);
    return 0;
}