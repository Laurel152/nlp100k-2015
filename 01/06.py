CHR = 0
WRD = 1

def n_gram(text,n,divmethod):
    index = {}
    if divmethod == CHR:
        processingunit = text
    elif divmethod == WRD:
        processingunit = text.split(" ")

    for i in range(len(processingunit)):
        keyname = generate_keyname(processingunit,n,divmethod,i)
        if keyname in index:
            index[keyname] = index[keyname] + 1
        else:
            index[keyname] = 1

    return index

def generate_keyname(processingunit,n,divmethod,cnt):
    if cnt + n < len(processingunit):
        li_tmp = processingunit[cnt:cnt+n]
    else:
        li_tmp = processingunit[cnt:]
    if divmethod == CHR:
        keyname = li_tmp
    elif divmethod == WRD:
        keyname = li_tmp[0]
        for i in range(len(li_tmp)-1):
            keyname = keyname + '-' + li_tmp[i+1]

    return keyname

inputstrX = "paraparaparadise"
inputstrY = "paragraph"

X = set(n_gram(inputstrX,2,CHR))
Y = set(n_gram(inputstrY,2,CHR))

print("  X   = " + str(X))
print("  Y   = " + str(Y))
print("X | Y = " + str(X | Y))
print("X & Y = " + str(X & Y))
print("X - Y = " + str(X - Y))
print("Y - X = " + str(Y - X))
print('se' in X)
print('se' in Y)