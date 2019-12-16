#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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
print(f"Network:\n{net[0]:<10}{net[1]:<10}{net[2]:<10}{net[3]:<10}\n{int(net[0]):08b}  {int(net[1]):08b}  {int(net[2]):08b}  {int(net[3]):08b}")
print(f"\n\nMask:\n{network[network.find('/'):]}\n{int(bin_mask[0:8], 2):<10}{int(bin_mask[8:16], 2):<10}{int(bin_mask[16:24], 2):<10}{int(bin_mask[24:32], 2):<10}\n{bin_mask[0:8]:<10}{bin_mask[8:16]:<10}{bin_mask[16:24]:<10}{bin_mask[24:32]:<10}")
