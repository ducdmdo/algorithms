function destroyer(arr) {

    var valsToRemove = Array.from(arguments).slice(1);
    console.log(valsToRemove);
    let resultArray =[];
    return resultArray = arr.filter(item => !valsToRemove.includes(item));
  }

  function destroyer(arr) {
    let valsToRemove = Object.values(arguments).slice(1);
  
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < valsToRemove.length; j++) {
        if (arr[i] === valsToRemove[j]) {
          delete arr[i];
        }
      }
    }
    return arr.filter(item => item !== null);
  }

  function destroyer(arr) {
    var valsToRemove = Array.from(arguments).slice(1);
    return arr.filter(function(val) {
      return !valsToRemove.includes(val);
    });
  }