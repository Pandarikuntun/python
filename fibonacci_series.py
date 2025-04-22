def fibonacci_series(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=",")
        a,b=b,a+b
    print()
n=int(input("enter the last number of series: "))
fibonacci_series(n)