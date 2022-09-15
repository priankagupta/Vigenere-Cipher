import numpy as np
with open('plaintext.txt') as f:
    p = f.read()
    p=p.lower()
print("plaintext file is read.")
k=input("Enter key for encryption: ")
pt=0
space=0
for i in p:
    #if(i!=" "):
        pt=pt+1   #count characters in plaintext
    #if(i==" "):
        #space=space+1
ki=0
for i in k:
    if(i!=" "):
        ki=ki+1  #count characters in key

plaintext=[]
for i in p:
    #if(i!=" "):
        number=ord(i)-97
        plaintext.append(number)
#print(plaintext)

key=[]

for j in range(int(pt/ki)):
    for i in k:
        number=ord(i)-97
        key.append(number)

diff=pt%ki
for i in range(diff):
    key.append(ord(k[i])-97)   

# print(len(plaintext))
# print(len(key))
# print(key)
# print(plaintext)

vc=np.add(plaintext,key)
output=[]
for i in vc:
    if(i>=0):
        output.append(i%26)
    else:
        output.append(i)

# print(vc," in vignere cipher ")
# print(output," o/p after adding (plaintext+key) mod 26 ")
ct=[]
for i in output:
    if(i>=0):
        ct.append(chr(i+97))
    else:
        ct.append(chr(32))
cipher=''.join(ct)
ciphertext=open('encrypted.txt','w')
ciphertext.write(cipher)
# for i in range(pt):
#     print(ciphertext[i])
#print("ciphertext is ",cipher)
print("Your plaintext is converted to cipher text. Please check ciphertxt.txt file.")

