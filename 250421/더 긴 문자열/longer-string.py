a, b = map(str, input().split())

c = len(a) ; d = len(b)

if c > d :
    print(a, c)
elif c == d :
    print("same")
else :
    print(b, d)



