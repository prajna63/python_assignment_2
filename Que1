import math
def getDivisors(num):
	n = math.ceil(math.sqrt(num))
	total = 1
	divisor = 2
	while(divisor<n):
		if(num%divisor == 0):
			total += divisor
			total += num//divisor
		divisor += 1
	return total

n = int(input("Enter the number:"))
print('1 is deficient number and sum is 0')
for i in range(2,n+1):
	t = getDivisors(i)
	if(t == 1):
		print(i,'is perfect number and sum is', t)
	elif(t < i):
		print(i,'is deficient number and sum is', t)
	else:
		print(i,'is abundant number and sum is', t)
