#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_cmd = True

with open(argv[1],"r") as f, open("config_sw1_cleared.txt","w") as dest:
	for line in f:
		for word in ignore:
			if line.find(word) != -1:
				ignore_cmd = True
				break
			else:
				ignore_cmd = False
		else:
			if ignore_cmd == False:
				dest.write(line)
