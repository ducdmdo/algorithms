/*********************************************************/
//Reduce
// executes a user-supplied "reducer" callback function on each element of the array, passing in the return value from the calculation on the preceding element.
// The final result of running the reducer across all elements of the array is a singe value.
/*********************************************************/

// sum of all the elements in an array

const array1 =[1,2,3,4];
console.log(array1.reduce((initialResult, currentValue) => initialResult + currentValue));


// Test initialValue
let testInitialValue = [1,100].reduce((initialResult, currentItem) => Math.max(initialResult, currentItem)); //100
let testInitialValue = [1,100].reduce((initialResult, currentItem) => Math.max(initialResult, currentItem, 99)); //100
let testInitialValue = [1,100].reduce((initialResult, currentItem) => Math.max(initialResult, currentItem, 101)); //101

// 1. If the array only has one element and no initialValue is provided, or if initialValue is provided but the array is empty => no callback functioned involved
let testInitialValue = [50].reduce((initialResult, currentItem) => Math.max(initialResult, currentItem, 101));
console.log(testInitialValue);


//2. To sum up the values contained in an array of objects, you must supply an initialValue, so that each item passes through your function.
let sum = [{x:1}, {x:2}, {x:3}].reduce((intialResult, currentItem) => initialResult + currentItem[x], 0)
console.log(sum)


//3. Flatten an array of arrays
let flattened = [[0,1],[2,3],[4,5]].reduce((previousValue, currentValue) => previousValue.concat(currentValue),[]);
console.log(flattened);

//4. Counting instances of values in an object
let countedNames = ['Alice','Bob', 'Tiff', 'Bruce', 'Alice'].reduce(function(initialResult, currentValue) 
{if (currentValue in initialResult) {
    initialResult[currentValue]++;
}else {
    initialResult[currentValue] = 1;
}
return initialResult
} ,{});
console.log(countedNames);

//5. Grouping objects by a property
let people = [
    {name: 'Alice', age:21},
    {name: 'Max', age:20},
    {name: 'Jane', age:20}
];
function groupBy (objectArray, property) {
    return objectArray.reduce(function (iniatialResult, currentValue) {
        let key = currentValue[property];
        console.log("key value: " + key);
        if (!iniatialResult[key]) {
            iniatialResult[key] = [];
        }
        iniatialResult[key].push(currentValue);

        return iniatialResult;
    },{})
}

let groupedPeople = groupBy(people, 'age');
console.log(groupedPeople);

//6.  Bonding arrays contained in an array of objects using the spread operator and initialValue
// friends - an array of object
// where object field 'books' is a list of favorite books

let friends = [{
    name: 'Anna',
    books: ['Bible', 'Harry Potter'],
    age: 21
}, {
    name: 'Alice',
    books: ['War and peace', 'Remeo and Juliet'],
    age: 26
},{
    name: 'Bob',
    books: ['The Lord of the Rings', 'The Shining'],
    age:18
}];
let allBooks = friends.reduce((previousValue, currentValue) => [...previousValue, ...currentValue.books],[]);
console.log(allBooks);

//7. Remove duplication items in an array
let myArray = ['a','b','a','b','c','e','e','c','d','d','d','d'];
let myArrayWithNoDuplicates = myArray.reduce(function(previousResult, currentValue) {
    if (previousResult.indexOf(currentValue) === -1) {
        previousResult.push(currentValue);
    }
    return previousResult;
},[])

console.log(myArrayWithNoDuplicates);

//8. Replace .filter().map() with .reduce()
const numbers = [-5, 6,2,0];

const doublePositiveNumbers = numbers.reduce((previousResultValue, currentValue) => {
    if (currentValue > 0) {
        const doubled = currentValue * 2;
        previousResultValue.push(doubled);
    }
    return previousResultValue;
}, []);

console.log(doublePositiveNumbers);

//9.  Running Promises in Sequence
/**
* Runs promises from array of functions that can return promises
* in chained manner
*
* @param {array} arr - promise arr
* @return {Object} promise object
*/
function runPromiseInSequence(arr, input) {
return arr.reduce(
(promiseChain, currentFunction) => promiseChain.then(currentFunction),
Promise.resolve(input)
)
}

// promise function 1
function p1(a) {
return new Promise((resolve, reject) => {
resolve(a * 5)
})
}

// promise function 2
function p2(a) {
return new Promise((resolve, reject) => {
resolve(a * 2)
})
}

// function 3  - will be wrapped in a resolved promise by .then()
function f3(a) {
return a * 3
}

// promise function 4
function p4(a) {
return new Promise((resolve, reject) => {
resolve(a * 4)
})
}

const promiseArr = [p1, p2, f3, p4]
runPromiseInSequence(promiseArr, 10)
.then(console.log)   // 1200

//10.  Function composition enabling piping
// Building-blocks to use for composition
const double = x => x + x
const triple = x => 3 * x
const quadruple = x => 4 * x

// Function composition enabling pipe functionality
const pipe = (...functions) => input => functions.reduce(
(acc, fn) => fn(acc),
input
)

// Composed functions for multiplication of specific values
const multiply6 = pipe(double, triple)
const multiply9 = pipe(triple, triple)
const multiply16 = pipe(quadruple, quadruple)
const multiply24 = pipe(double, triple, quadruple)

// Usage
multiply6(6)   // 36
multiply9(9)   // 81
multiply16(16) // 256
multiply24(10) // 240


//11.  Write map using reduce
if (!Array.prototype.mapUsingReduce) {
Array.prototype.mapUsingReduce = function(callback, initialValue) {
return this.reduce(function(mappedArray, currentValue, currentIndex, array) {
mappedArray[currentIndex] = callback.call(initialValue, currentValue, currentIndex, array)
return mappedArray
}, [])
}
}

[1, 2, , 3].mapUsingReduce(
(currentValue, currentIndex, array) => currentValue + currentIndex + array.length
) // [5, 7, , 10]
