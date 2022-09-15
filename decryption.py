import numpy as np
with open('encrypted.txt') as f:
    p = f.read()
p=p.lower()
print("ciphertext file is read.")
k=input("Enter key for decryption: ")
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

ctext=[]
for i in p:
    #if(i!=" "):
        number=ord(i)-97
        ctext.append(number)
#print(ctext)

key=[]

for j in range(int(pt/ki)):
    for i in k:
        number=ord(i)-97
        key.append(number)

diff=pt%ki
for i in range(diff):
    key.append(ord(k[i])-97)   

# print(len(ctext))
# print(len(key))
# print(key)
# print(ctext)

vc=np.add(ctext,key)
output=[]
for i in range(len(vc)):
    if(vc[i]>=0):
        output.append((ctext[i]-key[i]+26)%26)
    else:
        output.append(vc[i])

# print(vc," in vignere cipher ")
# print(output," o/p after adding (ctext+key) mod 26 ")
ptext=[]
for i in range(len(key)):
    if(output[i]>=0):
        ptext.append(chr(output[i]+97))
    else:
        ptext.append(chr(32))
plain=''.join(ptext)
pltext=open('decrypted.txt','w')
pltext.write(plain)
#print("plaintext is ",plain)
print("Your ciphertext is converted to plain text. Please check decrypted.txt file.")
