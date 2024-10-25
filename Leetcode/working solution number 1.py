def StringChallenge(str):
    # Directions map
    direction_map = {'r': (0, 1), 'l': (0, -1), 'u': (-1, 0), 'd': (1, 0)}
    
    def is_valid(x, y, grid):
        return 0 <= x < 5 and 0 <= y < 5 and not grid[x][y]

    def backtrack(path, x, y, grid, idx):
        if (x, y) == (4, 4):
            return path
        
        print(path)
        
        if idx >= len(path):
            return None
        
        direction = path[idx]
        if direction == '?':
            for d, (dx, dy) in direction_map.items():
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, grid):
                    grid[x][y] = True
                    new_path = path[:idx] + d + path[idx+1:]
                    result = backtrack(new_path, nx, ny, grid, idx + 1)
                    if result:
                        return result
                    grid[x][y] = False
            return None
        else:
            dx, dy = direction_map[direction]
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                grid[x][y] = True
                result = backtrack(path, nx, ny, grid, idx + 1)
                if result:
                    return result
                grid[x][y] = False
            return None

    # Initialize the grid and starting point
    grid = [[False] * 5 for _ in range(5)]
    grid[0][0] = True
    path = backtrack(str, 0, 0, grid, 0)
    
    # Validate the path
    if not path:
        return "No valid path"
    
    # Prepare the final result
    
    ChallengeToken = "h43kvgjlcba7"

    final_string = path + ChallengeToken

    result = []

    for i,char in enumerate(final_string):
        if(i+1) % 3 == 0:
            result.append("X")
        else:
            result.append(char)
    return ''.join(result)

print(StringChallenge("???rrurdr?")) 
