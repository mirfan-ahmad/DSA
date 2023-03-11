from ArrayStack import ArrayStack


def floodfill(data, height, width, sr, sc, bc, fc):
    def valid(row, col):
        return 0 <= row < height and 0 <= col < width and data[row][col] == bc

    if data[sr][sc] != bc:
        return

    stack = ArrayStack(height*width)
    stack.push((sr, sc))
    while not stack.isEmpty():
        row, col = stack.pop()
        data[row][col] = fc
        if valid(row - 1, col):
            stack.push((row - 1, col))
        if valid(row + 1, col):
            stack.push((row + 1, col))
        if valid(row, col-1):
            stack.push((row, col-1))
        if valid(row, col+1):
            stack.push((row, col+1))


if __name__ == '__main__':
    data = [
        [1, 1, 1, 1, 1, 2, 1, 1, 2],
        [2, 2, 8, 2, 2, 2, 2, 1, 1],
        [2, 8, 8, 2, 2, 5, 7, 8, 2],
        [2, 8, 8, 2, 9, 2, 2, 8, 3],
        [4, 4, 0, 2, 9, 2, 6, 2, 2],
        [0, 4, 2, 2, 9, 2, 2, 2, 5],
        [9, 4, 2, 2, 2, 2, 2, 2, 4],
        [0, 4, 4, 4, 4, 4, 5, 4, 4],
    ]

    floodfill(data, 8, 9, 3, 5, 2, 11)

    for row in data:
        print(*row)
