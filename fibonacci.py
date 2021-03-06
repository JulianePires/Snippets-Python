while True:
	lista = input().split(' ')
	n = int(lista[0])
	b = int(lista[1])
	aux = 1
	count = 0

	def fib(n):
		global count 
		count += 1
		if n < 2:
			return n
		else:
			return (fib(n-1)+fib(n-2))%b

	if n != 0 and b != 0:	
		fib(n)
		print(f'Case {aux}: {n} {b} {count}')
		aux += 1
	else:
		break
