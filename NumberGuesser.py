from random import randint

random_number = randint(1, 10)

number_of_guesses = 0
user_guess = 0

while user_guess != random_number:
	user_guess = int(input("Guess a number between 1 and 10: "))
	number_of_guesses += 1

	if user_guess == random_number:
		print("Congratulations! You guessed the number!")
		break
	elif number_of_guesses == 3:
		print("Sorry, you ran out of guesses. The number was " + str(random_number))
		break
	else:
		print("Sorry, try again!")