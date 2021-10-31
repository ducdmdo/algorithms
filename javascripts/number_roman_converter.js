function convertToRoman(num) {
    var numeral = "";
     var arr = [
     {number:1, roman: "I"},
     {number:4, roman: "IV"},
     {number:5, roman: "V"},
     {number:9, roman: "IX"},
     {number:10, roman: "X"},
     {number:40, roman: "XL"},
     {number:50, roman: "L"},
     {number:90, roman: "XC"},
     {number:100, roman: "C"},
     {number:400, roman: "CD"},
     {number:500, roman: "D"},
     {number:900, roman: "CM"},
     {number:1000, roman: "M"}
     ]
     while(num > 0){
      var searching = arr.filter(function(myArr){
        if(myArr.number <= num){
          return myArr.number
        }
      })
      var latest = searching.pop()
      var full = Math.floor(num / latest.number)
      for(let i = 0; i<full; i++){
        numeral +=latest.roman
      }
      num = num % latest.number
     }
     return numeral 
    }
    
    console.log(convertToRoman(36));

    function roman_to_Int(str1) {
        if(str1 == null) return -1;
        var num = char_to_int(str1.charAt(0));
        var pre, curr;
        
        for(var i = 1; i < str1.length; i++){
        curr = char_to_int(str1.charAt(i));
        pre = char_to_int(str1.charAt(i-1));
        if(curr <= pre){
        num += curr;
        } else {
        num = num - pre*2 + curr;
        }
        }
        
        return num;
        }
        
        function char_to_int(c){
        switch (c){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return -1;
        }
        }
        console.log(roman_to_Int('XXVI'));
        console.log(roman_to_Int('CI'));

    