
primes = [3]
tested = []
x = 1

while len(primes)<10000:
	x += 2

	for y in primes:
		if x%y != 0:
			if y == primes[len(primes)-1]:
				primes.append(x)
				primes = list(set(primes))
		else:
			break
primes.extend([1,2])
primes.sort()
print(primes.pop())