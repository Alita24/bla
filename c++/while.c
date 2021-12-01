#include <stdio.h>
int input_num(void)
{
    int x;
    scanf("%d",&x);
    return x;
}
int num_sum(int a,int b)
{
    return(a+b);
}
void print_num (int a)
{
    printf("%d",a);
}


int main6()
{
    printf("number of numbers: ");
    int n = input_num(),num=0,i=0,x;
    while(i<n)
    {
        printf("next num ");
        x=input_num();
        num=num_sum(x,num);
        i++;
    }
    printf("sum equals: %d\n",num);
    return 0;
}
