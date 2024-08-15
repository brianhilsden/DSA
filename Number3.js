function solution(A) {
    let frequency = {};
    let freqOfFreq = {};

    //calculates  the frequency
    for (let num of A) {
        frequency[num] = (frequency[num] || 0) + 1;
    }

    // counts the frquency of the calculated frequency
    for (let count of Object.values(frequency)) {
        freqOfFreq[count] = (freqOfFreq[count] || 0) + 1;
    }

    let deletions = 0;

    let sortedFreqs = Object.keys(freqOfFreq).map(Number).sort((a, b) => b - a);

    for (let i = 0; i < sortedFreqs.length; i++) {
        let freqCount = sortedFreqs[i];

        while (freqOfFreq[freqCount] > 1) {
            freqOfFreq[freqCount] -= 1; //decrements the counts in how many numbes the frequency has
            deletions += 1; // it the increments the deletion by 1 to make the frequcy unique

            if (freqCount - 1 > 0) {
                freqOfFreq[freqCount - 1] = (freqOfFreq[freqCount - 1] || 0) + 1;
            }
        }
    }

    return deletions;
}

// Example test cases
console.log(solution([1, 1, 1, 2, 2, 2]));  // Expected output: 1
console.log(solution([5, 3, 3, 2, 5, 2, 3, 2]));  // Expected output: 2
console.log(solution([127, 15, 3, 8, 10]));  // Expected output: 4
console.log(solution([10000000, 10000000, 5, 5, 5, 2, 2, 2, 0, 0]));  // Expected output: 4