N = int(input())

for _ in range (N, 101) :
    if N >= 90 :
        print("A", end=" ")
    elif N >= 80 :
        print("B", end=" ")
    elif N >= 70 :
        print("C", end=" ")
    elif N >= 60 :
        print("D", end=" ")
    else :
        print("F", end=" ")
    N += 1