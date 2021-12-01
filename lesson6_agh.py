# 6.2
alphabet=input("provide me with the set of characters i'm supposed to use: ")
lower=['a','b'.'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet:
    hyphen=alphabet.find('-')


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

# step of 15
# decrpyt=''
# steps=15
# plaintext='vgpijajyt htgstrocxt soxpap sdqgot'
# for n in plaintext:
#     if n!=' ':
#         code=ord(n)

#         code_base=ord(n)-ord('a')

#         code_shift = (code_base-steps)%26

#         code_high=code_shift+ord('a')

#         new_code= chr(code_high)

#         decrpyt+= new_code
#     else:
#         decrpyt+=' '
# print("decrypt: ",decrpyt)