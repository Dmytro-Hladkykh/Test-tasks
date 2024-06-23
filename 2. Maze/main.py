from maze import random_maze_generator, display_maze_with_path
from path_finder import find_path

if __name__ == "__main__":
    n = int(input("Enter the size of the maze (n x n): "))
    maze, P0, Pf = random_maze_generator(n, n)
    display_maze_with_path(maze, [])

    while True:
        print("\nOptions:")
        print("1. Print the path")
        print("2. Generate another maze")
        print("3. Exit the game")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            path = find_path(maze, P0, Pf)
            if path:
                display_maze_with_path(maze, path)
            else:
                print("No path found.")

        elif choice == "2":
            maze, P0, Pf = random_maze_generator(n, n)
            display_maze_with_path(maze, [])

        elif choice == "3":
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
