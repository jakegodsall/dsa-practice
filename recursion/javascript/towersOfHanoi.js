class TowersOfHanoi {
    constructor(numDisks) {
        this.numDisks = numDisks;
        this.disks = {
            A: [],
            B: [],
            C: [],
        };

        this.initGame(numDisks);
    }

    initGame(numDisks) {
        for (let i = 1; i < numDisks + 1; i++) {
            this.disks['A'].unshift(i);
        }
    }

    printDisk(diskNum) {
        const emptySpace = ' '.repeat(this.numDisks - diskNum);

        if (diskNum === 0) {
            // draw the pole
            console.log(emptySpace + '||' + emptySpace);
        } else {
            // draw the disk
            const diskSpace = '@'.repeat(diskNum);
            const diskNumLabel = String(diskNum);
            console.log(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace);
        }
    }

    printTowers() {
        // print all three towers
        for (let level = this.numDisks; level >= 0; level--) {
            for (let tower of this.disks) {
                if (level >= tower.length) {
                    this.printDisk(0);
                }
            }
        }
    }
}

const toh = new TowersOfHanoi(3);
toh.printDisk(1);
