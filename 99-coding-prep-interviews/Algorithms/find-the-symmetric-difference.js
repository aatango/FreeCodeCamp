function sym(...args) {
  let diffSet = new Set(args[0])

  for (let i = 1; i < args.length; i++) {
    let setB = new Set(args[i]);

    Array.from(setB).forEach(int => {
      if (diffSet.has(int)) {
        diffSet.delete(int);
      } else {
        diffSet.add(int);
      }
    })
  }
  return Array.from(diffSet);
}

sym([1, 2, 5], [2, 3, 5], [3, 4, 5]);
