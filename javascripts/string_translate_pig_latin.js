function translatePigLatin(str) {
    let consonantRegex = /^[^aeiou]+/;
    let myConsonants = str.match(myConsonants);
    return myConsonants !== null
    ? str
        .replace(consonantRegex, "")
        .concat(myConsonants)
        .concat("ay")
    : str.concat("way");
}

function translatePigLatin(str) {
    //Create variable to be used
    let pigLatin ="";
    let regex = /[aeiou]/gi;

    //check if the first character is a vowel
    if (str[0].match(regex)) {
        pigLatin = str + "way";
    } else if (str.match(regex) === null) {
        // check if the string contains only consonants
        pigLatin = str + "ay";
    } else {
        // Find how many consonants before the first vowel.
        let vowelIndice = str.indexOf(str.match(regex)[0]);
        console.log(vowelIndice);

        // Take the string from the first vowel to the last char
        // then add the consonants that were previously omitted and add the ending.
        pigLatin = str.substr(vowelIndice) + str.substr(0, vowelIndice) + "ay";
    }
    return pigLatin;
}

function translatePigLatin(str) {
    if (str.match(/^[aeiou]/)) return str + "way";

    const consonantCluster = str.match(/^[^aeiou]+/)[0];

    return str.substr(consonantCluster.length) + consonantCluster + "ay";
}

function translatePigLatin(str) {
    return str
      .replace(/^[aeiou]\w*/, "$&way")
      .replace(/(^[^aeiou]+)(\w*)/, "$2$1ay");
  }

  function translatePigLatin(str, charPos = 0) {
    return ['a', 'e', 'i', 'o', 'u'].includes(str[0])
      ? str + (charPos === 0 ? 'way' : 'ay')
      : charPos === str.length
        ? str + 'ay'
        : translatePigLatin(str.slice(1) + str[0], charPos + 1);
  }