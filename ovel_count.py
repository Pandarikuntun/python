def count_vowels(string):
    vowels = "aeiou"
    string = string.lower() 
    string = string.replace(" ","") 
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a word or sentence: ")
print("Number of vowels:", count_vowels(string))

def count_consonants(string):
    b=len(string)
    a=b-count_vowels(string)
    return a
print("number of consonents: ",count_consonants(string))