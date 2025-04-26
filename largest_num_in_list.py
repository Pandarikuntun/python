# largest
def large(numbers):
    numbers.sort()
    return numbers[-1]
numbers=[10,20,13,0,45,25,62,4,8,21,4,48,24,5,5]
print("largest number in list: ",large(numbers))

# smallest
def small(numbers):
    return numbers[0]
print("Smallest number in list: ",small(numbers))

#second large
def second_large(numbers):
    return numbers[-2]
print("second largest number in list: ",second_large(numbers))

# sorted list assending order
def sortedlist(numbers):
    return numbers[0:]
print("arrenged list in assending order: ",sortedlist(numbers))

#sorted list dissending order
def sortedlist(numbers):
    return numbers[-1::-1]
print("arrenged list in disending order: ",sortedlist(numbers))