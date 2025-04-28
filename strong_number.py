def strong_number():
    n=input("enter number: ")
    sum=0
    for i in n:
        fact =1
        for j in range(1,int(i)+1):
            fact=fact*j
        sum=sum+fact
    if sum==int(n):
        print("strong number")
    else:
        print("not strong number")
strong_number()