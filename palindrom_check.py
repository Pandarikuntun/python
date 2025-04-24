def palindrom_check(word):
    normalized_word = word.lower()
    reversed_word = normalized_word[::-1]
    return normalized_word == reversed_word

word= input(" enter word: ")
if palindrom_check(word):
    print(f"{word} is palindrom")
    print("word length is: ",len(word))
else:
    print(f"{word } is not palindrom")


