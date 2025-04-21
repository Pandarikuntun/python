def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i ==0:
            return False
    return True
num=int(input("enter last number in series: "))
sum=0
for i in range (2,num+1):
    if prime(i):
        print(i,end=",")
        sum +=i
print("\n""sum of series :",sum)
