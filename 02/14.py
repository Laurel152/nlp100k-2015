import sys

args = sys.argv

def head(n):
	inputfile = open('hightemp.txt', 'r')
	
	rowlists = inputfile.readlines()
	rownums = len(rowlists)
	if n > rownums:
		n = rownums
	
	output = ""
	for i in range(n):
		output = output + rowlists[i]
	
	inputfile.close()
	
	return output
	
if len(args) == 2:
	sys.stdout.write(head(int(args[1])))
else:
	print('ERROR: 14.py has only one integer augument.')
