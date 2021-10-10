function chunkArrayInGroups(arr, size) {

    let resultArray = [];
    if (arr.length <= size) {
        resultArray.push(arr);
    } else {
        for (let i = 0; i < arr.length; i+=size) {
            resultArray.push(arr.slice(i, i+size));
        }
    }
    return resultArray;
  }

  function chunkArrayInGroups(arr, size) {
    // Break it up.
    let newArr = [];
    let i = 0;
  
    while (i < arr.length) {
      newArr.push(arr.slice(i, i + size));
      i += size;
    }
    return newArr;
  }


  function chunkArrayInGroups(arr, size) {
    let newArr = [];
    while (arr.length > 0) {
      newArr.push(arr.splice(0, size));
    }
    return newArr;
  }

  function chunkArrayInGroups(arr, size) {
    if (arr.length <= size) {
      return [arr];
    } else {
      return [arr.slice(0, size)].concat(
        chunkArrayInGroups(arr.slice(size), size)
      );
    }
  }
  

  function chunkArrayInGroups(arr, size) {
    let temp = [];
    let result = [];
  
    for (let a = 0; a < arr.length; a++) {
      if (a % size !== size - 1) temp.push(arr[a]);
      else {
        temp.push(arr[a]);
        result.push(temp);
        temp = [];
      }
    }
  
    if (temp.length !== 0) result.push(temp);
    return result;
  }

  
  chunkArrayInGroups(["a", "b", "c", "d"], 2);


  chunkArrayInGroups(["a", "b", "c", "d"], 2);
  console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));