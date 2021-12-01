#include <stdio.h>
#include <stdlib.h>

 int main()
 {
    int a[10][10], ***b,r,c,i,j;
    r=8;
    c=5;
    b=malloc(sizeof(int **)*r);
    for(i=0;i<r;i++)
    {
        b[i]=malloc(sizeof(int *)*c);
    }
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            b[i][j]=&a[i][j];
        }
    }
    // for(i=0;i<r;i++)
    // {
    //     for(j=0;j<c;j++)
    //     {
    //         printf("%d ",a[i][j]);
    //     }
    //     printf("\n");
    // }

    // for(i=0;i<r;i++)
    // {
    //     for(j=0;j<c;j++)
    //     {
    //         printf("var : %p\n",&a[i][j]);
    //         printf("t_pointer: %p\n",b[i][j]);
    //     }
    // }
    
    printf("random variable: %d with adress %p\n",a[5][2],&a[5][2]);
    printf("POINTER\n");
    printf("random variable: %d with adress %p\n",*b[5][2],b[5][2]);
 }
