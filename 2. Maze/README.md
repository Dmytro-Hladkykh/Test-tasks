# Maze

The "Maze" project is a Python implementation of a maze generation and solving algorithm. The project includes a maze generator that creates a random maze with a specified size and starting (S) and ending (E) points. Additionally, it features a depth-first search (DFS) algorithm to find a path from the starting point to the ending point in the generated maze.

## Installation and Running

1. Ensure you have Python (version 3.x) installed.
2. Clone the repository.
3. Run the `main.py` file using the command `python main.py` in the console.

## Project Structure

- `maze.py` - File with components to generate and display maze.
- `path_finder.py` - File with DFS algorithm to solve the maze.
- `main.py` - Main file for running the program.
- `README.md` - This file.

## Components

### Maze Generation

The maze generation utilizes a stack-based algorithm to create a random maze. The algorithm ensures that there is only one path between the starting and ending points, making the maze solvable. The generated maze consists of cells marked as follows:

0: Wall (▓)
1: Open path (◌)
2: Starting point (S)
3: Ending point (E)
4: Path (◍)

Step-by-step process of maze generation:

1. Initialize the maze with all cells as walls (0).
2. Choose random starting and ending points on the outer edges of the maze.
3. Create a stack and push the starting point onto it.
4. While the stack is not empty:
   a. Pop a cell from the stack.
   b. If the cell has not been visited:
      - Mark it as visited.
      - Mark it as part of the path (1).
      - Get unvisited neighbors of the cell.
      - Randomly shuffle the neighbors.
      - For each neighbor:
        * If it's the end point, push it onto the stack and break the loop.
        * Otherwise, push it onto the stack.
5. Mark the starting point as 'S' (2) and the ending point as 'E' (3).

This algorithm ensures that there is always a path from the start to the end, and creates a maze with a single solution.

### Depth-First Search (DFS)

The DFS algorithm is employed to find a path from the starting point to the ending point in the generated maze. The DFS explores possible paths, backtracking when necessary, until it successfully reaches the destination. The path is then displayed, and the maze with the path is printed.

### User Interaction

The user can interact with the program through a simple console interface with the following options:

 - **Print the Path**: Display the solution path in the generated maze.
 - **Generate Another Maze**: Create a new random maze.
 - **Exit the Game**: Terminate the program.

## Efficiency Analysis

### Maze Generation:

**Algorithm**: The maze generation uses a stack-based DFS approach.

**Time Complexity**: O(r * c), where r and c are the number of rows and columns. Each cell is processed once, ensuring efficient maze creation.

**Space Complexity**: O(r * c) due to maze storage, DFS stack, and visited cell tracking.

### Depth-First Search (DFS):

**Algorithm**: Used to find a path from start to end in the maze.

**Time Complexity**: O(r * c), ensuring efficient pathfinding by exploring each cell and edge once.

**Space Complexity**: O(r * c) due to recursion stack depth.

### Why is the Solution Efficient?

 - **Maze Generation**: Linear time complexity ensures quick maze creation even for large sizes.

 - **Pathfinding**: Linear time complexity enables rapid path discovery through the maze.

# Conclusion

The solution's efficiency lies in its linear time complexity relative to maze size for both generation and pathfinding, making it suitable for practical use in generating and solving mazes of varying complexities.

