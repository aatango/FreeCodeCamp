function convertToRoman(num) {
	let romanNum = [];
	let romanKeys = [
		{'M': 1000},
		{'CM': 900},
		{'D': 500},
		{'CD': 400},
		{'C': 100},
		{'XC': 90},
		{'L': 50},
		{'XL': 40},
		{'X': 10},
		{'IX': 9},
		{'V': 5},
		{'IV': 4},
		{'I': 1}
	];
	let i = 0;
	while (i < romanKeys.length) {
		//console.log(num, Object.values(romanKeys[i]), i)
		if ((num - Object.values(romanKeys[i])) >= 0) {
			num = num - Object.values(romanKeys[i]);
			romanNum.push(Object.keys(romanKeys[i]));
		} else { i++ };
	}
	return romanNum.join('');
}


convertToRoman(1000);

