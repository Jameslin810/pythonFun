import math 

def piToNTHDigit():
	x = input('enter a number')
	# print "pi: %." + `x`+ "f" % math.pi
	y  = " " + str("pi: %." + `x` + "f" % math.pi)
	#y += `round(math.pi, x)`
	#print y[x]
	print y;


piToNTHDigit()

