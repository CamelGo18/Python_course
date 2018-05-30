'''average of a list '''
def average(list_name):
	av_value = sum(list_name) / (len(list_name))
	return('The average value of list ' + str(list_name) + ' is ' + str(av_value))
		

	

''' median of a list'''
def median(list_name):
	med_number = int(len(list_name)/2)
	sorted_list = sorted(list_name)	
	med_number2 = med_number + 1
	if len(list_name) % 2 == 0:
# % is module: divides left hand operand by right hand operand and returns remainder
		median = (sorted_list[med_number] + sorted_list[med_number2]) / 2
		return median	
	else:		
		median = sorted_list[med_number]
		return median
		
