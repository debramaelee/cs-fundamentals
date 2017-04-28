var array = [11, 13, 6, 69, 100];
var target = 69;

for (var i = 0; i <= array.length; i) {
	if (array[i] === target) {
		console.log('Yes it exists in index ' + i);
		break;
	}
	else {
		i++;
	}
}

//using recursion
def linear_search(arr, current_idx, value) {
	if (arr[i] === value) {
		return i
	}
	if (current_idx + 1 >= arr.length) {
		return False // or -1
	}
	else {
		current_idx ++
		linear_search(arr, current_idx, value)
	}
}