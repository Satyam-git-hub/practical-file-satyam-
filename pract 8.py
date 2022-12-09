n=input("type a character")
if n.isalpha():
    print("it is a letter")
    if n.isupper():
        print("Letter is upper case")
    elif n.islower():
        print("Letter is lower case")
elif n.isdigit():
    from num2words import num2words
    num2words(n)
    print("It is a digit")
else:
    print("it is a special character")
