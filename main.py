from gks import count_unique, count_diff, matrix_output, grouped, gks3, unique_module
from gks4 import draw_graph_create_module
from os import stat, path
from sys import argv

p = []
condition = True
filepath = str(path.realpath(path.dirname(argv[0]))) + '\matrix.txt'
if stat(filepath).st_size == 0:
	condition = False
	n = int(input('Введите количество строк операций: ')) 
	for i in range(n):
		print(str(i + 1)+': ', end='')
		p.append([j for j in input().split()])
if condition:
	for line in open(filepath):
		p.append( [x for x in line.split() ] )

#вывод входных данных
print('Входные данные: ')
for i in range(len(p)):
    for j in range(len(p[i])):
        print(p[i][j], end=' ')
    print()

n = count_unique(p)

lens = len(p)
ss2 = count_diff(p, n, lens)
m = matrix_output(ss2, lens)
mg = grouped(m.tolist())
specify_group = gks3(mg, p)
module = {}
for i in specify_group.keys():
	module[i] = draw_graph_create_module(p, specify_group[i], 'group'+str(i))
un_mod = unique_module(module)

print('\nВыходные данные:\n', m, sep='')
print('\nГруппы:')
for i in mg.items():
	print(i[0], 'group:', i[1])
print('\nУточненные группы:')
for i in specify_group.items():
	print(i[0], 'group:', i[1])
print('\nМодули:')
for i in module.items():
	print(i[0], 'group:', i[1])
print('\nУникальные модули:')
for i in un_mod.items():
	print(i[0], 'group:', i[1])
input("\nДля выхода нажмите любую клавишу")