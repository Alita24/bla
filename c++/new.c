#include <stdio.h>

void xxx(int *b)
{
    printf("b w xxx %d\n",*b);
    (*b)++;
    printf("nowe b w xxx %d\n",*b);
}

int main5(void)
{
    int a=6, *x;
    x=&a;
    printf("x=%p a=%d\n",x,a);
    *x=10;
    printf("nowe a=%d\n",a);
    xxx(x);
    printf("nowsze a=%d\n",a);
    return 0;
}
