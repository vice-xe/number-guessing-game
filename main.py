# Program for Number Guessing Game # 

import random

# Choose the Difficulty Level

while True:
   
   difficulty = input("Choose Difficulty(easy,medimum,hard)").strip().lower()

   if difficulty == "easy":
      maximum = 50
      break
   elif difficulty =="medimum":
      maximum = 100
      break
   elif difficulty =="hard":
      maximum = 500
      break
   else:
      print("Invalid difficulty")
   
play_again = "yes" 

# Ask the User to Play Again

while play_again == "yes":

    secret = random.randint(1,maximum)

    attempt = 0

    # Restrict the Game to 7 Attempts

    while attempt < 7:

        # Ask the user to guess the Number 
                      
        try:
           given = int(input(f"Enter a number between 1 and {maximum}:"))
        except ValueError:
           print("Please enter a number!")
           continue

        # Count how many guesses it took
                              
        attempt += 1

        # Tell the User if the Guess is Too High, Too Low, or Correct
                       
        if ( secret == given):
            print("Correct")
            break
        elif abs(secret - given) <= 5:
           print("Very Close")
        elif( secret > given):
            print("Too Low")
        else:
            print("Too High")
                          
    print("Number of Attempt", attempt)

    # Print whether the User Won or Lost

    if ( secret == given):
     print("You Won")
    else:
     print("You Lost")

    # Ask the User if they want to Play Again
    
    play_again = input("Do you want to play again? (yes/no):").strip().lower()