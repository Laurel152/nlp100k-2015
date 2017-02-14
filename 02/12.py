inputfile = open('hightemp.txt', 'r')
outputfile1 = open('col1.txt', 'w')
outputfile2 = open('col2.txt', 'w')

rownums = len(inputfile.readlines())
inputfile.seek(0)

datalists = []
for i in range(rownums):
	buf = inputfile.readline().replace('\n','')
	datalists.append(buf.split('\t'))
	
	outputfile1.write(datalists[i][0] + '\n')
	outputfile2.write(datalists[i][1] + '\n')
	
inputfile.close()
outputfile1.close()
outputfile2.close()
