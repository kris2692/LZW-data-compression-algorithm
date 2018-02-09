#Name:Krishna Sreenivas Student ID-800984436

import os
from numpy import binary_repr #library needed for binary representation
import sys #library needed to accept cmd line arguments
string = ""
final_code = []
table={}
encoded_string=''
bits=int(sys.argv[2])#to accept bits in cmd line
file=sys.argv[1]#to accept file name in cmd line

#reading file and copying text to an list
if os.path.getsize(file)>0:
    f=open(file, 'r')
    text = f.read()
    f.close()
else:
    print("File is empty!")
    exit(0)

#building up table containing 256 Ascii characters
j=0
while (j>=0 and j<256):
    table[chr(j)]=j
    j=j+1

#encoding code
max_size=pow(2,bits)#table size
i=0
while i<len(text):
    symbol = string+text[i]
    if symbol in table:
        string = symbol
    else:
        if len(table)<max_size:
            final_code = final_code + [table[string]]#encoding characters by looking in table.
        else:
            print("Need more bits to represent data")
            exit
        table[symbol]=len(table)#adding new strings in the table
        string = text[i]
    i=i+1

#appending encoded code of last character to the final list
if True:
    final_code = final_code + [table[string]]
    
#print statement to indicate encoding status
print("Encoding is completed. Please check the <input file>.lzw file")

#code to represent encoded codes of strings in 16 bit binary format with spaces in between
i=0
while i<len(final_code):
    test=binary_repr(final_code[i],16)
    encoded_string=encoded_string+" "+test[0:8]+" "+test[8:]
    i=i+1
encoded_string=encoded_string[1:]

#to write the binary representation of codes to .lzw file
f=open(file[:-4]+'.lzw', 'w')
f.write(encoded_string)
f.close()