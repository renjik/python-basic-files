word = input("enter the word:")
if (word[0].isupper()):
    print("the word is uppercase")
elif (word.islower()):
    print("the word is lowercase")
elif (word.isdigit()):
    print("the word is digit",word)