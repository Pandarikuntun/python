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
    print("Frinds")
elif result == "L":
    print("Love")
elif result == "A":
    print("Affection")
elif result == "M":
    print("Marriage")
elif result == "E":
    print("Enemy")
else:
    print("Sister")
