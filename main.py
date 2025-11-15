def printgrid():
    for row in grid:
        print()
        print(f"{row[0]} | {row[1]} | {row[2]}")
        
        print("-" *10)
        
def checkvalid(p):
    while not p.isdigit() or not (0 < int(p) <= 9):
        p = input("Ivalid input. (1-9): ")
    return int(p) - 1
    
    

grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "x"

printgrid()

for i in range(9):
    
    placement = input("Where would you like to go? (1-9): ")
    placement = checkvalid(placement)
    ogplace = placement
    
    row = placement // 3
    col = placement % 3
    
    if grid[row][col] == " ":
        grid[row][col] = turn
        
    else:
        while ogplace == placement:
            placement = input("This spot is already taken. Choose a new spot: ")
            checkvalid(placement)
            placement = checkvalid(placement)
        
        row = placement // 3
        col = placement % 3
        grid[row][col] = turn
        
        
    if turn == "x":
        turn = "o"
        
    else:
        turn = "x"
        
    printgrid()