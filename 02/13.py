inputfile1 = open('col1.txt', 'r')
inputfile2 = open('col2.txt', 'r')
outputfile = open('col1_2.txt', 'w')

rowlists1 = inputfile1.readlines()
rowlists2 = inputfile2.readlines()
rownums = len(rowlists1)

for i in range(rownums):
	buf1 = rowlists1[i].replace('\n', '')
	buf2 = rowlists2[i].replace('\n', '')
	outputfile.write(buf1 + '\t' + buf2 + '\n')

inputfile1.close()
inputfile2.close()
outputfile.close()
