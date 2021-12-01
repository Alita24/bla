
//sdkjgfhalisydflaksufaksgdfalswgdfilasudflasigudflaisdef

 #include <stdio.h>
 #include <stdlib.h>
 typedef void funkcja(char  *, unsigned);
 typedef struct p
 {
     char *name;
     unsigned age;
     funkcja *w;
     struct p *n;
 }pies;

 void wite_out (char *c, unsigned n)
 {
     printf("%s %u\n", c,n);
 }

 void add_dog(pies *some_dog,
              char *name, unsigned age,
              funkcja *f)
          {
              some_dog->name=name;
              some_dog->age=age;
              some_dog->w=f;
              some_dog->n=NULL;
          }
 void write_list(pies *s) // s wskaznik do pierwszego elementu listy wow Ala robi komentarze wow posz³a moim œladem hhaha
 {
     while(s)
     {
         s->w(s->name,s->age);
         s=s->n;
     }
 }
 int take_age(pies *s)
 {
     s=s->age;
     return s;
 }
 void add_dog_list(pies **start_list,
                   char *name,
                   unsigned age,
                   unsigned position) // position place where the new dog will be added
 {
     pies *new_dog,*some_dog=*start_list;
     new_dog=(pies *)malloc(sizeof(pies));
     add_dog(new_dog,name,age,wite_out);
     if(!position)
     {
         new_dog->n=*start_list; //n is the next dog
         *start_list=new_dog;
     }
     else
     {
         position--;
         while(some_dog->n && position)
         {
             some_dog=some_dog->n;
             position--;
         }
         new_dog->n=some_dog->n;
         some_dog->n=new_dog;
     }

 }
 int delete_dog(pies **s,unsigned position)
 {
     pies *whatevs, *current_list;
     current_list=*s;
     if(position==1)
     {
         *s=(*s)->n;
     }
     else
     {
         position--;
         while(current_list->n && (position-2)>0)
         {
             current_list=current_list->n;
             position--;
         }
         whatevs=current_list;
         while(current_list->n && position)
         {
             current_list=current_list->n;
             position--;
         }
         whatevs->n=current_list;
     }
     *s=current_list;
     return *s;
 }
 int main(void)
 {
     int i;
     char *names[7]={"serduszko","kwiatuszek","sloneczko","zappka","whatevs","whomeves","whatevs"};
     unsigned ages[7]={90,13,11,2021,234,233,235};
     pies *moj_psy, *new_dog;
     for(i=0;i<7;i++)
     {
         if(!i)
         {
             new_dog = (pies *)malloc(sizeof(pies));
             moj_psy=new_dog;
         }
         else
         {
             new_dog->n=(pies *)malloc(sizeof(pies)); //pole zawierajace adres psa
             new_dog=new_dog->n;
         }
         add_dog(new_dog,names[i],ages[i],wite_out);
     }
     free(new_dog);
     write_list(moj_psy);
     int position,smallest=12023790,age,j;
     pies *posortowane_psy,*maly_pies,*moje_psy;
     for(j=7;j>0;j--)
     {
         moje_psy=moj_psy;
         for(i=0;i<j;i++)
         {
             age=take_age(moje_psy);
             if(age<smallest)
             {
                 maly_pies=moje_psy;
                 smallest=age;
                 position=i;
             }
             moje_psy=moje_psy->n;
             printf("%d\n", smallest);
         }
         if(j==7)
         {
             new_dog = (pies *)malloc(sizeof(pies));
             posortowane_psy=new_dog;
         }
         else
         {
             new_dog->n=(pies *)malloc(sizeof(pies)); //pole zawierajace adres psa
             new_dog=new_dog->n;
         }
         add_dog(posortowane_psy,"yol",43,wite_out);
         smallest=129;
         write_list(posortowane_psy);
         moj_psy=delete_dog(&moj_psy,position);
         write_list(moj_psy);
     }
     // write_list(posortowane_psy);





     return 0;
 }
