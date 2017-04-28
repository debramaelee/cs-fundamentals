Arr = [1, 2, 3, 4, 5]
Idx = 0;


function reverse(arr, idx) {
	console.log(arr)
	if (Math.floor(arr.length/2) <= idx){
		console.log(arr)
		return arr;
	}
	else {
		var temp = arr[idx]
		arr[idx] = arr[(arr.length-1) - idx]
		arr[(arr.length-1) - idx] = temp
		idx++
		return reverse(arr, idx)
		// return arr
	}
}

console.log(reverse(Arr, Idx));

