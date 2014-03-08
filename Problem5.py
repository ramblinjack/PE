import sys

res = []
primes = 19*17*13*11*7*5*3*2
i = 1
x = 1

while True:
	x +=1
	i = primes*x
	for y in range(2,21):
		if i%y == 0:
			if y == 20:
				print(i)
				sys.exit(0)
		else:
			break
		


print(str(res))
	