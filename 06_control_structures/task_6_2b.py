#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите IP-адрес в формате 10.0.1.1: ")
ipIsCorrect = False
while not ipIsCorrect:
	if len(ip.split(".")) != 4:
		pass
	else:
		for octet in ip.split("."):
			if not int(octet) in range(255):
				ipIsCorrect = False
				break
			else:
				ipIsCorrect = True
		else:
			if ipIsCorrect == True:
				if int(ip.split(".")[0]) >= 1 and int(ip.split(".")[0]) <= 223:
					print("unicast")
				elif int(ip.split(".")[0]) >= 224 and int(ip.split(".")[0]) <= 239:
					print("multicast")
				elif ip == "255.255.255.255":
					print("broadcast")
				elif ip == "0.0.0.0":
					print("unassigned")
				else:
					print("unused")
				continue
	ip = input("Неправильный IP-адрес. Введите еще раз: ")
