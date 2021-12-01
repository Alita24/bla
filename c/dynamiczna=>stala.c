#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int x[10][10],**y,k,m,i,j;
    k=5;
    m=7;
    y=(int **)calloc(k,sizeof(int *));
    for(i=0;i<k;i++)
    {
        y[i]=(int *)calloc(m,sizeof(int));
        for(j=0;j<m;j++)
        {
            x[i][j]=i+1;
        }
    }
    for(i=0;i<k;i++)
    {
        for(j=0;j<m;j++)
        {
            y[i][j]=&x[i][j];
        }
    }
    for(i=0;i<k;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%d:%d: elementu: %d \n",i,j,*(y+i+j));
        }
        printf("\n");
    }
    for(i=0;i<k;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%d:%d: pozycja elementu: %p ",i,j,&x[i][j]);
            printf("ojok: %p \n",y[i][j]);
        }
        printf("\n");
    }
    printf("%d \n",&y[2][5]);
    printf("%d ",x[2][5]);
    return 0;
}
