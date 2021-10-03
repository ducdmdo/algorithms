/*  
-- There are many way to reverse string
-- Using loop
-- Using Recursion
-- Using array
 */

/*
Reverse the provided string.

You may need to turn the string into an array before you can reverse it.

Your result must be a string.
 */

function reverseString(str) {
    let newString='';
    for (let i = str.length - 1; i >= 0 ; i --) {
        newString += str[i];
    }
    console.log(newString);
    return newString;
}

function reverseString(str) {
    console.log(str.charAt(str.length-1));
    return (str === '') ? '' :  reverseString(str.substr(1)) + str.charAt(0);
}
console.log(reverseString('Hello'));

function reverseString(str) {
    return str.split("").reverse().join("");
}
reverseString("hello");