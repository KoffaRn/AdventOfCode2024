f = open("2/input.txt", "r")
input = f.read()
reports = input.split("\n")
count = 0
for report in reports:
    levels = [int(num) for num in report.split()]
    safe = True
    increasing = None

    for i in range(len(levels) - 1):
        current = levels[i]
        next = levels[i+1]
        distance = abs(current - next)
        if distance > 3 or distance == 0:
            safe = False
            break
        if increasing is None:
            increasing = next > current
        elif increasing and next <= current:
            safe = False
            break
        elif not increasing and next >= current:
            safe = False
            break
    if safe:
        count += 1
print(count)