import re
with open("3/input.txt", "r") as f:
    input = f.read()

do_array = input.split("do()")

for i in range(len(do_array)):
    dont_index = do_array[i].find("don't()")
    if dont_index != -1:
        do_array[i] = do_array[i][:dont_index]

count = 0
for operations in do_array:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", operations)
    for match in matches:
        numbers = re.findall(r"\d{1,3}", match)
        count += int(numbers[0]) * int(numbers[1])

print(count)