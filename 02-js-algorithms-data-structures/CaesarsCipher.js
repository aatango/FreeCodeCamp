function rot13(str) {
	let key = 13;
	let decoded = '';
	for (let i = 0; i < str.length; i++) {
	if (str.charCodeAt(i) > 64 & str.charCodeAt(i) < 91) {
		decoded += String.fromCharCode((str.charCodeAt(i) - 65 + key) % 26 + 65);
	} else {
		decoded += str[i];
	}
	}
	return decoded;
}


rot13("SERR PBQR PNZC");

