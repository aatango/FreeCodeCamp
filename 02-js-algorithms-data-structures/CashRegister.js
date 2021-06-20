function checkCashRegister(price, cash, cid) {
	let sid = 0; //Sum in drawer
	let answer = {"status": 0, "change": []};
	let change = cash - price;
	let denom = {
		'ONE HUNDRED': 100.00,
		'TWENTY': 20.00,
		'TEN': 10.00,
		'FIVE': 5.00,
		'ONE': 1.00,
		'QUARTER': 0.25,
		'DIME': 0.1,
		'NICKEL': 0.05,
		'PENNY': 0.01
	}
	for (let i = 0; i < cid.length; i++) {
		id += cid[i][1] * 100;
	}
	sid /= 100;
	if (sid < change) {
		answer.status = "INSUFFICIENT_FUNDS";
		return answer;
	} else if (sid === change) {
		answer.status= 'CLOSED';
		answer.change = cid;
		return answer;
	} else {
		cid = cid.reverse();
		let changeArr = [];
		for (let i = 0; i < cid.length; i++) {
			let denomI = denom[cid[i][0]];
			if (cid[i][1] > 0 && change > denomI) {
				let min = Math.min(Math.floor(change / denomI), cid[i][1] / denomI);
				changeArr.push([cid[i][0], min * denomI]);
				change -= min * denomI;
				change = Math.round(change * 100) / 100;
			}
		}
		for (let i = 0; i < changeArr.length; i++) {
			sid += changeArr[i][1] * 100;
		}
		sid /= 100;
		if (sid < change) { 
			answer.status = "INSUFFICIENT_FUNDS";
			return answer;
		} else {
			answer.status= 'OPEN';
			answer.change = changeArr;
			return answer;
}}}


//input
checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);

