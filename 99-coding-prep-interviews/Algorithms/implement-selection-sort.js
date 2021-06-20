function minIndex(arr) {
  let minI = 0;
  for (let i = 0 ; i < arr.length; i++) {
    if (arr[i] < arr[minI]) minI = i;
  }
  return minI;
}

function selectionSort(array) {
  for (let i = 0; i < array.length; i++) {
    let j = minIndex(array.slice(i));
    [array[i], array[j + i]] = [array[j + i], array[i]];
  }
  return array;
}


selectionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
