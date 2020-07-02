#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции (как передать вывод команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
"""
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
"""

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция работать
и на других файлах (тест проверяет работу функции на выводе из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

dict = {}
list = []

def parse_cdp_neighbors(command_output):
	i = 0
	result = command_output.split("\n")
	host = result[0][:result[0].index(">")]
	for line in result:
		if line.startswith("Device ID"):
			i = result.index(line)
	result = result[i+1:-1]
	for line in result:
		list.append(line.split("  "))
	for line in list:
		while '' in line:
			line.remove('')
		for item in line:
			line[line.index(item)] = item.strip()
		dict[tuple([host,line[1]])] = [line[0],line[-1].split("- ")[-1]]
	return dict

if __name__ == "__main__":
	with open("sh_cdp_n_r3.txt") as f:
		print(parse_cdp_neighbors(f.read()))
