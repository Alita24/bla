 //https://blog.etrapez.pl/macierze-odwrotne-liczone-metoda-gaussa-jordana/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int **a, **b, c=4,l,i,dziel,rzad;
    //define macierz do odwrocenia
    srand(2);
    a=malloc(sizeof(int *)*(c*2));
    for(l=0;l<c;l++)
    {
        a[l]=malloc(sizeof(float)*(c*2));
        for(i=0;i<c;i++)
        {
            a[l][i]=rand()%20;
            printf("%d ", a[l][i]);
        }
    //define macierz jednostkowa
        for(i=c;i<(c*2);i++)
        {
            if ((l+c)==i)
            {
                a[l][i]=1;
            }
            else
            {
                a[l][i]=0;
            }
            printf("%d ", a[l][i]);
        }
        printf("\n");
    }
}

