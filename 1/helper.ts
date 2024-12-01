import * as fs from "fs";

export function splitArray(): { left: number[]; right: number[] } {
  const file = fs.readFileSync("1/input.txt", "utf8");
  const lines = file.trim().split("\n");
  const left: number[] = [];
  const right: number[] = [];

  lines.forEach((line) => {
    const [leftValue, rightValue] = line.trim().split(/\s+/);
    left.push(Number.parseInt(leftValue));
    right.push(Number.parseInt(rightValue));
  });
  return { left: left, right: right };
}
