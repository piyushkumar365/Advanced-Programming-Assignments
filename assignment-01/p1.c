// TIME COMPLEXITY ANAKYSIS OF ANY SUITALBE ALGORITHMS IN C. VARY INPUT RISES AND CHECK TRENDS.
// IN LINEAR , LOGARITHMIC, QUADRATIC

#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int linear(int a[],int n,int x)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(a[i]==x)
        {
            printf("found");
            return 1;
        }
    }
    return 0;
}

int selection_sort(int a[],int n)
{
    int i,j,min;

    for(i=0;i<n-1;i++)
    {
        min = i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[min])
            {
                min = j;
            }
        }
        int temp = a[i];
        a[i] = a[min];
        a[min] = temp;

    }
    return 1;
}

int binary(int a[],int n,int x)
{
    int low = 0;
    int high = n-1;
    int mid;

    while(low<=high)
    {
        mid = low+(high-low)/2;

        if(a[mid]==x)
        {
            printf("found");
            return mid;
        }

        else if(a[mid]<x)
            low = mid+1;
        else
            high = mid-1;
    }
    return 1;
    
}


int main()
{

clock_t start,end;
int n,i,*a;
double cpu_time;

/*
printf("Enter size of array in linear search : ");
scanf("%d",&n);

printf("enter values in array : ");

for(i = 0;i<n;i++)
{
    scanf("%d",&a[i]);
}
*/
    // ********************

    n = 20000;   // DO NOT use large n with selection sort
    a = (int*)malloc(n * sizeof(int));

    if(a == NULL)
    {
        printf("Memory allocation failed\n");
        return 0;
    }

    srand(time(NULL));

    for(int i=0;i<n;i++)
        a[i] = rand() % 100000;

        // **************

int x;
printf("Enter value of x to be search : ");
scanf("%d",&x);


start = clock();
linear(a,n,x);
end = clock();

cpu_time = ((double)(end-start))/CLOCKS_PER_SEC;
printf("Time taken by linear search : %lf\n",cpu_time);

start = clock();
selection_sort(a,n);
end = clock();

cpu_time = ((double)(end-start))/CLOCKS_PER_SEC;
printf("Time taken by selection sort : %lf\n",cpu_time);

/* Array is now sorted, binary search can be performed */
start = clock();
binary(a,n,x);
end = clock();

cpu_time = ((double)(end-start))/CLOCKS_PER_SEC;
printf("Time taken by binary search : %lf\n",cpu_time);




    return 0;
}