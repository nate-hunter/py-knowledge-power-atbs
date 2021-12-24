# user_input = int(input('Please enter a number: '))

def collatz(number):
	if (number % 2 == 0):
		result = number // 2
		print(result)
		return result 
	elif (number % 2 == 1):
		result = 3 * number + 1
		print(result)
		return result 


def app():
	try:
		user_input = int(input('Please enter a number => '))

		result = collatz(user_input)

		while (result > 1):
			result = collatz(result)
	except ValueError:
		print('please enter an integer')

app()

