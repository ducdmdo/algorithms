/*
There are many way to solve Factorialize problem 
 */
ffunction factorializeNumber(number) {
    let result=1;
    for (let i = number; i >= 1; i--) {
        console.log("Inside for loop ");
        result *= i;
        console.log(result);
    }
    return result;
}
console.log(factorializeNumber(20));

function factorialize(num) {
    for (var product = 1; num > 0; num--) {
      product *= num;
    }
    return product;
  }

function factorialize(num) {
    return num === 1 ? 1 :
        num * factorialize(num-1);
}
console.log(factorialize(10));
  
  factorialize(5);