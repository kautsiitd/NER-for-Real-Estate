file = open("N.json").readlines()
data = []

for line in file:
	shout = ':'.join(line.split(':')[2:])[1:-3]
	lines = shout.split('\\n')
	temp  = []
	for i in lines:
		temp.extend(i.split())
	data.append(temp)

with open("test.txt","wb") as f:
	for shout in data:
		for token in shout:
			f.write(token)
			f.write('\n')
		f.write('\n')