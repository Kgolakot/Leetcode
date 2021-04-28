string = "leetcodeisacommunityforcoders"
lst = []

for ele in string:
	if(ele!='a' and ele!='i' and ele!='o' and ele!='u' and ele!='e'):
		lst.append(ele)

''.join(lst)
print(lst)
