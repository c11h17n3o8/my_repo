#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.1a

Сделать копию функции из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}
def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
	list = []
	for intf in intf_vlan_mapping:
		list.append(intf.rstrip())
		for cmd in access_template:
			if cmd.endswith("vlan"):
				cmd = f"{cmd} {intf_vlan_mapping[intf]}"
				list.append(cmd.rstrip())
			else:
                                list.append(cmd.rstrip())
		if psecurity:
			for sec_cmd in psecurity:
				list.append(sec_cmd.rstrip()) 
	return list
print(generate_access_config(access_config, access_mode_template, port_security_template))
