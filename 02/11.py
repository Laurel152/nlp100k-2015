inputfile = open('hightemp.txt', 'r')

replacedstr = inputfile.read().replace('\t', ' ')

print(replacedstr)

inputfile.close()
