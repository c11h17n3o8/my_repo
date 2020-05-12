#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
	int_cfg = {}
	int_cfg_2 = {}
	list_sum = []
	f = open(config)
	lines = f.read().split("interface")[1:-1]
	for line in lines:
		if line.find("switchport mode access") != -1:
			if line.find("switchport access vlan") == -1:
				int_cfg.update({line.split("\n")[0]: "1"})
			else:
				for cmd in line.split("\n"):
					if cmd.startswith(" switchport access vlan"):
                                        	int_cfg.update({line.split("\n")[0]: cmd.split()[-1]})
		if line.find("switchport mode trunk") != -1:
#			int_cfg_2.update({line.split("\n")[0]: "trunk"})
			for cmd in line.split("\n"):
				if cmd.startswith(" switchport trunk allowed vlan"):
					int_cfg_2.update({line.split("\n")[0]: cmd.split()[-1].split(",")})
	list_sum = [int_cfg, int_cfg_2]
	return list_sum
'''
if line.startswith("\ninterface Fast"):
                        line = line.split("\n")
                        for cmd in line:
                                if cmd.startswith(" switchport access vlan"):
                                        int_cfg.update({line[1]: cmd.split()[-1]})
                                if cmd.startswith(" switchport trunk allowed vlan"):
                                        int_cfg_2.update({line[1]: (cmd.split()[-1]).split(",")})
        list_sum = [int_cfg, int_cfg_2]
        return list_sum
'''
print(get_int_vlan_map("config_sw2.txt"))
