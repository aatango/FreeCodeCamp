function updateInventory(arr1, arr2) {
    arr2.forEach(nI => {
        let i = 0;
        while (i < arr1.length) {
            if (nI[1] == arr1[i][1]) {
                arr1[i][0] += nI[0];
                return;
            } else if(nI[1] < arr1[i][1]) {
                arr1.splice(i, 0, nI)
                return;
            }
        i++;
        }
        arr1.push(nI);
    })
    console.log(arr1);
    return arr1;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
