#include <stdio.h>
void input_list(int a[], int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("number %d: ",i);
        scanf("%d",&a[i]);
    }
}
void print_list(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d ", a[i]);
}
int main4()
{
    int t[10],n;
    printf("number of positions: ");
    scanf("%d",&n);
    if (n>0)
    {
        input_list(t,n);
        print_list(t,n);
    }
    return 0;
}
