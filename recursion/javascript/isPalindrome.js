// checks if a string is a palindrome

function isPalindromeIterative(string) {
    // first reverse the string
    let reverse = '';

    for (char of string) {
        reverse = char + reverse;
    }

    return string === reverse;
}

function isPalindromeRecursive(string) {
    if (string.length === 0 || string.length === 1) {
        return true;
    } else {
        const head = string[0];
        const middle = string.slice(1, string.length - 1);
        const tail = string[string.length - 1];

        return head === tail && isPalindromeRecursive(middle);
    }
}

console.log(isPalindromeIterative('racecar'));
console.log(isPalindromeIterative('hello'));

console.log(isPalindromeRecursive('racecar'));
console.log(isPalindromeRecursive('hello'));
