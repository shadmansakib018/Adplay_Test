def TypeCheck(str):
	val = ord(str[0])
	if(val>=48 and val<=57):
		print("Number")
	else:
		print("String")

TypeCheck('45')
