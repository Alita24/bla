# 2.1
# dic={'hola':'hi','abrol':'tree','libro':'libookbro'}
# look=input("what word to find? ")
# for i,n in dic.items():
#     if look==i:
#         print("translate: ",n)

# 2.2
# yard={}
# i=''
# print(yard)
# while i!= 'end':
    
#     i=input('please give the text: ')
#     yard[i]=len(i)
# del yard['end']
# print(yard)

# 2.3
# dic={}
# word=input("please gimme word: ")
# pkt=0
# while word!= 'end':
#     for samo in 'aeiouy':
#         for s in word:
#             if s == samo:
#                 pkt+=1
#     dic[word]=pkt
#     pkt=0 
#     word=input("please gimme word: ")
# print(dic)

# 3.1
# text=input('the given text: ')
# dic={}

# 나의 form
# lister=text.split()
# for i in lister:
#     pkt=0
#     for k in lister:
#         if i == k:
#             pkt+=1
#     dic[i]=pkt
# print(dic)

# 아저씨의 favourite form
# for w in text.split():
#     dic[w]=dic.get(w,0)+1
# print(dic)



# 3.3
# lan=input('specify the language: ')
# if lan == 'eng':
#     for i in ['e','a','r','i','o']
#         text=input('the given text: ')
#         # lister=text.split()
#         dic={}
#         for i in text:
#             for k in lister:
#                 if i == k:
#                     pkt+=1
#             dic[i]=pkt

#         txt_rplce=text.replace()
#     print(dic)

import random
def draw (text):
    i= random.randint(0,len(text)-1)
    return text[i]
text = 'you will know when you see it up and personal in your space. and i remeber thinking, i am about to beat this bitch up, aw man i nearly dropped my crossunt'
print(draw(text))
