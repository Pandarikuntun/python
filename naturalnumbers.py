def naturalnum(n):
    sum=0
    for i in range (1,n):
        print(i, end=",")
        sum+=i
    print("\n""sum of natural numbers:",sum)
n=int(input("enter the last number : "))
naturalnum(n)
