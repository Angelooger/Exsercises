number = int(raw_input('Dame un numero\n'))
counter = 0
for i in range(1,number+1):
	counter+=i
print 'La suma factorial es de: ' + str(counter)