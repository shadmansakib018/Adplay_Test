def NotCheck(str):
	if(str[0:3]=='not'):
		return str
	else:
		return 'not ' + str

print(NotCheck("candy"))