function fearNotLetter(str) {
  
    //Identify range
    let baseRange = "abcdefghijklmnopqrstuvwxyz";
  
    //Identify which letter are not in range
    //Identify the first and the last letter then compare with the base range
    //Identify the sub-base range
  
    let firstLetter = str[0];
    let lastLetter = str[str.length-1];
    let subBaseRange = baseRange.slice(baseRange.indexOf(firstLetter), baseRange.indexOf(lastLetter) + 1);
  
    //return missing letter which are not in range
    //Input: abce => output:d
    if (str === subBaseRange) return undefined;
    
    return subBaseRange.split("")
              .filter (item => str.indexOf(item) === -1)
              .join("");
  
  }
  
  console.log(fearNotLetter("abce"));

  function fearNotLetter(str) {
    for (var i = 0; i < str.length; i++) {
      /* code of current character */
      var code = str.charCodeAt(i);
  
      /* if code of current character is not equal to first character + no of iteration
          hence character has been escaped */
      if (code !== str.charCodeAt(0) + i) {
        /* if current character has escaped one character find previous char and return */
        return String.fromCharCode(code - 1);
      }
    }
    return undefined;
  }

  function fearNotLetter(str) {
    let currCharCode = str.charCodeAt(0);
    let missing = undefined;
  
    str
      .split("")
      .forEach(letter => {
        if (letter.charCodeAt(0) === currCharCode) {
          currCharCode++;
        } else {
          missing = String.fromCharCode(currCharCode);
        }
      });
  
    return missing;
  }

  function fearNotLetter(str) {
    for (let i = 1; i < str.length; ++i) {
      if (str.charCodeAt(i) - str.charCodeAt(i - 1) > 1) {
        return String.fromCharCode(str.charCodeAt(i - 1) + 1);
      }
    }
  }

  function fearNotLetter(str) {
    var allChars = "";
    var notChars = new RegExp("[^" + str + "]", "g");
  
    for (var i = 0; allChars[allChars.length - 1] !== str[str.length - 1]; i++)
      allChars += String.fromCharCode(str[0].charCodeAt(0) + i);
  
    return allChars.match(notChars)
      ? allChars.match(notChars).join("")
      : undefined;
  }
  