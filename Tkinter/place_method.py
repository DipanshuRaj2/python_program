n = int(input())


def result(n):
    a = 1
    for i in str(n):
        a = a * int(i)
    return a
        

b = result



if b<=25:
    print(b)
else:
    print("invalid")