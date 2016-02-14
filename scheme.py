from graphviz import Digraph
from os import stat, path
from sys import argv
def create_scheme(x, module):
	def func1(m, f1, f2, di, ind):
		edge_l = ''
		edge_f = ''
		for i in module.items():
			for j in i[1]:
				if j == f1:
					edge_f = i[0]
				if j == f2:
					edge_l = i[0]
		if edge_f == edge_l:
			return di
		edge = edge_f + ',' + edge_l
		if edge not in di:
			di[edge] = set()
			di[edge].add(ind)
		else:
			di[edge].add(ind)
		return di

	def func(matrix, module):
		first_elem = []
		second_elem = []
		for i in matrix:
			first_elem.extend(list(i)[:1])
			second_elem.extend(list(i)[-1:])
		first_elem = set(first_elem)
		second_elem = set(second_elem)
		keys_in = 'M2'
		keys_out = 'M1'
		module['in' + keys_in] = module[keys_in]
		module.pop(keys_in)
		module['out' + keys_out] = module[keys_out]
		module.pop(keys_out)
		return module
	edges = {}
	module = func(x, module)
	for i in x:
		for j in range(len(i) - 1):
			edges = func1(module, i[j], i[j+1], edges, x.index(i)) #index(i))
	#print(edges)

	dot = Digraph(comment='Struct', format='png')
	for i in module.items():
		dot.node(i[0], str(i[0]) + ':' + str(i[1]))
	for i in edges.items():
		m_m = i[0].split(',')
		dot.edge(m_m[0], m_m[1], str(list(i[1])))
	dot.render(str(path.realpath(path.dirname(argv[0]))) + '/schemes/' + 'img1')
