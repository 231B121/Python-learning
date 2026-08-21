n = int(input("Enter a number: "))
def bro(n):
    if n == 1:
        return 1
    return n * bro(n-1)
    

print(bro(n))