#Making a guessing game program
secret_number = 23
guess_c = 0
guess_l = 3
game = input("You wanna to play a guessing game? ")
print ("Great! Guess a number 1 to 23. ")
while guess_c < guess_l:
    guess = int(input("Guess: "))
    guess_c += 1
    if guess == secret_number:
        print("You Won! ")
        break
else:
    print("You failed loser")