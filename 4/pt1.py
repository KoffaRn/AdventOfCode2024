def count_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]
    
    def is_word_at(x, y, dx, dy):
        """Check if the word exists starting from (x, y) in direction (dx, dy)."""
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1

    return count

# Example Grid

with open("4/input.txt", "r") as f:
    input = f.read().splitlines()

# Search for "XMAS"
word = "XMAS"
result = count_word_in_grid(input, word)
print(f"The word '{word}' appears {result} times in the grid.")