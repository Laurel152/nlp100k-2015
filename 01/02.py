#coding: utf-8

in_str1 = "パトカー"
in_str2 = "タクシー"

out_str = ""
if len(in_str1) >= len(in_str2):
    max_length = len(in_str1)
else:
    max_length = len(in_str2)

for i in range(max_length):
    if i < len(in_str1):
        out_str = out_str + in_str1[i]
    if i < len(in_str2):
        out_str = out_str + in_str2[i]

print(out_str)