# generate fibonacchi series

def fibo():
    a,b = 0,1
    while True:
        yield a        # generator function
        a,b = b,a+b   # formula

fs = fibo()
n = int(input("generate series upto: "))
for i in range (n):
    print(next(fs))


# using Recursion.

def rec_fibo(n):
    if n<=1:
        return n
    else:
        return(rec_fibo(n-1)+rec_fibo(n-2))

upto = int(input("Enter  the number of terms you want to display :"))
print ("Fibonacci Series is:")
if  upto <= 0:
    print("Please enter a positive integer")
else:
    for i in range(upto):
        print(rec_fibo(i))
        