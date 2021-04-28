def isDigPrime(n):
	while(n>0):
		dig = n%10 
		if(dig != 2 and dig!=3 and dig!=5 and dig!=7):
			return 0
		n = n//10
	return 1

def FactorPrime(n):
	if(n == 1):
		return 0
	i = 2
	while i*i <= n:
		if(n%2==0):
			return 0
		i +=1
	return 1

def FullPrime(n):
	return(isDigPrime(n) and FactorPrime(n))

print("Please Enter the your choice of number:\n ")
num = int(input())

if (FullPrime(num)):
	print(" | Yes | ")
else:
	print(" | No | ")
