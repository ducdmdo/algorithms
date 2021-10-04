function largestOfFour(arr) {
    let resultArray=[];
    for (let i = 0; i < arr.length; i++) {
        console.log(Math.max(...arr[i]));
        resultArray.push(Math.max(...arr[i]));
    }
    return resultArray;
}

function largestOfFour(arr) {
    let result = [];
    for (i = 0; i < arr.length; i ++) {
        let largestNumber = arr[i][0]; /* set largestNumber base is the first number*/
        for (j = 1; j < arr[i].length; j ++) {
            if (arr[i][j] > largestNumber) {
                largestNumber = arr[i][j];
            }
        }
        result[i] = largestNumber;
    }
    return result;
}

function largestOfFour(arr) {
    return arr.map(function(group) {
        return group.reduce(function(prev, current) {
        return current > prev ? current : prev;
        });
    });
    }

    function largestOfFour(arr) {
        return arr.map(Function.apply.bind(Math.max, null));
    }

    function largestOfFour(arr, finalArr = []) {
        return !arr.length
            ? finalArr
            : largestOfFour(arr.slice(1), finalArr.concat(Math.max(...arr[0])))
        }

console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));