A = int(input())

if A % 2 == 0 :
    A /= 3
    print(int(A))

if A % 2 == 1 :
    A += 3
    if A % 3 == 0 :
        A /= 3
        print(int(A))
    else :
        print(int(A))
