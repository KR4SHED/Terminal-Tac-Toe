# Tic Tac Toe

grid = [
    ["  |", "  |", " "],
    ["  |", "  |", " "],
    ["  |", "  |", " "]
]

turn = "x"

for i in range(9):

    print()
    placement = input("Where would you like to go? (1-9): ")
    print("-"*37)
    print()
    
    while not placement.isdigit():
        placement = input("Where would you like to go? (1-9): ")
        
            
    placement = int(placement)
    
    while int(placement) <= 0 or int(placement) > 9:
        placement = input("Where would you like to go? (1-9): ")
    
    if placement == 1 and grid[0][0] == "  |":
        grid[0][0] = turn + " |"
    
    else:
        while placement == 1:
            placement = int(input("Where would you like to go? (1-9): "))

    if placement == 2 and grid[0][1] == "  |":
        grid[0][1] = turn + " |"
    
    else:
        while placement == 2:
            placement = int(input("Where would you like to go? (1-9): "))
    
    if placement == 3 and grid[0][2] == " ":
        grid[0][2] = turn
        
    else:
        while placement == 3:
            placement = int(input("Where would you like to go? (1-9): "))
    
    if placement == 4 and grid[1][0] == "  |":
        grid[1][0] = turn + " |"
        
    else:
        while placement == 4:
            placement = int(input("Where would you like to go? (1-9): "))
        
    if placement == 5 and grid[1][1] == "  |":
        grid[1][1] = turn + " |"
        
    else:
        while placement == 5:
            placement = int(input("Where would you like to go? (1-9): "))
    
    if placement == 6 and grid[1][2] == " ":
        grid[1][2] = turn
        
    else:
        while placement == 6:
            placement = int(input("Where would you like to go? (1-9): "))
        
    if placement == 7 and grid[2][0] == "  |":
        grid[2][0] = turn + " |"
        
    else:
        while placement == 7:
            placement = int(input("Where would you like to go? (1-9): "))
    
    if placement == 8 and grid[2][1] == "  |":
        grid[2][1] = turn + " |"
        
    else:
        while placement == 8:
            placement = int(input("Where would you like to go? (1-9): "))
        
    if placement == 9 and grid[2][2] == " ":
        grid[2][2] = turn
        
    else:
        while placement == 9:
            placement = int(input("Where would you like to go? (1-9): "))
            
    
    
    
    if turn == "x":
        turn = "o"
    
    else:
        turn = "x"
    
    
    for row in grid:
    
        for column in row:
        
            print(column, end=" ")
    
        print()
        print("-"*9)
    
