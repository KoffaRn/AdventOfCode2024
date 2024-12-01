import { splitArray } from "./helper";

const left = splitArray().left;
const right = splitArray().right;

left.sort();
right.sort();

let count: number = 0;

for (let i = 0; i < left.length; i++) {
  const distance = Math.abs(left[i] - right[i]);
  count += distance;
}

console.log("Part 1, Count: " + count);
