// concatenate elements in an array of strings

function concatArrayIterative(arr) {
    let string = '';

    for (val of arr) {
        string += val;
    }

    return string;
}

function concatArrayRecursive(arr) {
    if (arr.length === 0) {
        return '';
    } else {
        let head = arr[0];
        let tail = arr.slice(1, arr.length);

        return head + concatArrayRecursive(tail);
    }
}

console.log(concatArrayIterative(['this', 'is', 'a', 'test']));
console.log(concatArrayRecursive(['this', 'is', 'a', 'test']));
