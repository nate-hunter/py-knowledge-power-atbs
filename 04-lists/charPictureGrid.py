grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]


for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()

print(f'\n------------ \n')

for x in range(len(grid)):
    for y in range(len(grid[0])):
        print(grid[x][y], end='')
    print()

