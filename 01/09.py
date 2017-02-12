import random

def tokenize(text):
    token = text.split(" ")
    return token

def shuffle(word):
    chars = list(word)
    shufflechars = chars[1:-1]
    shuffledchars = random.sample(shufflechars,len(shufflechars))
    shuffledword = ''.join([chars[0],''.join(list(shuffledchars)),chars[-1]])
    return shuffledword

str_in = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = tokenize(str_in)

shuffledstr = ""
for w in words:
    if len(w)>=5:
        shuffledstr = shuffledstr + shuffle(w)
    else:
        shuffledstr = shuffledstr + w
    if w != words[len(words)-1]:
        shuffledstr = shuffledstr + " "

print(shuffledstr)