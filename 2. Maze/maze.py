import random

class Node:
    def __init__(self, value=None, next_element=None):
        self.val = value
        self.next = next_element

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            returned = self.head.val
            self.head = self.head.next
            self.length -= 1
            return returned

    def not_empty(self):
        return bool(self.length)

    def top(self):
        return self.head.val

def random_maze_generator(r, c):
    maze = [[0 for _ in range(c)] for _ in range(r)]
    seen = [[False for _ in range(c)] for _ in range(r)]
    previous = [[(-1, -1) for _ in range(c)] for _ in range(r)]

    # Choose a random coordinate on outer side of maze 
    def random_outer_coordinate():
        if random.choice([True, False]):
            # Random position on the top or bottom row
            return (random.choice([0, r - 1]), random.randint(0, c - 1))
        else:
            # Random position on the left or right column
            return (random.randint(0, r - 1), random.choice([0, c - 1]))

    # Choosing start and end coordinates
    start = random_outer_coordinate()
    end = random_outer_coordinate()

    while start == end:
        end = random_outer_coordinate()

    S = Stack()
    S.insert(start)

    while S.not_empty():
        x, y = S.pop()
        seen[x][y] = True

        # Check for backtracking
        if (x + 1 < r) and maze[x + 1][y] == 1 and previous[x][y] != (x + 1, y):
            continue
        if (0 < x) and maze[x-1][y] == 1 and previous[x][y] != (x-1, y):
            continue
        if (y + 1 < c) and maze[x][y + 1] == 1 and previous[x][y] != (x, y + 1):
            continue
        if (y > 0) and maze[x][y-1] == 1 and previous[x][y] != (x, y-1):
            continue

        # Mark current cell as part of path
        maze[x][y] = 1
        to_stack = []

        if (x + 1 < r) and not seen[x + 1][y]:
            seen[x + 1][y] = True
            to_stack.append((x + 1, y))
            previous[x + 1][y] = (x, y)

        if (0 < x) and not seen[x-1][y]:
            seen[x-1][y] = True
            to_stack.append((x-1, y))
            previous[x-1][y] = (x, y)

        if (y + 1 < c) and not seen[x][y + 1]:
            seen[x][y + 1] = True
            to_stack.append((x, y + 1))
            previous[x][y + 1] = (x, y)

        if (y > 0) and not seen[x][y-1]:
            seen[x][y-1] = True
            to_stack.append((x, y-1))
            previous[x][y-1] = (x, y)

        end_flag = False
        while to_stack:
            neighbour = to_stack.pop(random.randint(0, len(to_stack) - 1))
            if neighbour == end:
                end_flag = True
            else:
                S.insert(neighbour)

        if end_flag:
            S.insert(end)

    x_start, y_start = start
    x_end, y_end = end
    maze[x_start][y_start] = 2
    maze[x_end][y_end] = 3
    return maze, start, end

def display_maze_with_path(maze, path):
    symbols = {0: "▓", 1: "◌", 2: "S", 3: "E", -1: "◍"}
    maze_copy = [row[:] for row in maze]
    for x, y in path:
        if maze_copy[x][y] == 1:
            maze_copy[x][y] = -1
    for row in maze_copy:
        print(" ".join(symbols[cell] for cell in row))
