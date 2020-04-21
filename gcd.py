num1 = input ("Enter first number:\n")
num2 = input ("Enter second number:\n")

def GCD(x,y):
	if x>y:
		num = y
	else:
		num = x
	for i in range(1, num+1):
		if ((x%i == 0) and (y%i == 0)):
			gcd = i;
	return gcd

print ("the gcd of {0} and {1} is {2}" .format(num1, num2,GCD(num1, num2) ))
