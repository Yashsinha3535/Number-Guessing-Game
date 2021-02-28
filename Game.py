#Modules
import random

#Information to user
print("Guess the number between 1 to 100")

#Number range
Number = random.randint(1,100)
#Default Trie when game starts
Tries = 1
#Done default to false
Done = False

#When user has not guessed the number
while not Done:
    #Enter the number
    guess = int(input("Enter your guess:"))
    #If guess is equal then Done is equal to true and if not true increase tries and then compare guess by number and tells us if number is smaller than the guess or greater
    if guess == Number:
        print(Number,"is the number")
        Done = True
    else:
        Tries += 1
        if guess > Number:
            print("Your guess is smaller than the number")
        if guess < Number:
            print("Your guess is greater than the number")

#When done then print this statement
if Done:
  print(Tries,"Tries were taken to win")


#When done this stament will print at last and when enter is pressed, console will close
print("Press enter to close now...")
input()


