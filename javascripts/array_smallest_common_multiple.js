/*
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.
*/

/*
smallestCommons([1, 5]) should return a number.

smallestCommons([1, 5]) should return 60: 1, 2, 3, 4, 5 = 5*4*3 => 60

smallestCommons([5, 1]) should return 60.

smallestCommons([2, 10]) should return 2520: 1, 2, 3, 4, 5, 6, 7, 8,9,10 => 10 (5,2) * 9 (6,3) * 8 (4,2) * 7 (7, 1) * 6 (3,2) * 5 (5,1) * 4 (4,2) * 3 * 2 * 1
==> [5,2,6,3,4,2,7,1,3,2,5,1,2,2,3,2,1]

smallestCommons([1, 13]) should return 360360.

smallestCommons([23, 18]) should return 6056820.
*/

function smallestCommons(arr) {

    let arrayTemp = [1,2];

    //Analysis and separate numbers
    //push to the arrayTemp if a number is an odd number
    //push to the arrayTemp the divided result if a number is an even number
    for (let i = 3; i <= Math.max(...arr); i++) {
        if (i % 2 !== 0) {
            arrayTemp.push(i);
        } else {
            arrayTemp.push(i/2);
        }
    }
    console.log(arrayTemp);
    //Filter the duplicated numbers in range
    // return result which is the smallest common MULTIPLE of parameters in range
    return arrayTemp.reduce((previousValueResult, currentValure) => {
            if (!previousValueResult.includes(currentValure)) {
                previousValueResult.push(currentValure);
            }
            return previousValueResult;
        },[]).reduce((pre, curr) => {
            return pre * curr;
        },1);
    }

    function smallestCommons(arr) {
        // Setup
        const [min, max] = arr.sort((a, b) => a - b);
        const numberDivisors = max - min + 1;
        // Largest possible value for SCM
        let upperBound = 1;
        for (let i = min; i <= max; i++) {
          upperBound *= i;
        }
        // Test all multiples of 'max'
        for (let multiple = max; multiple <= upperBound; multiple += max) {
          // Check if every value in range divides 'multiple'
          let divisorCount = 0;
          for (let i = min; i <= max; i++) {
            // Count divisors
            if (multiple % i === 0) {
              divisorCount += 1;
            }
          }
          if (divisorCount === numberDivisors) {
            return multiple;
          }
        }
      }
      
      smallestCommons([1, 5]);


      function smallestCommons(arr) {
        // Setup
        const [min, max] = arr.sort((a, b) => a - b);
        const range = Array(max - min + 1)
          .fill(0)
          .map((_, i) => i + min);
        // Largest possible value for SCM
        const upperBound = range.reduce((prod, curr) => prod * curr);
        // Test all multiples of 'max'
        for (let multiple = max; multiple <= upperBound; multiple += max) {
          // Check if every value in range divides 'multiple'
          const divisible = range.every((value) => multiple % value === 0);
          if (divisible) {
            return multiple;
          }
        }
      }
      
      smallestCommons([1, 5]);

      function smallestCommons(arr) {
        // Setup
        const [min, max] = arr.sort((a, b) => a - b);
        const range = Array(max - min + 1)
          .fill(0)
          .map((_, i) => i + min);
        // GCD of two numbers
        // https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
        const gcd = (a, b) => (b === 0) ? a : gcd(b, a % b);
        // LCM of two numbers
        // https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor
        const lcm = (a, b) => a * b / gcd(a, b);
        // LCM of multiple numbers
        // https://en.wikipedia.org/wiki/Least_common_multiple#Other
        return range.reduce((multiple, curr) => lcm(multiple, curr));
      }
      
      smallestCommons([1, 5]);

      // Find the SCM of a range of numbers
function smallestCommons(arr) {
    let primeFactors = {};
    const [min, max] = arr.sort((a, b) => a - b);
    for (let i = min; i <= max; i++) {
      // Factorize number in range
      let primes = getPrimeFactors(i);
      for (let j in primes) {
        // Add factor to set or update number of occurrences
        if (!primeFactors[j] || primes[j] > primeFactors[j]) {
          primeFactors[j] = primes[j]
        }
      }
    }
    // Build SCM from factorization
    let multiple = 1;
    for (let i in primeFactors) {
      multiple *= i ** primeFactors[i]
    }
    return multiple;
  }
  
  // Compute prime factors of a number
  function getPrimeFactors(num) {
    const factors = {};
    for (let prime = 2; prime <= num; prime++) {
      // Count occurances of factor
      // Note that composite values will not divide num
      while ((num % prime) === 0) {
        factors[prime] = (factors[prime]) ? factors[prime] + 1 : 1;
        num /= prime;
      }
    }
    return factors;
  }
  
  smallestCommons([1, 5]);
    