#include <stdio.h>
#include <stdlib.h>
int m_add(int **b, int **d,int j,int c, int l, int i, int r1)
{
    int m=0,var=0;
    for(m=0;m<c;m++)
        {
            var=var+b[j][m]*d[l][i];
            l=(l+1)%(r1+1);
        }
    return var;
}

int main()
 {
    int **b,**d,**w,r,c,r1,c1,i,j,l ,m,var=0;
    printf("ile wierszy chcesz miec w macierzy a. ");
    scanf("%d", &r);
    printf("ile kolumn chcesz miec w macierzy a. ");
    scanf("%d", &c);
    b=malloc(sizeof(int *)*r);
    for(i=0;i<r;i++)
    {
        b[i]=malloc(sizeof(int)*c);
    }
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("number %d:%d ",i,j);
            scanf("%d", &b[i][j]);
        }
    }
    for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                printf("%d ", b[i][j]);
            }
            printf("\n");
        }
    printf("ile wierszy chcesz miec w macierzy b. ");
    scanf("%d", &r1);
    printf("ile kolumn chcesz miec w macierzy b. ");
    scanf("%d", &c1);
    d=malloc(sizeof(int *)*r1);
    for(i=0;i<r1;i++)
    {
        d[i]=malloc(sizeof(int)*c1);
    }
    for(i=0;i<r1;i++)
    {
        for(j=0;j<c1;j++)
        {
            printf("number %d:%d ",i,j);
            scanf("%d", &d[i][j]);
        }
    }
    for(i=0;i<r1;i++)
        {
            for(j=0;j<c1;j++)
            {
                printf("%d ", d[i][j]);
            }
            printf("\n");
        }
    if(c!=r1)
    {
        printf("not a valid input");
        return 0;
    }
    w=malloc(sizeof(int *)*r);
    for(i=0;i<r;i++)
    {
        w[i]=malloc(sizeof(int)*c1);
    }

    j=0;
    i=0;
    l=0;

    for(j=0;j<r;j++)
    {
        for(i=0;i<c1;i++)
          {
              w[j][i]=m_add(b,d,j,c,l,i,r1);
              printf("wynik %d:%d %d\n",j,i,w[j][i]);
              l=0;
          }
    }
    for(i=0;i<r;i++)
    {
        for(j=0;j<c1;j++)
        {
            printf("%d ",w[i][j]);
        }
        printf("\n");
    }


 }