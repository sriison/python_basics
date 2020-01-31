n =23

for i in range(2, n):
    if i > 0:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print (i)

