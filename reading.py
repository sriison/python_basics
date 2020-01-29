
f=open("srini.txt", "a")
f.write("\n writing few more new lines to a file")
f.close()
f=open("srini.txt", "r")
print(f.read())

