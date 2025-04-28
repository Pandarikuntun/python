def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10+sum_digits(num//10)
num=int(input("Enter the number: "))
print("sum of digits in number: ",sum_digits(num))
