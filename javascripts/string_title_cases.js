function titleCase(str) {
    let array = str.split();
    let result = '';
    for (let i = 0; i < array.length; i++) {
        let strLower = array[i].toLowerCase();
        result += array[i].replaceAt(0, array[i].charAt(0).toUpperCase());
    }
    return result;

}

function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)\S/g, L => L.toUpperCase());
  }

function titleCase(str) {
    var convertToArray = str.toLowerCase().split(" ");
    var result = convertToArray.map(function(val) {
      return val.replace(val.charAt(0), val.charAt(0).toUpperCase());
    });
    return result.join(" ");
  }
  
  String.prototype.replaceAt = function(index, character) {
    return (
      this.substr(0, index) + character + this.substr(index + character.length)
    );
  };
  
  function titleCase(str) {
    var newTitle = str.split(" ");
    var updatedTitle = [];
    for (var st in newTitle) {
        let strLower = newTitle[st].substr(1).toLowerCase();
        updatedTitle[st] = newTitle[st][0].toUpperCase() + strLower ;
    }
    return updatedTitle.join(" ");
}