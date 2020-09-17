''' A computer game in which the player is located in a certain tile in a grid.
    At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.
    The player starts in tile (1,1). At the beginning, and after each move selected by the player,
    the program should print the player’s travel options. If there is an open wall in a direction, write that direction as a possible travel direction.
    At each iteration, the player enters the first letter of the direction he/she wishes to travel,
    after which the player should be located in another tile and the options for the new tile are then printed out.
'''
def display_available_paths(current_tile):
    if current_tile == 1 or current_tile == 4 or current_tile == 7:
        return "N"
    if current_tile == 2:
        return "N, E, S"
    if current_tile == 3:
        return "E, S"
    if current_tile == 5 or current_tile == 9:
        return "W, S"
    if current_tile == 6:
        return "E, W"
    if current_tile == 8:
        return "N, S"

def switch_tile(current_tile, direction):
    available_paths = display_available_paths(current_tile)
    if direction.upper() in available_paths:
        if direction.upper() == "N":
            current_tile += 1
        elif direction.upper() == "E":
            current_tile += 3
        elif direction.upper() == "S":
            current_tile -= 1
        elif direction.upper() == "W":
            current_tile -= 3
        return current_tile
    else:
        print("Not a valid direction!")
    
# prufa
current_tile = 1
while current_tile != 7:
    print("You are in tile", current_tile)
    print("You can travel:", display_available_paths(current_tile)+".")

    direction = input("Direction: ")
    current_tile = switch_tile(current_tile, direction)

