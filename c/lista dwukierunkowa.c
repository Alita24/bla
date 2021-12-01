#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct x
{
    int w;
    struct x *p; //pointer to previous element
    struct x *n; //pointer to next element
} element;

void add(element **adr)
{
    element *l;
    l=(element *)malloc(sizeof(element));
    if(adr)
    {
        l->w=rand()%10;
        l->n=NULL;
        l->p=NULL;
        if(!(*adr))
        {
            *adr=l;
        }
        else
        {
            while((*adr)->n)
                *adr=(*adr)->n;
            (*adr)->n=l;
            l->p=(*adr);
            while((*adr)->p)
                *adr=(*adr)->p;
        }
    }
}

void write(element *adr)
{
    printf(">>>>>>>>>>>>\n");
    while(adr)
    {
        printf("%d\n",adr->w);
        adr=adr->n; //address of next element
    }
     printf(">>>>>>>>>>>>\n");
}

void rev_write(element *adr)
{
    printf("<<<<<<<<<<<<\n");
    while(adr->n) adr=adr->n;
    while(adr)
    {
        printf("%d\n",adr->w);
        adr=adr->p;
    }
    printf("<<<<<<<<<<<<\n");
}

void wstaw(element **adr,int position)
{
    element *l;
    l=(element *)malloc(sizeof(element));
    if(l)
    {
        l->w=rand()%10;
        l->n=NULL;
        l->p=NULL;
        if(!position) //if position is 0
        {
            l->n=*adr;
            (*adr)->p=l;
            *adr=l;
        }
        else
        {
            while((*adr)->n && position) 
            {
                (*adr)=(*adr)->n;
                position--;
            }
            if(!p)
            {
                l->n = (*adr);
                (*adr)->p->n=l;
                l->p=(*adr)->p;
                (*adr)->p=l;
            }
            else
            {
                (*adr)->n=l;
                l->p=(*adr);
            }
            while((*adr)->p) (*adr)=(*adr)->p;
        }
    }


}
int main(void)
{
    element *u=NULL;
    int i;
    srand(time(NULL));
    for(i=0;i<5;i++)
    {
        add(&u); //address of variable which contains the first element of list
    }
    write(u);
    rev_write(u);
    wstaw(&u,3);
    write(u);
    return 0;
}
