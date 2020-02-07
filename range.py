for i in range(50,100):
    if i > 10:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)

