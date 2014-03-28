'''
Fizz-Buzz is a popular algorithm question to test knowledge in some programming interviews
Ryan Schachte
2014

Goals:
	If number is divisible by 3 then print fizz, if it is divisible by 5 then print buzz. If neither, print the actual number to the console
'''

for x in xrange(1,100):
	if(x % 3 == 0):
		print 'Fizz' #Print Fizz, because the current number IS divisible by 3.
	elif(x % 5 == 0): #Print Buzz, because the number IS divisible by 5.
		print 'Buzz'
	else: print x


print 'Now that they for loop has iterated through the following number 1-100, it is time to take a try for yourself'

number_to_check = raw_input("Enter the number you would like to determine if it is Fizz or Buzz...")

if (int(number_to_check) % 3 == 0 and int(number_to_check) % 5 != 0 ):
	print 'Your number is indeed Fizz because it is divisible by 3'
elif (int(number_to_check) % 5 == 0 and int(number_to_check) % 3 != 0):
	print 'Your number is indeed Buzz because it is divisible by 5'
elif (int(number_to_check) % 5 ==0 and int(number_to_check) % 3 == 0):
	print 'Your number is Fizz and Buzz! The number ' + str(number_to_check) + " is divisible by 3 and 5!"
else:
	print 'The shit you entered is neither divisible by 3 or 5, therefore, it is not fizz or buzz!!'

