n = int(input())
r = int(str(n)[::-1])

if int(str(n*n)[::-1]) == r*r:
    print("Adam number")
else:
    print("Not Adam number")
