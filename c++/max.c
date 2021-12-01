#include <stdio.h>
int input_num(void)
{
    int x;
    printf("next number: ");
    scanf("%d",&x);
    return x;
}

int main4()
{
    int n, max,i=0,a,min;
    printf("number of numbers: ");
    scanf("%d",&n);
    printf("%d",a);
    max=input_num();
    min=max;
    for(;i<n-1;i++)
    {
        a=input_num();
        if(a>max)
            max=a;
        if (a<min)
            min=a;

    }
      
    printf("max of this group is: %d\n", max);
    printf("min of this group is: %d\n", min);
    return 0;
}
