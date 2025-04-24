def repeted_leters(word):
    repeted={}
    for letter in set(word):
        count= word.count(letter)
        if count>1:
            repeted [letter] = count
    return repeted
try:
    word=input("enter the word: ")
    result=repeted_leters(word)
    if result:
        for letter,count in result.items():
            print(f"{letter} = {count}")
    else:
        print("no letter is repeted")


except KeyboardInterrupt:
    print("")