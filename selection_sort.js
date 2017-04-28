var unsorted_list = [7, 4, 2, 10, 13]
var sorted_list = []

// step 1: find idx of min
// step 2: swap min idx with i
// step 3: repeat until reached end of arr

for (var i = 0; i < unsorted_list.length; i++){
	for (var j = i+1; j < unsorted_list.length; j++){
		if (unsorted_list[i] < unsorted_list[j]) {
			var min_idx = unsorted_list[i];
			sorted_list.push(min_idx);
			console.log(sorted_list);
		}
		
		
	}
}