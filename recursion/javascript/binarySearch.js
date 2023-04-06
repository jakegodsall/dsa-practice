function binarySearch(array, value, low, high) {
    // if low and high not explicitly set, add values
    if (!low) {
        low = 0;
    }
    if (!high) {
        high = array.length - 1;
    }

    // check array is not empty
    if (low > high) {
        return false;
    } else {
        const mid = Math.floor((low + high) / 2);

        if (value === array[mid]) {
            return true; // value found
        } else if (value < array[mid]) {
            return binarySearch(array, value, low, mid - 1);
        } else {
            return binarySearch(array, value, mid + 1, high);
        }
    }
}

const array = [12, 32, 33, 35, 77, 89, 121, 323, 12312];

console.log(binarySearch(array, 33));
console.log(binarySearch(array, 34));
