# generate fibonacchi series

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

res = fibo()
n = int(input("Enter  the number you want to display :"))
for i in range (n):
    print(next(res))


# using Recursion.

def rec_fibo(n):
    if n<=1:
        return n
    else:
        return(rec_fibo(n-1)+rec_fibo(n-2))

enter = int(input("Enter  the number of terms you want to display :"))
print ("Fibonacci Series is:")
if  enter <= 0:
    print("Please enter a positive integer")
else:
    for i in range(enter):
        print(rec_fibo(i))

def simple_fibo(n):
    if n <= 1:
        return n
    else:
        return simple_fibo(n - 1) + simple_fibo(n - 2)


for i in range(8):
    print(simple_fibo(i))