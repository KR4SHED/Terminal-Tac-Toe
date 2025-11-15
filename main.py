def printgrid():
    for row in grid:
        print()
        print(f"{row[0]} | {row[1]} | {row[2]}")
        
        print("-" *10)
        
def checkvalid(p):
    while not p.isdigit() or not (0 < int(p) <= 9):
        p = input("Ivalid input. (1-9): ")
    return int(p) - 1

def win():
    # Checks Rows for a Win
    if grid[0][0] == grid[0][1] == grid[0][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    elif grid[1][0] == grid[1][1] == grid[2][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    elif grid[2][0] == grid[2][1] == grid[2][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    
    # Checks Columns for a Win
    elif grid[0][0] == grid[1][0] == grid[2][0] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    elif grid[0][1] == grid[1][1] == grid[2][1] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    elif grid[0][2] == grid[1][2] == grid[2][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    
    # Checks Diagonals for a Win
    elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    elif grid[2][0] == grid[1][1] == grid[0][2] != " ":
        print(f"Congratulations {grid[0][0].upper()} WINS!!")
        return False
    
    # If nobody wins game continues to run
    else:
        return True
    
running = True
    
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "x"

printgrid()

while running:
    
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
            placement = checkvalid(placement)
        
        row = placement // 3
        col = placement % 3
        grid[row][col] = turn
        
        
    if turn == "x":
        turn = "o"
        
    else:
        turn = "x"
        
    printgrid()
    
    running = win()
    
print("Over")