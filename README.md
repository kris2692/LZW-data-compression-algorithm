# LZW-data-compression-algorithm
Encoder and Decoder module of LZW algorithm realized using Python.

# Programming language used: Python 3.6.0

# Requirements:
NumPy has to be installed on the system. Since the code makes use of binary_repr().

# Command to install NumPy:
pip install numpy 
Data Structure used for table construction is of type Dict(dictionary).

# Encoding module:
1) The file name and bits required are passed as command line arguments.
2) An initial table of 256 characters is constructed using chr() function. Subsequent new strings are added to the table in the end.
3) Contents present in the file are copied in an string, if the size is greater than 0. Which is then passed to the encoding module.
4) The resultant codes are stored in 16 bit binary format by stripping first 2 characters (0b which is default for binary in python) through binary_repr(), which is then written into a file with .lzw extension.

# Execution command:
Enter the below command in command prompt.
python Encoder.py <file_name.txt> <bits>

# Decoding module:
1) An initial table of 256 characters is built in reverse manner, where the codes refer to the characters.
2) Binary codes are copied from a file which is supplied in command line onto an string if the file exists.
3) These binary codes are returned to their original table representation by removing spaces in between.
4) This is then passed onto a decoding module where the resultant string is stored in an string variable before being written to a file.

# Execution command:
Enter the below command in command prompt.
python Decoder.py <file_name.lzw> <bits>

# Files:
Contains 3 files
Encoder.py
Decoder.py
README.docx

# Issues:
1) No validation present to check the type of files being provided as arguments.
2) Encoding and Decoding mechanisms will not work if number of bits is less.
3) If the text is huge, then number of bits should be more.
