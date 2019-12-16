#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
net = argv[1].split(".")
mask = argv[2]
bin_mask = '1'*int(mask) + '0'*(32-int(mask))
bin_net = f"{int(net[0]):08b}{int(net[1]):08b}{int(net[2]):08b}{int(net[3]):08b}"[0:int(mask)] + "0"*(32-int(mask))
print(f"Network:\n{int(bin_net[0:8],2):<10}{int(bin_net[8:16],2):<10}{int(bin_net[16:24],2):<10}{int(bin_net[24:32],2):<10}\n{bin_net[0:8]:<10}{bin_net[8:16]:<10}{bin_net[16:24]:<10}{bin_net[24:32]:<10}")
print(f"\n\nMask:\n/{mask}\n{int(bin_mask[0:8], 2):<10}{int(bin_mask[8:16], 2):<10}{int(bin_mask[16:24], 2):<10}{int(bin_mask[24:32], 2):<10}")
print(f"{bin_mask[0:8]:<10}{bin_mask[8:16]:<10}{bin_mask[16:24]:<10}{bin_mask[24:32]:<10}")
