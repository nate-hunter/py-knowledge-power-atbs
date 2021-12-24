spam = [ ]

def to_string(aList): 
	if len(aList) == 0:
		print('Please provide a list.')
		return ''
	else: 
		result = ''
		for i, element in enumerate(aList):
			if i + 1 != len(aList):
				result += f'{element}, '
			elif i + 1 == len(aList):
				result += f'and {element}'
		return result

print(to_string(spam))