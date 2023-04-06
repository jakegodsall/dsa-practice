// Recursive English Ruler

function drawLine(length, label) {
    let line = '-'.repeat(length);

    if (label) {
        line += ' ' + label;
    }
    console.log(line);
}

function drawInterval(centreLength) {
    if (centreLength > 0) {
        drawInterval(centreLength - 1);
        drawLine(centreLength);
        drawInterval(centreLength - 1);
    }
}

function drawRuler(numInches, barLength) {
    drawLine(barLength, '0');
    for (let i = 1; i < numInches + 1; i++) {
        drawInterval(barLength - 1);
        drawLine(barLength, i);
    }
}

drawRuler(3, 3);
