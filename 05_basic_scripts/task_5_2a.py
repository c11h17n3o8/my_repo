#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

network = input("Input network in format 10.1.1.0/24: ")
net = network.split("/")[0].split(".")
mask = network.split("/")[1]
bin_mask = '1'*int(mask) + '0'*(32-int(mask))
bin_net = f"{int(net[0]):08b}{int(net[1]):08b}{int(net[2]):08b}{int(net[3]):08b}"[0:int(mask)] + "0"*(32-int(mask))
print(f"Network:\n{int(bin_net[0:8],2):<10}{int(bin_net[8:16],2):<10}{int(bin_net[16:24],2):<10}{int(bin_net[24:32],2):<10}\n{bin_net[0:8]:<10}{bin_net[8:16]:<10}{bin_net[16:24]:<10}{bin_net[24:32]:<10}")
print(f"\n\nMask:\n{network[network.find('/'):]}\n{int(bin_mask[0:8], 2):<10}{int(bin_mask[8:16], 2):<10}{int(bin_mask[16:24], 2):<10}{int(bin_mask[24:32], 2):<10}")
print(f"{bin_mask[0:8]:<10}{bin_mask[8:16]:<10}{bin_mask[16:24]:<10}{bin_mask[24:32]:<10}")
