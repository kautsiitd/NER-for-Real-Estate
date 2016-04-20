import sys

filename = sys.argv[1]

ans = []
with open(filename) as ff:
	lines = ff.readlines()
	for ite,line in enumerate(lines):
		line = line.rstrip()
		if (line.strip()==''): 
			continue
		xx = line.split()
		if (len(xx)!=2 or (xx[1]!='L' and xx[1]!='P'
							and xx[1]!='LA' and xx[1]!='C'
							and xx[1]!='N' and xx[1]!='T'
							and xx[1]!='A' and xx[1]!='O')):
			ans.append((ite+1, line))
print "Following are the lines with error\n"
for tt in ans:
	print tt
print "\n"