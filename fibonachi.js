//fibonachi

var arr = [0, 1]
while(arr[arr.length-1] + arr[arr.length-2] <= 100) {
	var L = arr.length;
	arr.push(arr[L-1] + arr[L-2])
	console.log(arr)
}

