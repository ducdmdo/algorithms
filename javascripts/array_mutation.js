function mutation(arr) {
    let firstItem = arr[0].toLowerCase();
    let secondItem = arr[1].toLowerCase();
    for (let i = 0; i< secondItem.length; i++) {
        if (firstItem.indexOf(secondItem[i]) < 0) return false;
    }
    return true;
}

function mutation(arr) {
    return arr[1]
      .toLowerCase()
      .split("")
      .every(function(letter) {
        return arr[0].toLowerCase().indexOf(letter) != -1;
      });
  }

function mutation([ target, test ], i = 0) {
    target = target.toLowerCase();
    test = test.toLowerCase();
    return i >= test.length
      ? true
      : !target.includes(test[i])
        ? false
        : mutation([ target, test ], i + 1);
  }

console.log(mutation("Hello", "h"));
console.log(mutation("Hello", "hey"));
mutation(["hello", "hey"]);