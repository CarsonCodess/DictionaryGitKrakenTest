import time

def add(addWord, addDefinition): #Adds a word along with a definition to the dictionary.txt file.

    with open("dictionary.txt", "a") as dictionaryFile:
        dictionaryFile.write(str(addWord) + ", " + str(addDefinition) + "\n")

    main()

def read(): #Reads the entire dictionary.txt file to the user.

    with open("dictionary.txt", "r") as dictionaryFile:
        print(dictionaryFile.read())

    main()

def remove(removeWord): #Removes a word from the dictionary.txt file.

    with open("dictionary.txt", "r") as dictionaryFile:
        lines = dictionaryFile.readlines()

    with open("dictionary.txt", "w") as dictionaryFile:
        for line in lines:
            if removeWord not in line[0:line.index(",")]:
                dictionaryFile.write(line)

    main()

def check(checkWord): #Reads a word the user wants a definition for from the dictionary.txt file.

    with open("dictionary.txt", "r") as dictionaryFile:
        lines = dictionaryFile.readlines()

        for line in lines:
            if checkWord in line:
                print(line)

    main()


def main(): #Main file, mostly does the user input.

    userInput = input("Would you like to add, remove, check, read, or exit the dictionary?")

    if(userInput == "exit"):
        exit()

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

    elif (userInput == "check"):
        word = input("Enter the word: ")
        confirm = input(f"To confirm, you would like to check the word \"{word}\"? (y/n)")

        if(confirm == "y"):
            check(word)

        elif(confirm == "n"):
            print("Okay.")
            time.sleep(3)
            main()

    elif (userInput == "read"):
        read()

    else:
        print("Invalid Choice!")
        main()

main()