import re

str_in = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
li_takeOneChar = [0,4,5,6,7,8,14,15,18]

str_tmp = re.sub(r"[,\.]", "", str_in)
li_words = str_tmp.split(' ')
dic_initials = {}

for i in range(len(li_words)):
    if i in li_takeOneChar:
        dic_initials[li_words[i][:1]] = i
    else:
        dic_initials[li_words[i][:2]] = i

print(dic_initials)