with open("5/rules_input.txt", "r") as f:
    rules_input = f.read().splitlines()
rules = [list(map(int, line.split('|'))) for line in rules_input]

with open("5/update_input.txt", "r") as f:
    update_input = f.read().splitlines()
updates = [list(map(int, line.split(','))) for line in update_input]

for rule in rules:
    print(rule[0])
    print(rule[1])
for update in updates:
    print(update[0])