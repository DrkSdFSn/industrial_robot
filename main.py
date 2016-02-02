from gks import count_unique, count_diff, matrix_output, grouped, gks3, unique_module
from gks4 import draw_graph_create_module
from scheme import create_scheme
from os import stat, path
from sys import argv
from copy import deepcopy

matrix_opr = []
condition = True
filepath = str(path.realpath(path.dirname(argv[0]))) + '\matrix.txt' # if file is empty, input via the console
if stat(filepath).st_size == 0:
	condition = False
	n = int(input('Enter the number of lines of operations: '))
	for i in range(n):
		print(str(i + 1)+': ', end='')
		matrix_opr.append([j for j in input().split()])
if condition:
	for line in open(filepath):
		matrix_opr.append( [x for x in line.split() ] )

#input matrix of operations
print('Input data: ')
for i in range(len(matrix_opr)):
    for j in range(len(matrix_opr[i])):
        print(matrix_opr[i][j], end=' ')
    print()

nn = count_unique(matrix_opr) 
n = int(len(nn)/2)
print("\nCount of unique elements: ", n, "(", nn,")")

lens = len(matrix_opr)
ss2 = count_diff(matrix_opr, n, lens)

matrix_out = matrix_output(ss2, lens)
print('\nSquare matrix:\n', matrix_out, sep='')

groups = grouped(matrix_out.tolist())
print('\nGroups:')
for i in groups.items():
	#print('\t', i[0], 'group:', i[1],  set([k for j in i[1] for k in matrix_opr[j]]))
	print("\t {0:<1d} group: {1!s:<30s} -> {2!s:<100s}".format(i[0], i[1], set([k for j in i[1] for k in matrix_opr[j]])))

specify_group1 = gks3(groups, matrix_opr) # some bug with this fubction
refin_groups = gks3(groups, matrix_opr) # for it works well we must call twice this func
print('\nRefined groups:')
for i in refin_groups.items():
	#print('\t', i[0], 'group:', i[1], set([k for j in i[1] for k in matrix_opr[j]]))
	print("\t {0:<1d} group: {1!s:<35s} -> {2!s:<100s}".format(i[0], i[1], set([k for j in i[1] for k in matrix_opr[j]])))
    	
module = {}
for i in refin_groups.keys():
	module[i] = draw_graph_create_module(matrix_opr, refin_groups[i], 'group'+str(i))
print('\nModules:')
for i in module.items():
	print('\t', i[0], 'group:')
	for j in i[1].items():
		print('\t', j[0], j[1])
	print('\n')

un_mod = unique_module(module)
print('\nRefined modules:')
for i in un_mod.items():
	print('\t', i[0], ':', i[1])
	
create_scheme(matrix_opr, un_mod)
input("\nTo exit, press any key")
