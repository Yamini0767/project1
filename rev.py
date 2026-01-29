'''write a program to  reverse number '''

def reverse(num):
    rev=0
    while num>0:
        rev =rev*10+num%10
        num//=10
    return rev

def isPalidrome(num):
    return num==reverse(num)

print(reverse(143))
print(isPalidrome(1236))
print(isPalidrome(1239))
>>>>>>> 5d48e51262b90b3294f7dcbb9aa871c06080b986
print(reverse(121))
print(isPalidrome(121))

print("yamini")


