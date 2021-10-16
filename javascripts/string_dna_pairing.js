function pairElement(str) {
    let resultArray = [];
    //Iterate through item in input string
    //Add a missing item in the pair accordingly to the second Array. Notes: base paris: AT, CG
    //Add pairs into resultArray
    resultArray = str.split("")
                  .map(item => (item === "A") ?["A", "T"] : 
                                ((item === "T" ? ["T","A"]:
                                (item === "C" ? ["C","G"] :
                                (item === "G") ? ["G","C"]: "G")))
                                );
  
  
    //Return pairs result of AT and CG.Input ("ATCGA") 
    //=> Output [["A","T"], ["T", "A"], ["C","G"],["G","C"],["A","T"]]
    // Output should be a 2 dimensions arrays
    return resultArray;
  }

  function pairElement(str) {
    //create object for pair lookup
    var pairs = {
      A: "T",
      T: "A",
      C: "G",
      G: "C"
    };
    //split string into array of characters
    var arr = str.split("");
    //map character to array of character and matching pair
    return arr.map(x => [x, pairs[x]]);
  }
  
  
  console.log(pairElement("ATCGA"));

  function pairElement(str) {
    // Return each strand as an array of two elements, the original and the pair.
    var paired = [];
  
    // Function to check with strand to pair.
    var search = function(char) {
      switch (char) {
        case "A":
          paired.push(["A", "T"]);
          break;
        case "T":
          paired.push(["T", "A"]);
          break;
        case "C":
          paired.push(["C", "G"]);
          break;
        case "G":
          paired.push(["G", "C"]);
          break;
      }
    };
  
    // Loops through the input and pair.
    for (var i = 0; i < str.length; i++) {
      search(str[i]);
    }
  
    return paired;
  }
  