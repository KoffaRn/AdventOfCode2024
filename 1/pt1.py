with open("input.txt", "r") as file:
    data = [line.split() for line in file]

left_numbers = sorted(int(parts[0]) for parts in data)
right_numbers = sorted(int(parts[1]) for parts in data)

total_difference = sum(abs(left - right) for left, right in zip(left_numbers, right_numbers))

print(total_difference)