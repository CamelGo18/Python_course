def absolute(x):
	if type(x) == (int) or type(x) == (float):
		return('The absolute value of ' + str(x) + ' is ' + str(abs(x)))
	else:
		return('error: not a number')


def maximum(your_list):
	max_value = max(your_list)
	return ('The maximum value in your list is: ' + str(max_value))





def absolute(x):
	if x>= 0:
		 return('The absolute value of ' + str(x) + ' is ' + str(x))
	elif x < 0:
		return('The absolute value of ' + str(x) + ' is ' + str(abs(x)))
	else:
		return('error: not a number')

