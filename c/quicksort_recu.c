#include<stdio.h>
#include<stdlib.h>
#include <time.h>


int compare(int a[],int j,int p)
{
    if(a[p]<a[j])
        return 1;
    else 
        return 0;
    
}
int change (int a[],int j, int i)
{
        int c;
        c=a[j];
        a[j]=a[i];
        a[i]=c;
    return a;
}
int insert(int a[], int i,int p)
{
    // printf("INSERT p:%d i:%d\n",p,i);
    int c;
    c=a[p];
    a[p]=a[i];
    a[i]=c;
    return a;
}
void print_arr(int a[], int n)
{
    int l;
    printf("[");
    for(l=0;l<n;l++)
        printf("%d,",a[l]);
    printf("]\n"); 
}
int iteration(int a[],int i,int j, int p, int n1,int s, int n)
{
    s=0;
    printf("j:%d i:%d p:%d a[p]:%d n1:%d n:%d \n",j,i,p,a[p],n1,n);
    
    while(s<n1-1)
    {
        printf("i:%d j:%d p:%d\n",i,j,p);
        if(compare(a,j,p)==1)
        {
            i--;
            change(a,j,i);
        }
        j--;
        print_arr(a,9);   
        
        s++;
    }
    //find place for the pivot
    
    if(i>=1 && p<n1)
    {
        printf("%d\n",i);
        i--;
        insert(a,i,p);
        printf("%d\n",i);
        print_arr(a,9); 
    }
    printf("j:%d i:%d p:%d a[p]:%d n1:%d\n",j,i,p,a[p],n1);
    printf("______________________\n");
    if ((p-j)==0)
    {
        //left side
        printf("$$$$$$$$$$$$ LEFT p:%d $$$$$$$$$$$$$$$\n",p);
        iteration(a,i,i-1,0,i,0,n);
        //right side
        printf("$$$$$$$$$$$$ RIGHT p:%d $$$$$$$$$$$$$$$\n",p);
        if(p!=n1)
            iteration(a,9,8,i+2,n-(i+1),0,n); //the 7 and the 6 are nonmutable for this set of data. if you change the complete number of elements, these values will change accordingly i=n; j=n-1
    }
    return a;  
}
int main()
{
    int a[9]={20,15,3,8,6,0,13,4,18};
    int n=9;
    int p=0;
    int i=n,j=n-1;
    int l,s;
    print_arr(a,n);
    printf("..................\n");
    printf("THE ENDING ARRAY: ");
    iteration(a,i,j,p,n,s,n);
    print_arr(a,9);
    return 0 ;
    

}