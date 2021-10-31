function palindrome(str) {

    //lower cases all the letters remove all non-alphanumberic characters
    str = str.toLowerCase().replace(/[\W_]+/g,"");
    console.log(str);
    let result = true;
    let j = 0;

    //verify the palindrome string
    for (let i = 0; i < str.length - 1; i++) {
        if (str[i] !== str[str.length-1 - j]){
            result = false;
        }
        j++;
    }
    return result;
    }

    console.log(palindrome("not a palindrome"));
    

    