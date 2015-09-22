def fibSequence():

	n = input('enter a number here: ')

	if n <= 1 :
		print n
		return

	case1 = 0
	case2 = 1
	print case1
	print case2
	
	for k in range (2, n):

		x = case1 + case2
		print x

		case1 = case2
		case2 = x		


fibSequence()