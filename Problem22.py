
with open('./misc/names.txt') as f:
    content = f.readlines()
newcontent = content.pop().split(',')
newcontent.sort()

i = 0
tot_sum = 0

while newcontent:

	i+=1
	wordsum = 0
	for char in newcontent.pop(0).replace('"',''):
		wordsum += ord(char)-ord('A')+1
	tot_sum += i * wordsum

print(tot_sum)