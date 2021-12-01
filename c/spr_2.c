#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int **t,i,j,c,s;
    time_t o;
    srand((unsigned) time(&o));
    scanf("%d", &c);
    scanf("%d", &s); /* wiersze, rows*/
    int ***w;
    t=malloc(c*sizeof(int *));
    for(i=0;i<c;i++)
    {
        t[i]=malloc(sizeof(float)*s);
        for(j=0;j<s;j++)
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
        w[i]=malloc(sizeof(int *)*s);
        for(j=0;j<s;j++)
        {
            w[i][j]=&t[i][j];
        }
    }
    // db
    float small=t[0][0];
    int *position=&t[0][0];
    for(i=0;i<c;i++)
    {
        for(j=0;j<s;j++)
        {
            if (small> t[i][j])
            {
                small=t[i][j];
                position =&t[i][j];
            }
        }
    }
    printf("the smallest element in this array is %f, with the address of %p\n", small ,&position);
    //bdb
    int count;
    for(i=0;i<c;i++)
    {
        if(i%2==0)
        {
            position=&t[i][0];
            int cp=0,c,tmp;
            
            for(c=0;c<s;c++)
            {
                count=0;
                small=t[i][cp];
                for(j=cp;j<s;j++)
                {
                    if (small>t[i][j])
                    {
                        small=t[i][j];
                        position =&t[i][j];
                        count+=1;
                    }
                }
                if(count==0)
                    {
                        cp++;
                        continue;
                        
                    }
                else
                    {
                        tmp=t[i][cp];
                        *position=tmp;
                        t[i][cp]=small;
                        cp++;
                    }
            }
            for(j=0;j<s;j++)
            {
                printf("%d ",t[i][j]);
            }
            printf("\n");
        }
        else
        {
            int big;
            position=&t[i][0];
            int cp=0,c,tmp;
            for(c=0;c<s;c++)
            {
                big=t[i][cp];
                count=0;
                for(j=cp;j<s;j++)
                {
                    
                    if (big<t[i][j])
                    {
                        big=t[i][j];
                        position =&t[i][j];
                        count+=1;
                    }
                }
                if(count==0)
                {
                    cp++;
                    continue;
                }
                else
                {
                    tmp=t[i][cp];
                    *position=tmp;
                    t[i][cp]=big;
                    cp++;
                }
    
                
            }
            
            for(j=0;j<s;j++)
                {
                    printf("%d ",t[i][j]);
                }
            printf("\n");
        }  
    }
    // cel
    int **r,a;
    printf("define a: ");
    scanf("%d", &a);
    r=malloc(c*sizeof(int *));
    for(i=0;i<c;i++)
    {
        r[i]=malloc(sizeof(float)*s);
        for(j=0;j<s;j++)
        {
            r[i][j]=t[i][j]/a;
            printf("%d ",r[i][j]);
        }
        printf("\n");
    }
}