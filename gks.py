from numpy import int16, zeros, amax

#подсчет количества уникальных операций
def count_unique(matrix):
	str_matrix_unique_elements = ''
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if not matrix[i][j] in str_matrix_unique_elements:
				str_matrix_unique_elements = str_matrix_unique_elements + matrix[i][j]
	return int(len(str_matrix_unique_elements)/2)
	
#подсчет не встречающихся операций в строках 
def  count_diff(matrix, K, len_matrix):
	res_list = []
	res_dict = {}
	for i in range(len(matrix)):
		if i == len_matrix:
			break
		res_list.append({(i, j): K - int(len(set(matrix[i]).symmetric_difference(set(matrix[j])))) for j in range(i , len_matrix) if i != j})
	for i in res_list:
		if(type(i) == dict):
			res_dict.update(i)
	return res_dict

#форматированние вывода в виде квадратичной матрицы
def matrix_output(matrix, len_matrix):
	result_matrix = zeros((len_matrix,len_matrix), dtype=int16)
	for i in range(len_matrix):
		for j in range(len_matrix):
			if (i, j) in matrix.keys():
				result_matrix[i,j] = matrix[(i, j)]
				result_matrix[j, i] = matrix[(i, j)]
	return result_matrix

#составление групп
def grouped(matrix):
	result_group = set()
	condition_group = set()
	x = []
	our_group = {x for x in range(len(matrix))}
	while len(condition_group) != len(matrix):
		if len(our_group) - len(condition_group) <= 2:
			x.append(our_group.difference(condition_group))
			break
		condition = True
		position = []
		result_group.clear()
		max_elem = amax(matrix)
		for i in range(len(matrix)): #находим индексы всех макс элементов
			for j in range(len(matrix)):
				if matrix[i][j] == max_elem:
					position.append((i,j))
		result_group.update(set(position[0]))
		matrix[position[0][0]][position[0][1]] = 0
		if (len(result_group.difference(condition_group)) < 2):
			continue
		if len(position) > 1:
			for i in range(len(position) - 1):
				i += 1
				if not result_group.isdisjoint(set(position[i])) and result_group.isdisjoint(condition_group):  #записуем другие индексы на пересечение первых индексов
					result_group.update(set(position[i]))
					matrix[position[i][0]][position[i][1]] = 0
		if len(result_group.difference(condition_group)) != 0:
			x.append(result_group.difference(condition_group)) #добавляем всю группу в список групп
		condition_group.update(result_group)
	l = {x.index(i)+1:i for i in x}
	return(l)

#3 лабораторная, изменение групп
def gks3(input_data, matr):
	def sortByLength(inputStr):
		return len(inputStr)
	while True:
		if len(input_data) < 2:
			break
		input_items = list(input_data.items())
		list_res = []
		for i in input_items:
			str_bush = ''
			str_bush += str(i[0]) + ','
			for j in i[1]:
				for n in matr[j]:
					if not n in str_bush:
						str_bush += n + ','
			str_bush = str_bush[:-1]
			list_res.append(str_bush.split(','))
		list_res.sort(key=sortByLength, reverse=True)
		#print(list_res)
		str_chk = ''
		for i in range(len(list_res)):
			for j in range(len(list_res)):
				if j <= i or str(list_res[j][0]) in str_chk:
					continue
				heading = int(list_res[i][0])
				second = int(list_res[j][0])
				if set(list_res[j][1:]).issubset(set(list_res[i][1:])):
					input_data[heading].update(input_data[second])
					str_chk += str(second)
					input_data.pop(second)
					continue
				trash = []
				if  str(second) not in str_chk:
					for f in input_data[second]:
						if set(matr[f]).issubset(set(list_res[i][1:])):
							input_data[heading].add(f)
							trash.append(f)
							str_chk += str(f)
					for q in trash:
						input_data[second].remove(q)
				if len(trash) > 0:
					continue
		break
	x = list(input_data.values())
	x.sort(key=sortByLength, reverse=True)
	l = {x.index(i)+1:i for i in x}
	return(l)

def unique_module(module):
	list_operations = []
	trash = []
	for i in module.values():
		for j in i.values():
			list_operations.append(j)
	for i in list_operations:
		for j in list_operations:
			if i == j:
				continue
			if i.issubset(j) and i not in trash:
				trash.append(i)
	for i in trash:
		list_operations.remove(i)
	list_operations.sort()
	for i in list_operations:
		for j in list_operations:
			if i == j or len(j) > len(i):
				continue
			for u in j:
				if u in i:
					i.remove(u)
	trash.clear()
	for i in list_operations:
		if i not in trash:
			trash.append(i)
	un_mod = {}
	incr = 1
	for i in trash:
		key = 'M' + str(incr)
		un_mod[key] = i
		incr += 1
	return un_mod
	
if __name__ == '__main__':
		print("GKS.py")
		input("Press any key.")