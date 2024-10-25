function StringChallenge(str) {
    const n = 5; // 5x5 grid
    const directions = {
        r: [0, 1],  // move right
        l: [0, -1], // move left
        u: [-1, 0], // move up
        d: [1, 0]   // move down
    };
    
    let grid = Array.from({ length: n }, () => Array(n).fill(false));
    let x = 0, y = 0;  // start at the top left corner
    grid[x][y] = true; // mark starting position as visited

    for (let i = 0; i < str.length; i++) {
        if (str[i] === '?') {
            for (let dir in directions) {
                let [dx, dy] = directions[dir];
                let nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !grid[nx][ny]) {
                    str = str.slice(0, i) + dir + str.slice(i + 1);
                    x = nx;
                    y = ny;
                    grid[x][y] = true;
                    break;
                }
            }
        } else {
            let [dx, dy] = directions[str[i]];
            x += dx;
            y += dy;
            grid[x][y] = true;
        }
    }

    return str;
}

// Example usage:
console.log(StringChallenge("r?d?drdd")); 