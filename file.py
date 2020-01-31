import os
# file = open("srini.txt",'r')
# file.write("forth line added\n")
# file.write("fifth line added\n")
# file.close()

file = open("srini.txt","r+")
str = file.read()
print (str[0])
file.close()
os.remove("srini.txt")

