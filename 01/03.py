import re
str_in = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str_tmp = re.sub(r"[,\.]", "", str_in)
li_words = str_tmp.split(' ')
li_charNums = []
for i in range(len(li_words)):
    li_charNums.append(len(li_words[i]))

print(li_charNums)