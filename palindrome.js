let aString1 = "hello"
let aString2 = "racecar"

function isItPalin(aString) {
	//find loop stopping point
	let halfOfString = Math.floor(aString.length/2)

	for (var i = 0; i <= halfOfString; i++) {
		if (aString[i] !== aString[aString.length-1-i]) {
			return false;
		}

		else if (aString[i] === aString[aString.length-1-i] && i === halfOfString) {
			return true
		}
	}
}

console.log(isItPalin(aString1));
//returns false

console.log(isItPalin(aString2));
//resturns true