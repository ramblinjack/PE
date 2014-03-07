pal = []

for x in range(900,999):
	for y in range(900,999):
		sum = str(x*y)
		if sum[0] == sum[len(sum)-1]:
			if sum[1]== sum[len(sum)-2]:
				if sum[2]== sum[len(sum)-3]:
					pal.append(sum)
pal.sort()
print(pal.pop())