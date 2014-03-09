import math
sum1 = 0
sum2 = 0

for x in range(1,101):
	sum1 += pow(x,2)
	sum2 += x
sum2 = pow(sum2, 2)
print(str(sum2-sum1))
