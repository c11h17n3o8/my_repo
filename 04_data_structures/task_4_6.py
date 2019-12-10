# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

print(f'''
    ...: {"Protocol:":<24}{"OSPF"}
    ...: {"Prefix:":<24}{ospf_route.split()[1]}
    ...: {"AD/Metric:":<24}{ospf_route.split()[2].strip('[]')}
    ...: {"Next-Hop:":<24}{ospf_route.split()[4].strip(',')}
    ...: {"Last update:":<24}{ospf_route.split()[5].strip(',')}
    ...: {"Outbound Interface:":<24}{ospf_route.split()[6]}''')

