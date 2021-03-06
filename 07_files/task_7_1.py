#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open("ospf.txt","r") as f:
	for line in f:
		print(f'''{"Protocol:":<24}{"OSPF"}
{"Prefix:":<24}{line.split()[1]}
{"AD/Metric:":<24}{line.split()[2].strip('[]')}
{"Next-Hop:":<24}{line.split()[4].strip(',')}
{"Last update:":<24}{line.split()[5].strip(',')}
{"Outbound Interface:":<24}{line.split()[6]}
		''')
