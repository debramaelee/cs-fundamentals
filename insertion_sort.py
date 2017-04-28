def insertion_sort(list):
	# return a sorted list.
	# step 1: take the 2nd item, compare to first. 
	# for i in range(len(list)):
	# 	j = i - 1
	# 	while j > 0:
	# 		if list[i+1] < list[i]:
	# 			list.insert(i, list[i+1])
	# 			del list[i+2]
	# 			print list
	# 		else:
	# 			break

	####
	for index in range(1, len(list)):
		currentval = list[index]
		print currentval
		position = index
		print position

		while position > 0 and list[position-1] > currentval:
			
			list[position] = list[position-1]
			position = position-1
		list[position] = currentval


my_array = [54,26,93,17,77,31,44,55,20]
print my_array
print(insertion_sort(my_array))