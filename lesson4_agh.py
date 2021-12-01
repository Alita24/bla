# 2.1
# string="asufbjewbasikhdk"
# print(string[::2])

# 2.2
# import random
# text=input("give me a text: ")
# position = random.randrange(len(text)-1)
# print(text[position])

# 3.1 upper > lower 
# text = 'Akdh Ajsdh DEUUB skjdh HJIKH'
# text2=''
# for i in text:
#     if i.islower():
#         text2+=i.upper()
#     else:
#         text2+=i.lower()
# print(text2)

# 3.2 the removal of sinterpunction
# text='ksdjhf, sdhjieb. Asduifkjh: seude ; leather()unehh isufh a::\\''aopp'
# for i in text:
#     for g in [',', ':', '.','(',')',';']:
#         if i == g:
#             text=text[:text.find(i)]+text[text.find(i)+1:]
# print(text)

# 4.1
# surnames=['kowalski','smith','gawron','olszewska','bond','jones','lawrence','pitt','jolie','park','kim']
# given_name=input("please provide me with a surname: ")
# if given_name in surnames:
#     print('looks like your welcome to the party!')
# else:
#     print('try again or get the hell outta here')

# 4.2
# sentence=input("hit me with a excruciatingly long sentencs: ")
# words=sentence.split()
# for i in words:
#     print('wrd ',i, 'has',len(i),'words')

# some kind of cipher, prolly cesears
# norm=input("the text please: ").lower()
# codeList=[]
# step=3
# ciphered=''
# for i in norm:
#     code=ord(i)-97
#     code+=step
#     code = code%25
#     print(code)
#     code+=97
#     ciphered+=chr(code)
#     print(ciphered)
# print(ciphered)
# deciphered=''
# for n in ciphered:
#     code=ord(i)-97
#     code-=step
#     code = code%25
#     print(code)
#     code+=97
#     deciphered+=chr(code)
#     print(deciphered)
# print(deciphered)

# 6.1 'e' in the text
# text=input("the text: ")
# count=0
# blanks=0
# for i in text:
#     if i in ['e','E']:
#         count+=1
#     if i == ' ':
#         blanks+=1
# length=len(text)-blanks
# percent=round((count/length)*100,2)
# print('there are',count,'many instances of "e". that makes up',percent,"percent of all the letters")

# 6.2 kinda doesn't work
# norm=input("the text please: ").lower()
# codeList=[]
# step=[2,3,5]
# ciphered=''
# steps=0

# for i in norm:
#     code=ord(i)
#     code+=step[steps]
#     # print(code)
#     code = code%122
#     ciphered+=chr(code)
#     steps+=1
#     steps=steps%3
#     # print(steps)
# print(ciphered)

# steps=0
# deciphered=''

# for n in ciphered:
#     # print(code)
#     code=ord(n)
#     # print(code)
#     code=code - step[steps]
#     # print(code)
#     code = code%122
#     deciphered+=chr(code)
#     steps+=1
#     steps=steps%3
#     # print(steps)
# print(deciphered) 


# unicode practice 
# so i kinda looked on the internet for this one sorry-not-sorry
# a='a'
# b='B'
# text='aWAiasj-90.AS,jsk'
# encryption = ""
# shift=
# for c in text:

#     # check if character is an uppercase letter
#     if c.isupper():

#         # find the position in 0-25
#         c_unicode = ord(c)

#         c_index = ord(c) - ord("A")

#         # perform the shift
#         new_index = (c_index + shift) % 26

#         # convert to new character
#         new_unicode = new_index + ord("A")

#         new_character = chr(new_unicode)

#         # append to encrypted string
#         encryption = encryption + new_character
#     elif c.islower():
#         c_unicode = ord(c)
#         c_index = ord(c) - ord("a")
#         new_index = (c_index + shift) % 26
#         new_unicode = new_index + ord("a")
#         new_character = chr(new_unicode)
#         encryption = encryption + new_character
#     else:
#         encryption+=c

# print("Plain text:",text)

# print("Encrypted text:",encryption)       
# plaintext=''
# for i in encryption:
#     if i.isupper():
#         i_unicode = ord(i)
#         i_index = ord(i) - ord("A")
#         new_index = (i_index - shift) % 26
#         new_unicode = new_index + ord("A")
#         new_character = chr(new_unicode)
#         plaintext+=new_character
#     elif i.islower():
#         i_unicode = ord(i)
#         i_index = ord(i) - ord("a")
#         new_index = (i_index - shift) % 26
#         new_unicode = new_index + ord("a")
#         new_character = chr(new_unicode)
#         plaintext+=new_character
#     else:
#         plaintext+=i
# print('decription text:',plaintext)

# 6.3
# a='a'
# b='B'
# text='ArgD2aadSS5.;hs'
# encryption = ""
# shift=[2,3,5]
# steps=0
# for c in text:

#     # check if character is an uppercase letter
#     if c.isupper():

#         # find the position in 0-25
#         c_unicode = ord(c)

#         c_index = ord(c) - ord("A")

#         # perform the shift
#         new_index = (c_index + shift[steps]) % 26

#         # convert to new character
#         new_unicode = new_index + ord("A")

#         new_character = chr(new_unicode)
        
#         # append to encrypted string
#         encryption = encryption + new_character
#     elif c.islower():
#         c_unicode = ord(c)
#         c_index = ord(c) - ord("a")
#         new_index = (c_index + shift[steps]) % 26
#         new_unicode = new_index + ord("a")
#         new_character = chr(new_unicode)
#         encryption = encryption + new_character
#     elif c.isnumeric():
#         c_unicode = ord(c)
#         c_index = ord(c) - ord("0")
#         new_index = (c_index + shift[steps]) % 10
#         new_unicode = new_index + ord("0")
#         new_character = chr(new_unicode)
#         encryption = encryption + new_character
#     else:
#         encryption+=c
#     steps+=1
#     steps%=3

# print("Plain text:",text)

# print("Encrypted text:",encryption)       
# plaintext=''
# steps=0
# for i in encryption:
#     if i.isupper():
#         i_unicode = ord(i)
#         i_index = ord(i) - ord("A")
#         new_index = (i_index - shift[steps]) % 26
#         new_unicode = new_index + ord("A")
#         new_character = chr(new_unicode)
#         plaintext+=new_character
#     elif i.islower():
#         i_unicode = ord(i)
#         i_index = ord(i) - ord("a")
#         new_index = (i_index - shift[steps]) % 26
#         new_unicode = new_index + ord("a")
#         new_character = chr(new_unicode)
#         plaintext+=new_character
#     elif i.isnumeric():
#         i_unicode = ord(i)
#         i_index = ord(i) - ord("0")
#         new_index = (i_index - shift[steps]) % 10
#         new_unicode = new_index + ord("0")
#         new_character = chr(new_unicode)
#         plaintext = plaintext + new_character
#     else:
#         plaintext+=i
#     steps+=1
#     steps%=3
# print('decription text:',plaintext)


# 6.2
# text='akshda'
# steps=[2,3,5]
# plaintext=''
# faze=0
# for i in text:
#     code=ord(i)

#     code_base=ord(i)-ord('a')

#     code_shift = (code_base+steps[faze])%26

#     code_high=code_shift+ord('a')

#     new_code= chr(code_high)

#     plaintext+= new_code
#     faze=(faze+1)%3

# print('text: ',text)
# print("crypt: ",plaintext)
# decrpyt=''
# faze=0
# for n in plaintext:
#     code=ord(n)

#     code_base=ord(n)-ord('a')

#     code_shift = (code_base-steps[faze])%26

#     code_high=code_shift+ord('a')

#     new_code= chr(code_high)

#     decrpyt+= new_code
#     faze=(faze+1)%3
# print("decrypt: ",decrpyt)