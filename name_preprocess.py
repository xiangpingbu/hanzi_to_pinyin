# -*- coding: utf-8 -*-
f = open('name_daquan.txt','r')
ft = f.readline()
list = []
output = open('name_word.txt','w')

for i in range(0,len(ft),3):
	word = ft[i:i+3]
	if word not in list:
		list.append(word)
		output.write(word+'\n')
output.close()
