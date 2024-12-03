import re
with open("3/input.txt", "r") as f:
    input = f.read()

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

count = 0

for match in matches:
    numbers = re.findall(r"\d{1,3}", match)
    count += int(numbers[0]) * int(numbers[1])

print(count)