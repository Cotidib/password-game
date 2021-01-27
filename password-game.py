password = "red"
guess = ""
guess_counter = 0
guess_limit = 5
out_of_guesses = False

def hint(guessnum):
    if guessnum == 1:
        print("Apples are...")
    elif guessnum == 2:
        print("Tomatoes are...")
    elif guessnum == 3:
      print("Roses are...")
    elif guessnum == 4:
        print("Think a color")
    elif guessnum == 5:
        print("Last try!") 

while guess != password and not(out_of_guesses):
    if guess_counter <= guess_limit:
        hint(guess_counter)
        guess = input("Enter password: ")
        guess_counter += 1     
    else:
        out_of_guesses = True
        

if out_of_guesses:
    print("Out of guesses")
else:
    print("You're in!")

 
        
