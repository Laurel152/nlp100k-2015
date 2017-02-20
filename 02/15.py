import sys

args = sys.argv

def tail(n):
	inputfile = open('hightemp.txt', 'r')
	
	rowlists = inputfile.readlines()
	rownums = len(rowlists)
	if n > rownums:
		n = rownums
	
	output = ""
	for i in range(rownums)[-n:]:
		output = output + rowlists[i]
	
	inputfile.close()
	
	return output
	
if len(args) == 2:
	sys.stdout.write(tail(int(args[1])))
else:
	print('ERROR: 15.py has only one integer augument.')
