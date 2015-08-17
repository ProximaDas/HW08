# Imports
import random,sys
# Function definitions
def mimsmind0():
	# Try accessing user input for 	number of digits
	try:
		num_length = int(sys.argv[1])
	except:
		num_length = 1
	finally:
		print "Let's play the mimsmind0 game."
		# Generate random number
		random_number = generate_random_n(num_length)
		# Start guess_counter
		guess_counter = 0
		guess,guess_counter = promp_user("Guess a " + str(num_length) + " digit number: ",guess_counter)

		while True:
			# Compare random_number and user's guess
			if guess > random_number:
				guess,guess_counter = promp_user("Try again. Guess a lower number: ",guess_counter)
			elif guess < random_number:
				guess,guess_counter = promp_user("Try again. Guess a higher number: ",guess_counter)
			else:
				print "Congratulations. You've guessed the number in %i attempts" % (guess_counter)
				break

def promp_user(message,counter):
	while True:
			# Prompt user for guess
			input = raw_input(message)
			try:
				guess = int(input)
			except:
				print "I'm afraid that's not a number. Try again."
			else:
				counter += 1
				break
	return guess, counter

def generate_random_n(n):
	if n == 1:
		lower_bound = 0
	else:
		lower_bound = 10 ** (n-1)
	upper_bound = (10 ** (n)) - 1
	random_number = random.randint(lower_bound,upper_bound)

	return random_number

def main():
	mimsmind0()

if __name__ == '__main__':
	main()