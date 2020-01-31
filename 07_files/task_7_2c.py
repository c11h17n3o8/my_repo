#!/usr/bin/env python3

# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_cmd = True

with open(argv[1],"r") as f, open(argv[2],"w") as dest:
        for line in f:
                for word in ignore:
                        if line.find(word) != -1:
                                ignore_cmd = True
                                break
                        else:
                                ignore_cmd = False
                else:
                        if ignore_cmd == False:
                                dest.write(line)
