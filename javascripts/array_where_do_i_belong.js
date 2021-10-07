
/* This function can be optimized better by divide into 2 part */
function getIndexToIns(arr, num) {
    arr.sort((a,b) => a-b);
    for (let i = 0; i < arr.length; i ++) {
        if (arr[i] >= num) return i;
    }
    return arr.length;

}
/* Count the number of entries that are smaller than the new value num
The new value would be inserted after these values
 */

function getIndexToIns(arr, num) {
    return arr.filter(val => num > val).length;
  }

  function getIndexToIns(arr, num) {
    // sort and find right index
    let index = arr
      .sort((curr, next) => curr - next)
      .findIndex(currNum => num <= currNum);
    // Returns index or total length of arr
    return index === -1 ? arr.length : index;
  }

  function getIndexToIns(arr, num) {
    return arr
      .concat(num)
      .sort((a, b) => a - b)
      .indexOf(num);
  }
getIndexToIns([40, 60], 50);