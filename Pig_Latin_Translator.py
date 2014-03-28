'''
PIG LATIN TRANSLATOR
Ryan Schachte
2014
'''
#Program takes in a word, moves first letter to end of word and then adds ay to the end of it.

user_input = raw_input("Enter a word to convert into pig latin: ") #Gather user input

if len(user_input) > 0 and user_input.isalpha(): #First conditional (Entered min of 1 char, and ensures that char is alpha only)

	first_letter = user_input[0] #Gets first letter of the said entered string
	altered_user_input = user_input[1:len(user_input)] #Stores the remaining word into a new String var
	pig_add = 'ay' #Add 'ay' string to end of word for proper PYG Latin conversion

	#Convert everything to lower case.
	first_letter = first_letter.lower() 
	altered_user_input = altered_user_input.lower()
	pig_add = pig_add.lower()

	print 'Your pig word is converted into: ' + altered_user_input + first_letter + pig_add #Final concatenation

else:

	print 'You need to enter a valid string.' #Else conditional that fails to meet previous conditions
