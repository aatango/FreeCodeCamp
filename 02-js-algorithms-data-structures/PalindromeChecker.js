function palindrome(str) {
		str = str.toLowerCase().match(/[a-z0-9]/g).join("")
			let invStr = str.split("").reverse().join("");
				return str == invStr;
}


palindrome("race car");

