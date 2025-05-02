def duplicate():
    b=int(input("enter the number of elements in list to add:"))
    list=[]
    n=(input("enter elements "))
    for i in range(b-1):
        a = input("")
        if a not in list:
         list.append(a)
    print(f"here the list {list}")
    
duplicate()
