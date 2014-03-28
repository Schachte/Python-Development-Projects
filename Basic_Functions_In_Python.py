'''
This is a program that calculates the square of a function in Python
'''
#Ryan Schachte
#2014

def squareNumber(n):
	input_squared = n**2
	print 'You entered the number: ' + str(n) + " and then I squared that number and got " + str(input_squared)
	return input_squared

number = raw_input("Enter a number to square..")
number = int(number)

squareNumber(number)

def nameConcatenation(first_name, last_name):
	full_name = "Your name is %s %s" %(first_name, last_name)
	print full_name
	print "Your name is also, " + first_name[0] + ". %s" %(last_name)
	print "You have the initials of: %s.%s" %(first_name[0], last_name[0]) 
	return full_name

first_name = raw_input("Please enter your first name: ")
last_name = raw_input("Please enter your last name: ")

nameConcatenation(first_name, last_name)