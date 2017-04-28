def binarySearch(array, target):
	# Return idx of target if the value exists
	# Return None if the value does not exist

	start = 0
	end = len(array)

	while start < end:
		
		mid = start + ((end - start) // 2)

		if array[mid] == target:
			return mid
			
		elif array[mid] > target:
			#reassign end value
			end = mid
			pass

		elif array[mid] < target:
			#reassign start value
			start = mid
			pass

	return None

print('Index: ' + str(binarySearch([1, 5, 8, 10], 11)))