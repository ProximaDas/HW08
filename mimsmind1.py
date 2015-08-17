# mimsmind1 game. This implements the bulls and cows feedback in the classic guessing game.

# Imports
import random,sys,re

# Function definitions
def mimsmind1():
	# Try accessing user input for 	number of digits
	try:
		num_length = int(sys.argv[1])
	except:
		num_length = 3
	finally:
		# Calculate max number of attempts allowed
		maxrounds = 2 ** num_length + num_length
		print "Let's play the mimsmind1 game. You have %i guesses." % (maxrounds)
		# Generate random number
		random_number = generate_random_n(num_length)
		# Start guess_counter
		guess_counter = 0
		guess,guess_counter = promp_user("Guess a " + str(num_length) + " digit number: ",guess_counter,num_length)

		while guess_counter < maxrounds:
			# Compare random_number and user's guess
			if guess != random_number:
				guess,guess_counter = promp_user(bull_and_cow(guess,random_number) + " Try again: ",guess_counter,num_length)

			else:
				print "Congratulations. You've guessed the number in %i tries." % (guess_counter)
				break

		if guess_counter == maxrounds:
			print "Sorry, you did not guess the number in %i tries. The correct number is %s." % (guess_counter,random_number)

def promp_user(message,counter,length):
	input = raw_input(message)
	while True:
			searchObj = re.search('^[0-9]{' + str(length) +'}$',input)
			# Prompt user for guess
			if searchObj:
				guess = input
				counter += 1
				break
			else:
				input = raw_input("Invalid input.Try again. ")
	
	return str(guess), counter

def generate_random_n(n):
	lower_bound = 0
	upper_bound = (10 ** (n)) - 1
	random_number = random.randint(lower_bound,upper_bound)

	# Pad zeroes to left of generated number to ensure it's of length n
	if len(str(random_number)) < n:
		random_number = str(random_number).zfill(n)
	else:
		random_number = str(random_number)
	return random_number

def bull_and_cow(input,solution):
	feedback = {'bull':0,'cow':0}
	for i in range(len(input)):
		if input[i] in solution:
			# Check if it's a bull/cow
			if solution.find(input[i]) == i:
				feedback['bull'] += 1
			else:
				feedback['cow'] += 1
	feedback_string = "%i bull(s), %i cow(s)." % (feedback['bull'], feedback['cow'])
	return feedback_string

def main():
	mimsmind1()

if __name__ == '__main__':
	main()