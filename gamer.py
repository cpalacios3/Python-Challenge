def game():
  max_guess = 9
  attempt = 0
  number = 18
  guess = int(input("Guess: "))
    
  while number != guess:
    attempt += 1
    guess = int(input("Repeat Guess: "))
    if guess == number:
        print (f"You Won. It took you {attempt} tries.")
        break
    elif attempt == max_guess:
        print("Out of guesses")
        break
    elif guess > 100 or guess < 1:
        print('You have chosen a number out of play')
    elif guess > number:
        print ("Wrong. You chose a number greater than the secret number")
    elif guess < number:
        print('Wrong. You chose a number less than the secret number')