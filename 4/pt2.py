with open("4/input.txt", "r") as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])
count = 0
patterns = [
    ('M', 'S', 'M', 'S'),
    ('S', 'M', 'S', 'M'),
    ('M', 'S', 'S', 'M'),
    ('S', 'M', 'M', 'S')
]

for x in range(1, rows - 1): 
    for y in range(1, cols - 1): 
        if grid[x][y] == 'A':  
            
            diagonals = (
                grid[x-1][y-1], 
                grid[x+1][y+1],  
                grid[x-1][y+1],  
                grid[x+1][y-1]  
            )
            
            if diagonals in patterns:
                count += 1
print(count)