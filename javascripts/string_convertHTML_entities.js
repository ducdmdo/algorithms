function convertHTML(str) {
    //return a string in which convert some character to the corresponding HTML entities
    //& => &amp;
    //< => &lt;
    //> => &gt
    //" => &quot;
    //' => &apos;
    let inputArray = str.split("");
    let resultArray = [];
    for (let i = 0; i < inputArray.length; i ++) {
      switch (inputArray[i]) {
        case "&":
          inputArray[i] = "&amp;";
          break;
        case "<":
          inputArray[i] = "&lt;";
          break;
        case ">":
          inputArray[i] = "&gt;";
          break;
        case "\"":
          inputArray[i] = "&quot;";
          break;
        case "'":
          inputArray[i] = "&apos;";
          break;
      }
        
    }
    return inputArray.join("");
  }
  console.log(convertHTML("Dolce & Gabbana"));

  function convertHTML(str) {
    // Use Object Lookup to declare as many HTML entities as needed.
    const htmlEntities = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&apos;"
    };
    // Using a regex, replace characters with it's corresponding html entity
    return str.replace(/([&<>\"'])/g, match => htmlEntities[match]);
  }

  function convertHTML(str) {
    // Use Object Lookup to declare as many HTML entities as needed.
    const htmlEntities = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&apos;"
    };
    //Use map function to return a filtered str with all entities changed automatically.
    return str
      .split("")
      .map(entity => htmlEntities[entity] || entity)
      .join("");
  }
  
  // test here
  convertHTML("Dolce & Gabbana");