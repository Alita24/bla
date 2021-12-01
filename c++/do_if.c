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

int main2()
{
    printf("number of numbers: ");
    int n = input_num(),num=0,i=0,x;
    if (n>0)
    {
        do
        {
            printf("next num ");
            x=input_num();
            num=num_sum(x,num);
        } while(++i<n);
        printf("sum equals: ");
        print_num(num);
    }
    else
    {
        printf("choose a positive number.");
    }
    return 0;
}
