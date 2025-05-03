import string

def word_frequency_counter(text):
    text= text.lower()
    for punct in string.punctuation:
        text = text.replace(punct,"")
        words = text.split()
        frequency={} 
        for word in words:
            frequency[word] = frequency.get(word,0) + 1
    print(frequency,"end=")
text=input("enter the sentence or paragraph:")
word_frequency_counter(text)