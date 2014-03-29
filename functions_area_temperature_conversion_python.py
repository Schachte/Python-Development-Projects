#Compute area of a triangle

def triangle_area(base, height):
	area = .5 * base * height
	return area

base = raw_input("What is the base?")
base = int(base)

height = raw_input("What is the height?")
height = int(height)

a = triangle_area(base, height)

print 'Area is ' + str(a)


#Convert F to C
#F = c * 9/5 + 32
#C = (f - 32) * 5/9

def c_to_f(value):
	f = value * (9.0/5.0) + 32
	return f 

def f_to_c(value):
	c = (value - 32) * 5.0/9.0
	return c 

user_conversion = raw_input("Would you like to convert Fahrenheit to Celcius or Celcius to Fahrenheit?")
user_conversion = user_conversion[0].lower()
print user_conversion

if (user_conversion == 'f'):
	fahr = raw_input("Enter the degree in Fahrenheit: ")
	fahr = int(fahr)
	new_temp = f_to_c(fahr)
	print str(fahr) + " degrees Fahrenheit is the same as " + str(new_temp) + " degrees Celcius."

elif (user_conversion == "c"):
	cels = raw_input("Enter the degree in Celcius: ")
	cels = int(cels)
	new_temp = c_to_f(cels)
	print str(cels) + " degrees Celcius is the same as " + str(new_temp) + " degrees Fahrenheit."

else:
	print 'You did not enter a valid value.'
