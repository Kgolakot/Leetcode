from collections import Counter

def duplicate(nums):
	check = Counter(nums)
	for val in check.values():
		if(val > 1):
			return True
	return False
lst = []

print("Please enter the number of elements in your array")

n = int(input())

print("please enter the elements of your array")

for i in range(0, n):
	ele = int(input())
	lst.append(ele)

if(duplicate(lst)):
	print("Your list contains duplicate")
else:
	print("Yay you do not have any duplicates")


