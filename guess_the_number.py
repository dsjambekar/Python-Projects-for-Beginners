import random
num = random.randint(1, 100);
guess = 0
while guess != num:
	if guess!= 0 :
		absGuess = abs(guess-num)
		if absGuess < 5:
			print("It's too hot!")
		elif absGuess < 20:
			print("It's getting warmer!")
		else :
			print("Cold!")
		# print("Sorry",guess," wrong guess. Try again.")
	try:
		guess = int(input("Guess a number between 1 to 100: "))
	except ValueError:
		print("Invalid input. Please enter a valid number between 1 to 100.")


print("Congratulations! You got it! The number is",guess)
		