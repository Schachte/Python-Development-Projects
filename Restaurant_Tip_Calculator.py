'''''''''''''''''''''''''''''''''''''''
Restaurant Tip Calculations in Python
'''''''''''''''''''''''''''''''''''''''
#Ryan Schachte
#2014 - Python Development

#Define function to calculate Tip
def tipCalculator(cost_of_meal):

	percent_tip = raw_input("Do you want to pay 15% or 20%? Enter 15 or 20. ")

	percent_tip = int(percent_tip)

	if percent_tip == 15:
		amount_to_tip = cost_of_meal * .15
		total_cost = cost_of_meal + amount_to_tip
		print 'Your meal will cost: ' + str(total_cost)
		print 'Here is a break-down of your meal costs:\nMeal Cost: $%s\nTip Amount: $%s' %(str(cost_of_meal),str(amount_to_tip))

	elif percent_tip == 20:
		amount_to_tip = cost_of_meal * .2
		total_cost = cost_of_meal + amount_to_tip
		print 'Your meal will cost: ' + str(total_cost)
		print 'Here is a break-down of your meal costs:\nMeal Cost: $%s\nTip Amount: $%s' %(str(cost_of_meal),str(amount_to_tip))

	else:
		print "You didn't enter a valid tip amount"


cost_of_meal = raw_input("How much did your meal cost?")
tipCalculator(int(cost_of_meal))
