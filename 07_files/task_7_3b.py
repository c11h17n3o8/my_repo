#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input("Input VLAN: ")
list = []
with open("CAM_table.txt","r") as f:
        for line in f:
                if line.find("DYNAMIC") != -1:
                       list.append(line.replace("  DYNAMIC    ", "").rstrip().split())
for item in list:
	item[0] = str(item[0])
	if vlan == item[0]:
		print("\t".join(item))
