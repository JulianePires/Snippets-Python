k=0
money=0
canFly=True
A=[]
B=[]
C=[]

while canFly != False:
	k+=1
	inputs = input().split(' ')
	N = int(inputs[0])
	M = int(inputs[1])

	count = 0
	cost=[]

	for x in range(M-1):
		inputs2 = input().split(' ')
		A[x] = int(inputs2[0])
		B[x] = int(inputs2[1])
		C[x] = int(inputs2[2])
		cost[count]+=C[x]
		if A[x] == 1:
			count+=1
		if B[x] == 4:
			x+=1
		
	inputs3 = input().split(' ')
	D = int(inputs3[0])
	K = int(inputs3[1])

	if K*count < D:
		print(f'Instancia {k}')
		print('impossivel \n')
		canFly = False
		break

	while D > 0:
		if K >= D:
			money+=D*min(cost)
			D=0
		else:
			minimo=min(cost)
			cost.remove(min(cost))
			money+=K*minimo
			D=-K

	print(f'Instancia {k}')
	print(money+'\n')
		
