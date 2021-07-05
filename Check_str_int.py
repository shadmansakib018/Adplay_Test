def TypeCheck(str):
	type = 'String'
	for ch in str:
		val = ord(ch)
		if(val>=48 and val<=57):
			type = "Number"
		else:
			return "String"
	return type

print(TypeCheck('!5657577009a'))
