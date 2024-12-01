import * as fs from 'fs';

const file = fs.readFileSync('1/input.txt', 'utf8');
const lines = file.trim().split("\n");
const left: number[] = [];
const right: number[] = [];

lines.forEach(line => {
    const [leftValue, rightValue] = line.trim().split(/\s+/);
    left.push(Number.parseInt(leftValue));
    right.push(Number.parseInt(rightValue));
})

left.sort();
right.sort();

let count: number = 0;
let similarity: number = 0;

const rightFrequency = new Map<number, number>();

right.forEach(num => {
    rightFrequency.set(num, (rightFrequency.get(num) || 0) + 1);
})


left.forEach(num => {
    let simScore = 0;
    if(rightFrequency.has(num)) {
        simScore += rightFrequency.get(num)!;
    }
    similarity += (num * simScore);
})

for(let i = 0; i < left.length; i++) {



    const distance = Math.abs(left[i] - right[i]);
    count += distance;
}



console.log("Part 1, Count: " + count);

console.log("Part 2, Similarity: " + similarity);