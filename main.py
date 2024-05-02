import time

def add(addWord, addDefinition):
    dictionaryFile = open("dictionary.txt", "a")
    dictionaryFile.write("{" + str(addWord) + ", " + str(addDefinition) + "} ")

def read():
    dictionaryFile = open("dictionary.txt", "r")
    print(dictionaryFile.read())

def remove(removeWord):
    dictionaryFile = open("dictionary.txt", "r+")
    readFile = dictionaryFile.read()
    wordIndex = readFile.index(str(removeWord))
    endBracketIndex = (readFile[wordIndex:]).index("}")
    dictionaryFile.write(readFile[0: wordIndex-1] + readFile[endBracketIndex:])

def main():
    userInput = ""
    while(userInput != "exit"):
        userInput = input("Would you like to add, remove, check, read, or exit the dictionary?")
        if(userInput == "exit"):
            break
        elif (userInput == "add"):
            word = input("Enter the word: ")
            definition = input("Enter the definition: ")
            confirm = input(f"To confirm, you would like to add the word \"{word}\", with the definition \"{definition}\"? (y/n)")
            if(confirm == "y"):
                add(word, definition)
            elif(confirm == "n"):
                print("Okay.")
                time.sleep(3)
                main()
        elif (userInput == "remove"):
            word = input("Enter the word: ")
            confirm = input(f"To confirm, you would like to remove the word \"{word}\"? (y/n)")
            if(confirm == "y"):
                remove(word)
            elif(confirm == "n"):
                print("Okay.")
                time.sleep(3)
                main()
            remove(word)
        elif (userInput == "check"):
            print("Check")
        elif (userInput == "read"):
            read()
        else:
            print("Invalid Choice!")

main()