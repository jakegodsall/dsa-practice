// factorial function

// iterative solution
function factorialIterative(num) {
    let total = 1;

    for (let i = 1; i <= num; i++) {
        total *= i;
    }

    return total;
}

// recursive solution
function factorialRecursive(num) {
    if (num === 0) {
        // base case
        return 1;
    } else {
        // recursive case
        return num * factorialRecursive(num - 1);
    }
}

console.log(factorialIterative(5));
console.log(factorialRecursive(5));
