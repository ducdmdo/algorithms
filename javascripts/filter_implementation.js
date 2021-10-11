let s = [23,65,98,5];

Array.prototype.myFilter = function(callback) {
    var newArray = [];
    for (let i = 0; i < this.length; i ++) {
        if (callback(this[i]) === true) {
            newArray.push(this[i]);
        }
    }
    return newArray;
};

Array.prototype.myFilter = function(callback){
    // Only change code below this line
    let newArray = [];
    this.forEach(function(x) {
      if (callback(x) == true) {
        newArray.push(x);
      }
    });
    // Only change code above this line
    return newArray;
  };