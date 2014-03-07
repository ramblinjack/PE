import math

L = [600851475143]
prime = []

while L:
	i = L.pop()
	for x in range(2, int(math.sqrt(i))):
		if i%x == 0:
			L.append(x)
			prime.append(x)
			try:
				prime.remove(i)
			except ValueError:
				pass

prime.sort()
print(prime.pop())

