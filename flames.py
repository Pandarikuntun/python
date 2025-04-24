def flemes():
    name1=input()
    name2=input()
    name1=name1.replace(" ","").lower()
    name2=name2.replace(" ","").lower()
    letters=list(name1+name2)
    for letter in set(name1):
        if letter in name2:
            letters.remove(letter)
            letters.remove(letter)
            count=0
            for letter in letters:
                count+=1
            print(count)
flemes()

