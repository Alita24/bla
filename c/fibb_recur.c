#include<stdio.h>
#include<stdlib.h>


//#1
// int fib(int n)
//     {
//         if(!n)
//             return 0;
//         else if (n==1 || n==2)
//         {
//             return 1;
//         }
//         else
//             return fib(n-1)+fib(n-2);
//     }

//#2
int fib(int n)
    {
        if (n>=3)
            return fib(n-1)+fib(n-2);
        else
            return 1;
    }
int main()
{
    int n;
    n=13;
    printf("isdfh %d\n",fib(n));
    return 0; 
    
}