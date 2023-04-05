// reverse the order of a string

function reverseStringIterative(string) {
    let reversed = '';

    for (char of string) {
        reversed = char + reversed;
    }

    return reversed;
}

function reverseStringRecursive(string) {
    if (string.length === 0 || string.length === 1) {
        return string;
    } else {
        const head = string[0];
        const tail = string.slice(1, string.length);

        return reverseStringRecursive(tail) + head;
    }
}

console.log(reverseStringIterative('hello'));
console.log(reverseStringRecursive('hello'));
