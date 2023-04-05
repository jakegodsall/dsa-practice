// sum all values in an array

function sumArrayIterative(arr) {
    let total = 0;

    for (val of arr) {
        total += val;
    }

    return total;
}

function sumArrayRecursive(arr) {
    if (arr.length === 0) {
        return 0;
    } else {
        const head = arr[0];
        const tail = arr.slice(1, arr.length);
        return head + sumArrayRecursive(tail);
    }
}

console.log(sumArrayIterative([1, 2, 3, 4, 5]));
console.log(sumArrayRecursive([1, 2, 3, 4, 5]));
