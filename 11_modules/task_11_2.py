#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

from draw_network_graph import draw_topology

# эти заготовки написаны чтобы показать в какой момент должна
# рисоваться топология (после вызова функции)
def create_network_map(filenames):
	i = 0
	list = []
	dict = {}
	list2 = []
	for file in filenames:
		with open(file) as f:
			result = f.read().split("\n")
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
		list = []
	for value in dict.values():
		list2.append(str(value).strip("[").strip("]"))
	dict2 = dict.copy()
	for key in tuple(dict.keys()):
		if str(key).strip("(").strip(")") in list2:
			del dict2[tuple(dict[key])]
			list2.remove(str(key).strip("(").strip(")"))
			list2.remove(str(dict[key]).strip("[").strip("]"))
	return dict2

if __name__ == "__main__":
	infiles = [
		"sh_cdp_n_sw1.txt",
		"sh_cdp_n_r1.txt",
		"sh_cdp_n_r2.txt",
		"sh_cdp_n_r3.txt",
	]
#	create_network_map(infiles)
	topology = create_network_map(infiles)
    # рисуем топологию:
	draw_topology(topology)
