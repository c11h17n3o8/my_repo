#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
pri
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите IP-адрес в формате 10.0.1.1: ")
if len(ip.split(".")) == 4:
	for octet in ip.split("."):
			if int(octet) >= 0 and int(octet) <= 255:
				ipIsCorrect = True
			else:
				ipIsCorrect = False
				print("Неправильный IP-адрес")
else:
	ipIsCorrect = False
	print("Неправильный IP-адрес")
if ipIsCorrect:
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
