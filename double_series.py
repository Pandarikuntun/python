def double_series(n):
    first=0
    second=1
    for _ in range (n):
        print(first)
        first=second
        second=first+second
n=int(input("enter the last number in series:"))
double_series(n)