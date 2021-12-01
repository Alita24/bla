#include <stdio.h>

int main1() 
{
    // Write C code here
    int n=0,i,sum=0,a=0;
    float sum_float;
    printf("number of numbers: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("next element: ");
        scanf("%d",&a);
        sum+=a;
    }
    sum_float=(float)sum/n;
    printf("the float %f",sum_float);
    
    return 0;
}