// sum the digits of a positive integer using recursion

function sumOfDigits(num) {
    const div = Math.floor(num / 10);
    const mod = num % 10;

    if (div === 0) {
        return num;
    } else {
        return mod + sumOfDigits(div);
    }
}

console.log(sumOfDigits(1234));
