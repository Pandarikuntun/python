def anagram():
    first=input()
    second=input()
    first=first.lower()
    second=second.lower()
    first=sorted(first)
    second=sorted(second)
    if first==second:
        print("Anagrams")
    else:
        print("not anagrams")
anagram()