def palindrome(n):
	my_num = 0
	if n<0:
		return false
	while(n>0):
		rem = n%10
		my_num = my_num*10 + rem
		n = n//10
	return my_num	

if __name__ == '__main__':
	print("Please enter the number you would like to check: \n")
	number = int(input())

	if(number == palindrome(number)):
		print('true')
	else:
		print('false')
