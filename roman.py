roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }

print("Please enter the string values :\n")
string = str(input())

value = 0
s_big = roman_map['I']
for s in string[::-1]:
	if(s_big > roman_map[s]):
		value = value - roman_map[s]
	else:
		value = value + roman_map[s]
		s_big = roman_map[s]

print(value)	
	
		
