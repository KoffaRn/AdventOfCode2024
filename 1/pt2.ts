import { splitArray } from "./helper";

const left = splitArray().left;
const right = splitArray().right;

let similarity: number = 0;

const rightFrequency = new Map<number, number>();

right.forEach((num) => {
  rightFrequency.set(num, (rightFrequency.get(num) || 0) + 1);
});

left.forEach((num) => {
  let simScore = 0;
  if (rightFrequency.has(num)) {
    simScore += rightFrequency.get(num)!;
  }
  similarity += num * simScore;
});

console.log("Part 2, Similarity: " + similarity);
