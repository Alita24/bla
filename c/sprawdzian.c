#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int **t,i,j,c,r;
    time_t o;
    srand((unsigned) time(&o));
    scanf("%d", &c);
    scanf("%d", &r);
    int ***w;
    t=malloc(c*sizeof(int *));
    for(i=0;i<c;i++)
    {
        t[i]=malloc(sizeof(float)*r);
        for(j=0;j<r;j++)
        {
            t[i][j]=rand()%30;
            printf("%d ",t[i][j]);
        }
        printf("\n");
    }
    // dst
    w=&t;
    w=(int ***)calloc(c,sizeof(int **));
    for(i=0;i<c;i++)
    {
        w[i]=malloc(sizeof(int *)*r);
        for(j=0;j<r;j++)
        {
            w[i][j]=&t[i][j];
        }
    }
    // db
    float small=t[0][0];
    int *position=&t[0][0];
    for(i=0;i<c;i++)
    {
        for(j=0;j<r;j++)
        {
            if (small> t[i][j])
            {
                small=t[i][j];
                position =&t[i][j];
            }
        }
    }
    printf("the smallest element in this array is %f, with the address of %p\n", small ,&position);
     
    for(i=0;i<c;i++)
    {
        if(i%2==0)
        {
            position=&t[i][0];
            int cp=0,c,tmp;
            for(c=0;c<r;c++)
            {
                small=t[i][cp];
                for(j=cp;j<r;j++)
                {
                    if (small>t[i][j])
                    {
                        small=t[i][j];
                        position =&t[i][j];
                    }
                }
                tmp=t[i][cp];
                *position=tmp;
                t[i][cp]=small;
                
    
                cp++;
            }
            for(j=0;j<r;j++)
                {
                    printf("%d ",t[i][j]);
                }
            printf("\n");
        }
        else
        {
            {
                int big;
                position=&t[i][0];
                int cp=0,c,tmp;
                for(c=0;c<r;c++)
                {
                    big=t[i][cp];
                    for(j=cp;j<r;j++)
                    {
                        if (big<t[i][j])
                        {
                            big=t[i][j];
                            position =&t[i][j];
                        }
                    }
                    tmp=t[i][cp];
                    *position=tmp;
                    t[i][cp]=big;
                    
        
                    cp++;
                }
            
            for(j=0;j<r;j++)
                {
                    printf("%d ",t[i][j]);
                }
            printf("\n");
        }  
        }
    }
}