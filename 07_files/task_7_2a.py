#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_cmd = True

with open(argv[1],"r") as f:
	for line in f:
		if line.startswith("!"):
			pass
		else:
			for word in ignore:
				if line.find(word) != -1:
					ignore_cmd = True
					break
				else:
					ignore_cmd = False
			else:
				if ignore_cmd == False:
					print(line.rstrip())
