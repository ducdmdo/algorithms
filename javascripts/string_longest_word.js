function findLongestWordLength(str) {
    let arrayResult = str.split(" ");
    let max = 0;
    console.log(arrayResult);
    for (let i = 0; i < arrayResult.length; i++){
        console.log(max);
        if (max <= arrayResult[i].length) {
            max = arrayResult[i].length;
        }
    }
    return max;
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));

function findLongestWordLength(s) {
    return s.split(' ')
        .reduce(function(longest, word) {
           return Math.max(longest, word.length)
        }, 0);
    }

function findLongestWordLength(str) {
        return Math.max(...str.split(" ").map(word => word.length));
    }

    function findLongestWordLength(str) {
        // split the string into individual words
        const words = str.split(" ");

        // words only has 1 element left that is the longest element
        if (words.length == 1) {
            return words[0].length;
        }

        // if words has multiple elements, remove the first element
        // and recursively call the function
        return Math.max(
            words[0].length,
            findLongestWordLength(words.slice(1).join(" "))
        );
    }

findLongestWordLength("The quick brown fox jumped over the lazy dog");