N = int(input())

for i in range (N) :
    for j in range (N-i) :
        print("*",end="")

    for j in range (2*i) :
        print(" ",end="")

    for j in range (N-i) :
        print("*",end="")
    print()