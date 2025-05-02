def flames():
    name1=input("Enter your Name: ")
    name2=input("Enter the your crush Name: ")
    name1=name1.replace(" ","").lower()
    name2=name2.replace(" ","").lower()
    add=name1+name2
    result = "".join([letter for letter in add if add.count(letter) == 1])
    count=len(result)
    flames=["F","L","A","M","E","s"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames.pop()
    return flames[0]

result=flames()

if result == "F":
    print("bothe are good Frinds")
elif result == "L":
    print("your relationship is Love")
elif result == "A":
    print("you have only Affection")
elif result == "M":
    print("your relationship goes to Marriage")
elif result == "E":
    print("you both are Enemys")
else:
    print("your relationship Sister")
