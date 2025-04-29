def automorphic_number():
    n = input("enter number: ")
    square = int(n)**2
    if str(square).endswith(str(n)):
        print("automorphic number")
    else:
        print("not automorphic number")
automorphic_number()

