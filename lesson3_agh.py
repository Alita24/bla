
# 5.1 even or odd number
# num=int(input("give me a number, i'll tell you whether its even or odd: "))
# if num%2 == 0:
#     print("it's even :)")
# else:
#     print("it's odd :(")

# 5.2
# import random
# selected_num= random.randrange(0,100)
# guess = int(input("try to guess what number was selected: "))
# print("if you want to end type 'end' without apostrofies")

# one_shot
# if guess == selected_num:
#     print("aren't you a lucky chap")
# else:
#     print("the chances of you winning, are quickly decreasing")

# LESS-HARD-VERSION with the 'end' function
# while guess != "end":
#     if int(guess) > selected_num:
#         print("too much")
#         guess = input("try to guess what number was selected: ")
#     elif int(guess) < selected_num:
#         print("too little")
#         guess = input("try to guess what number was selected: ")
#     elif int(guess) == selected_num:
#         print("look at you... you did it!")
#         break

# SUPER-HARD-VERSION (with from next line)
# while guess != selected_num:
#     print("good luck next time")
#     guess = input("try to guess what number was selected: ")

# 5.3
# import math
# num=int(input("provide me with a number, if it's possisble, i'll reciprocate you with the square root "))
# if num < 0:
#     print("don't try to mess with me honey.")
# else:
#     print("the square root is",math.sqrt(num))
#     # you_could_replace the math thingy with 'num**(1/2)' and it'll work the same

# 6.1
# for i in range(0,100):
#     print(i,"squared is",i**2)

# 6.2
# already_did_that in the 5.2 the SUPER-HARD-VERSION

# 6.3 99-bottle song
# for i in range(100,2,-1):
#     print("",i,"bottles of beer on the wall,\n",i,"bottles of beer!\n Take one down,\n Pass it around,\n",i-1,"bottles of beer on the wall!\n")
# i=i-1
# if i == 2:
#     print("",i,"bottles of beer on the wall,\n",i,"bottles of beer!\n Take one down,\n Pass it around,\n",i-1,"bottle of beer on the wall!\n")
#     i=i-1
# if i ==1:
#     print("",i,"bottle of beer on the wall,\n",i,"bottle of beer!\n Take one down,\n Pass it around,\n No more bottles of beer on the wall!\n")

# 6.4 grade average
# num=float(input("insert the grade you, may or may have not, acquired: "))
# average=0
# total_ammount=0
# while num!= -1:
#     average+=num
#     total_ammount+=1
#     num=float(input("insert the grade you, may or may have not, acquired: "))
# average=average/total_ammount
# print(average)

# 7.1 leap year
# start=int(input("start date: "))
# finish=int(input("end date: "))
# for i in range(start,finish+1):
#     if i%100 == 0:
#         if i%400 == 0:
#             print(i,"yeap it's a leap year")
#         else:
#             print(i,"no way, it's just a normal year")
#     else:
#         if i%4 == 0:
#             print(i,"LEAP YEAR!!!!")
#         else:
#             print(i,"you thought, it was. well it ain't")

# 7.2 machine russian-roulette guess
# import random
# num=int(input("give me a number, i'll try to guess it:" ))
# loop=1
# guess=random.randrange(0,100)
# while guess != num:
#     loop+=1
#     guess=random.randrange(0,100)
# print(guess,"is your number. i've found it in",loop,"tries")

# 7.3 average_tries machine russian-roulette guess
# import random
# num1=int(input("give me a number, i'll try to guess it:" ))
# loop1=1
# guess=random.randrange(0,100)
# while guess != num1:
#     loop1+=1
#     guess=random.randrange(0,100)

# num2=int(input("give me a number, i'll try to guess it:" ))
# loop2=1
# guess=random.randrange(0,100)
# while guess != num2:
#     loop2+=1
#     guess=random.randrange(0,100)

# num3=int(input("give me a number, i'll try to guess it:" ))
# loop3=1
# guess=random.randrange(0,100)
# while guess != num3:
#     loop3+=1
#     guess=random.randrange(0,100)

# average=(loop1+loop2+loop3)/3
# print("the average number of tries is",average)

# 7.4 fibbonachi number - to the 1000th
# num1=0
# num2=1
# print(num2)
# for i in range(0,999):
#     num3=num1+num2
#     print(num3)
#     num1=num2
#     num2=num3