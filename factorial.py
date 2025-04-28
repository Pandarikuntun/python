def factorial(num):
    for i in range(1,num+1):
        if num==0 or num==1:
            return 1
        else:
            return num*factorial(num-1)
num = int(input("enter the number: "))
print(f"factorial of {num} is {factorial(num)}")