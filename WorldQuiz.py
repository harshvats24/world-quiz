print("\nHello Player! Welcome to the World Quiz.\nYou'll be asked random questions upon world cities, history and geography.\nYou need to give one-word answer. \n")

userInput = input("Shall we start? \n").lower()
if userInput!="yes":
    print("\nBye. See you later.")
    quit()
else:
    print("\nAwesome! Let's start...")

correctStr = 'Correct'
incorrectStr = 'Incorrect'
score = 0

userInput = input("\nWhat's the capital of Australia? \n").lower()
if userInput == 'canberra':
    print(correctStr)
    score += 1
else:
    print(incorrectStr)

userInput = input("\nWhat's the continent of Spain? \n").lower()
if userInput == 'europe':
    print(correctStr)
    score += 1
else:
    print(incorrectStr)

userInput = input("\nWhich river is the longest river in the world? \n").lower()
if userInput == 'nile':
    print(correctStr)
    score += 1
else:
    print(incorrectStr)

userInput = input("\nName the hot desert found in India. \n").lower()
if userInput == 'thar':
    print(correctStr)
    score += 1
else:
    print(incorrectStr)

userInput = input("\nWhich is the uninhabitated continent in the world? \n").lower()
if userInput == 'antarctica':
    print(correctStr)
    score += 1
else:
    print(incorrectStr)

print(f"\nYou have got {score} out of 5 answers right.\n")
if score<3:
    print("\nYou should try again.")
