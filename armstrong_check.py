def armstrong_check(num):
    sum = 0
    temp = num  
    while temp > 0:
        r = temp % 10
        sum += r ** 3  
        temp //= 10
    return sum  

num = int(input("Enter the number: "))
if armstrong_check(num) == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")