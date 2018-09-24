def fibonacci(n):
	if n==1:
		return 1
	elif n ==2:
		return 1
	elif n > 2:
		return fibonacci(+1)+ fibonacci(n+2)

for n in range (1,20):
	print(n, ":", fibonacci(n))
