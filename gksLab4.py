from graphviz import Digraph
from os import stat, path
from sys import argv

def group_unique_oper(matrix): #finding unique items
	str_matrix_unique_elements = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if not matrix[i][j] in str_matrix_unique_elements:
				str_matrix_unique_elements.append(matrix[i][j])
	return str_matrix_unique_elements

def update_path(res_group, paths): #update graph
	cash_dollars = set()
	for i in res_group.keys():
		for k in res_group[i]:
			cash_dollars.clear()
			cash_dollars.add(k)
			for j in paths.keys():	
				if not paths[j].isdisjoint(cash_dollars):
					if i == j :
						paths[j].remove(k)
						if i in paths[j]:
							paths[j].remove(i)
						continue
					paths[j].remove(k)
					paths[j].add(i)
	return paths

def create_graph(matrix, group): #Graphing
	current_matrix = []
	for i in group:
		current_matrix.append(matrix[i])
	unique_elements = group_unique_oper(current_matrix)
	module_dict = {i:set() for i in unique_elements}
	for i in group:
		for elem in range(len(matrix[i])-1):
			module_dict[matrix[i][elem]].add(matrix[i][elem + 1])
	return module_dict, unique_elements
	
def create_module(module_dict, elements, finally_module, counter): #create a module, add the operation, remove from the graph
	for i in elements:
		key = 'M'+str(counter)
		module_dict[key] = module_dict[i]
		module_dict.pop(i)
		finally_module[key] = {i}
		counter += 1
	return module_dict, finally_module, counter

def chn_crt_module(module_dict, current, finally_module, counter): # создание модуля для 3, 4, 5
	imho = ['M'+str(i) for i in range(1, counter)]
	trash, key = [], ''
	current.sort(reverse=True)
	for i in current:
		trash.clear()
		for j in i:
			if j in imho:
				trash.append(j)
		if trash:
			key = min(trash)
			i.remove(key)
		if not key:
			key = 'M' + str(counter)
		if not key in module_dict:
			module_dict[key] = set()
		if not key in finally_module:
			finally_module[key] = set()
		for j in i:
			try:
				module_dict[key].update(module_dict[j])
				finally_module[key].update({j})
				module_dict.pop(j)
			except:
				continue
		if not trash:
			counter += 1
	return module_dict, finally_module, counter

def output_links(module_dict): #elements in which only the output connection
	current_matrix = []
	for i in module_dict.keys():
		check = False
		for j in module_dict.keys():
			if i == j:
				continue
			if i in module_dict[j]:
				check = True
		if check is False:
			current_matrix.append(i)
	return current_matrix

def input_links(module_dict): #elements in which only input connection
	current_matrix = []
	for i in module_dict.keys():
		if len(module_dict[i]) == 0:
				current_matrix.append(i)
	return current_matrix
	
def remove_module_input_output(elements, counter):
	imho = ['M'+str(i) for i in range(1, counter)]
	trash = []
	for i in elements:
		if i not in imho:
			trash.append(i)
	return trash

def strong_links(module_dict): #a->b, b->a
	current_matrix = []
	for i in module_dict.keys():
		for j in module_dict.keys():
			if i in module_dict[j]:
				if j in module_dict[i]:
					if not [j,i] in current_matrix:
						current_matrix.append([i,j])
	return current_matrix
	
def triple_links(value): #a->b, b->c
	str_chk = ''
	current = []
	battlecry = []
	return_value = []
	for i in value:
		condition = True
		for j in value:
			if i == j:
				continue
			if set(i).isdisjoint(set(j)) == False:
				condition = False
		if condition:
			current.append(i)
	for i in current:
		return_value.append(i)
		value.remove(i)
	current.clear()
	def merge_lists(lst1, lst2):
		for i in lst2:
			if i not in lst1:
				lst1.append(i)
		return lst1
	for i in value:
		current.clear()
		for j in value:
			if j == i:
				continue
			if not set(i).isdisjoint(set(j)):
				current.append(j[0])
				current.append(j[1])
		if current:
			battlecry = merge_lists(i, current)
			return_value.append(battlecry)
	for i in return_value:
		i.sort()
	current.clear()
	for i in return_value:
		if not i in current:
			current.append(i)
	return_value = current[:]
	current.sort()
	for i in current:
		for j in current:
			if i == j:
				continue
			if not set(i).isdisjoint(set(j)) and len(i) < len(j):
				return_value.remove(i)
	return return_value

def find_all_paths(graph, start, end, path=[]): 
	path = path + [start]
	if start == end:
		return [path]
	if not start in graph:
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				if len(newpath) > 2:
					paths.append(newpath)
	return paths
	
def outline(module): #finding the outlines
	return_paths, current = [], []
	for i in module.keys():
		for j in module[i]:
			return_paths.extend(find_all_paths(module, j, i ))
	for i in return_paths:
		i.sort()
	for i in return_paths:
		if i not in current:
			current.append(i)
	return_paths = current[:]
	current.sort()
	for i in current:
		for j in current:
			if i == j:
				continue
			if not set(i).isdisjoint(set(j)) and len(i) < len(j):
				try:
					return_paths.remove(i)
				except: 
					continue
	current = return_paths[:]
	for i in current:
		if len(i) < 3:
			return_paths.remove(i)
	return return_paths
	
def distant_branch(module): #5 x->a->b->c->y x->y
	current, paths = [], []
	swr = False
	for i in module.keys():
		paths.clear()
		for j in module[i]:
			if i == j:
				continue
			paths.extend(find_all_paths_bool(module,i, j))
		current.extend(paths)
	paths = current[:]
	for i in current:
		swr = False
		for j in i[1:-1]:
			if not find_input(module, j):
				swr = True
		if swr:
			paths.remove(i)
	return paths

def find_input(module, element): # an element that has only one input and one output
	trash = []
	for i in module.keys():
		if i == element:
			continue
		for j in module[i]:
			if j == element:
				trash.append(j)
	if len(trash) > 1:
		return False
	return True

def find_all_paths_bool(graph, start, end, path=[], dsb = False): #find chain between 2 operations
	path = path + [start]
	if start == end:
		return [path]
	if not start in graph:
		return []
	paths = []
	for node in graph[start]:
		if dsb:
			if node not in path and len(graph[start]) == 1:
				newpaths = find_all_paths_bool(graph, node, end, path, dsb = True)
				for newpath in newpaths:
					if len(newpath) > 2:
						paths.append(newpath)
			continue
		if node not in path:
			newpaths = find_all_paths_bool(graph, node, end, path, dsb = True)
			for newpath in newpaths:
				if len(newpath) > 2:
					paths.append(newpath)
	return paths
	
'''def check_exit(finally_module, unique_elements):
	current = []
	for i in finally_module.values():
		current.extend(list(i))
	current.sort()
	if current == unique_elements:
		return False
	else:
		return True
'''

def draw_graph(module, namefile, iteration):
	nodes = module.keys()
	dot = Digraph(comment='Module GKS4', format='png')
	for i in nodes:
		dot.node(i)
	for i in module.keys():
		for j in module[i]:
			dot.edge(i, j)
	dot.render(str(path.realpath(path.dirname(argv[0]))) + '/modules/' + str(namefile) + '_iteration' + str(iteration))
	return iteration + 1

def draw_graph_create_module(matrix, group, namefile_group):
	finally_module = {}
	unique_elements = []
	current = []
	counter = 1
	namefile_number = 1
	module, unique_elements = create_graph(matrix, group)
	namefile_number = draw_graph(module, namefile_group, namefile_number)
	while 1:
		current.clear()
		#1
		current1 = output_links(module)
		current1 = remove_module_input_output(current1, counter)
		if current1:
			module, finally_module, counter = create_module(module, current1, finally_module, counter)
			module = update_path(finally_module, module)
			namefile_number = draw_graph(module, namefile_group, namefile_number)
		#2
		current2 = input_links(module)
		current2 = remove_module_input_output(current2, counter)
		if current2:
			module, finally_module, counter = create_module(module, current2, finally_module, counter)
			module = update_path(finally_module, module)
			namefile_number = draw_graph(module, namefile_group, namefile_number)
		#3
		current3 = strong_links(module)
		current3 = triple_links(current3)
		if current3:
			module, finally_module, counter = chn_crt_module(module, current3, finally_module, counter)
			module= update_path(finally_module, module)
			namefile_number = draw_graph(module, namefile_group, namefile_number)
		#4
		current4 = outline(module)
		if current4:
			module, finally_module, counter = chn_crt_module(module, current4, finally_module, counter)
			module = update_path(finally_module, module)
			namefile_number = draw_graph(module, namefile_group, namefile_number)
		#5
		current5 = distant_branch(module)
		if current5:
			module, finally_module, counter = chn_crt_module(module, current5, finally_module, counter)
			module = update_path(finally_module, module)
			namefile_number = draw_graph(module, namefile_group, namefile_number)
		if not current1 and not current2 and not current3 and not current4 and not current5:
			check = False
			imho = ['M'+str(i) for i in range(1, counter)]
			for i in module.keys():
				if i not in imho:
					current.append(i)
			if current:
				module, finally_module, counter = create_module(module, current, finally_module, counter)
				module = update_path(finally_module, module)
				namefile_number = draw_graph(module, namefile_group, namefile_number)
			break
	return finally_module
