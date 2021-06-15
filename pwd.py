pwd = 'a123456'
x = 2
while True :
	e = input('Please enter your password: ')
	if e == pwd :
		print('password correct.')
		print('You sign in successfully.')
		break
	elif x == 0 :
		print('You try too much time.')
		print('You can not enter the password anymore.')
		break
	else :
		print('your password is incorrect.')
		print('you have', x, 'chance to enter.')
		x = x - 1
