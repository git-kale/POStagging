def sec(val):
	return int(val[1])

l = [line.rstrip('\n') for line in open("./files/outfreq.txt",'r')]

for i in range(0,len(l)):
	l[i] = l[i].rsplit(":", 1)
	l[i][1] = int(l[i][1])

l = sorted(l, key=sec, reverse=True)

with open("./files/sorted_out.txt", 'w') as f:
	for i in range(10):
		f.write("{}: {}\n".format(l[i][0], l[i][1]))
