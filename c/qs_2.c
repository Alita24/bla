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
int iteration(int a[],int i, int p, int n1)
{
    int j=i-1,s=0,n=7;
    printf("j:%d i:%d p:%d a[p]:%d n1:%d n:%d \n",j,i,p,a[p],n1,n);
    while(s<n1-1) //n1 amount of elements in a given section
    {
        printf("i:%d j:%d p:%d\n",i,j,p);
        if(compare(a,j,p)==1)
        {
            i--;
            change(a,j,i);
        }
        j--;
        print_arr(a,7);   
        
        s++;
    }
    //find place for the pivot
    
    if(i>=1 && p<n1)
    {
        printf("%d\n",i);
        i--;
        insert(a,i,p);
        printf("%d\n",i);
        print_arr(a,7); 
    }
    printf("j:%d i:%d p:%d a[p]:%d n1:%d\n",j,i,p,a[p],n1);
    printf("______________________\n");
    if ((p-j)==0)
    {
        //left side
        printf("$$$$$$$$$$$$ LEFT i:%d $$$$$$$$$$$$$$$\n",i);
        iteration(a,i,0,i);
        //right side
        printf("$$$$$$$$$$$$ RIGHT i:%d $$$$$$$$$$$$$$$\n",i);
        if(p!=n1)
            iteration(a,i,i+2,n-(i+1)); //the 7 and the 6 are nonmutable for this set of data. if you change the complete number of elements, these values will change accordingly i=n; j=n-1
    }
    return a;  
}
int main()
{
    int a[7]={11,4,2,1,17,13,6};
    int n=7,p=0;
    int i=n,s;
    print_arr(a,n);
    printf("..................\n");
    iteration(a,i,p,n);
    printf("THE ENDING ARRAY: ");
    print_arr(a,7);
    return 0 ;
    

}