import math
import sys

res = a2 = b2 = c2 = 0


for x in range(1,1000):
	for y in range(1,x):
		
		a2 = pow(x,2)
		b2 = pow(y,2)

		c2 = a2 + b2

		res = math.sqrt(c2) + math.sqrt(b2) + math.sqrt(a2)

		if res == 1000:
			print(int(math.sqrt(c2) * math.sqrt(b2) * math.sqrt(a2)))
			sys.exit(0)
		

