unsorted_list = [7, 4, 2, 10, 13]
sorted_list = []

# step 1: find idx of min
# step 2: swap min idx with i
# step 3: repeat until reached end of arr

def selection_sort(unsorted_list):
	for i in range(0, len(unsorted_list)):
		min_val = unsorted_list[i]

		for j in range(i, len(unsorted_list)):
			if unsorted_list[j] < min_val:
				min_val = unsorted_list[j]
				min_idx = j

		unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]

	return unsorted_list

