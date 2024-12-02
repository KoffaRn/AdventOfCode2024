def validate_levels(current: int, next: int, increasing: bool):
    distance = abs(current - next)
    if distance > 3 or distance == 0:
        return False
    if increasing and next <= current:
        return False
    if not increasing and next >= current:
        return False
    return True


def is_safe_with_dampener(levels):
    for skip_index in range(len(levels)):
        modified_levels = levels[:skip_index] + levels[skip_index + 1 :]
        if is_safe(modified_levels):
            return True
    return False


def is_safe(levels):
    increasing = None
    for i in range(len(levels) - 1):
        current = levels[i]
        next = levels[i + 1]
        if increasing is None:
            increasing = next > current
        if not validate_levels(current, next, increasing):
            return False
    return True

with open("2/input.txt", "r") as f:
    reports = f.read().splitlines()

count = 0
for report in reports:
    levels = [int(num) for num in report.split()]
    if is_safe(levels) or is_safe_with_dampener(levels):
        count += 1

print(count)