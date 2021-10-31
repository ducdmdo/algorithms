function telephoneCheck(str) {
    let firstRex = /^(1\s?)?\d{3}([-\s]?)\d{3}\2\d{4}$/
    let secondRex = /^(1\s?)?\(\d{3}\)\s?\d{3}[-\s]?\d{4}$/;
  
      return (firstRex.test(str)) ? true :
        secondRex.test(str) ? true :
        false;
  }
  
  console.log(telephoneCheck("555-555-5555"));