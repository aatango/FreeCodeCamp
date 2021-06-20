function bubbleSort(array) {
  /*
  Iterate through array checking two adjacent items, swaping them if in decreasing order.
  If iterable is used, then changes had to be made, and at least one more run is needed.
  Last run is used to check sort.
  */

  let it = array[0]; // initial declaration of iterable, allocating appropriate size.

  for (let j = 1; j < array.length && it != undefined; j++) {
    it = undefined;
    for (let i = 0; i < array.length - j; i++) {
      if (array[i] > array[i + 1]) {
        it = array[i + 1];
        array[i + 1] = array[i];
        array[i] = it;
      }
    }
  }
  return array;
}

bubbleSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
