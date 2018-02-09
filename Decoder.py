#Name:Krishna Sreenivas Student ID-800984436

import os
import sys #library needed to accept cmd line arguments
bits=int(sys.argv[2]) #to accept bits in cmd line
file=sys.argv[1]#to accept file name in cmd line
encoded_string =[]
table = {}

#checking if file exists and copying the contents onto an array. 
#else printing an error.  
if os.path.exists(file):
    f=open(file, 'r') 
    code = f.read().split()
    f.close()
    k=0
    while (k>=0 and k<len(code)):
        encode_prep=code[k]+code[k+1]
        encoded_string.append(int(encode_prep,2))
        k=k+2
else:
    print("File does not exists!")
    exit(0)

#building up table containing 256 Ascii characters
j=0
while (j>=0 and j<256):
    table[j]=chr(j)
    j=j+1

#Decoding module.
max_size=pow(2,bits)#table size
string = table[encoded_string.pop(0)]#popping the code of first encoded string into a list
final_string=[string]

i=0
while i<len(encoded_string):
    code=encoded_string[i]#copying encoded strings into a variable in each iteration
    if code not in table:
        new_string = string+string[0]#new characters are concatenated with previous string
    else:
        new_string=table[code]
    final_string.append(new_string)#decoded strings are appended to a final list
    if len(table)<max_size:
        table[len(table)]=string+new_string[0]
    else:
        print("Need more bits to represent data")
        exit
    string=new_string
    i=i+1

decoded_text=''.join(final_string) #converting list to string
print("Decoding is completed. Please check the <input file>_decoded.txt file")

#writing the decoded string to a file
f=open(file[:-4]+'_decoded.txt', 'w')
f.write(decoded_text)
f.close()