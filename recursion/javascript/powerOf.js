// calculate the power of a number recursively

function powerOf(base, exponent) {
    if (exponent === 0) {
        return 1;
    } else if (exponent > 0) {
        return (1 / base) * powerOf(base, exponent + 1);
    } else {
        return base * powerOf(base, exponent - 1);
    }
}

console.log(powerOf(2, 10));
