function telephoneCheck(str) {
	if (str.match(/[\d]/g).length == 10 ||
	(str.match(/[\d]/g).length == 11 & str.match(/^1/))) {
		if (str.match(/\(/) || str.match(/\)/)) {
			if(str.match(/\(...\)/g)) {
				let strMatch = str.match(/\(...\)/g);
				for (let i = 0; i < strMatch.length; i++) {
					if (!strMatch[i].match(/\(\d\d\d\)/g)) {
						return false;
					}
				}
				return true;
			} else { return false; }
		}
		return true;
	}
	return false;
}


telephoneCheck("(555)5(55?)-5555");

