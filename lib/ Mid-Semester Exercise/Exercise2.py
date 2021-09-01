"""
Last modified: 2021/08/26
This file includes Maze Class.
Import Maze by:
    from maze import Maze
"""
from random import choice, randint


class Maze:
    """
    A class to represent the Maze.
    ...
    Attribute
    ----------
    the_maze(list(list(str))): a 2D list that represents the row and column of the maze.

    Methods
    -------
    _is_valid_step(next_step,visited):
        Check whether next_step coordinate is valid, not visited, and not creating loop.
    _is_available_step(current_step,visited):
        Check whether there is available non-visited neighbour grids of the current grid.
    _create_maze(difficulty):
        Initialize the maze.
    print_maze():
        Print the maze.
    get_maze():
        Returns the maze.
    get_grid(row_idx,col_idx):
        Returns the maze grid at (row_idx, col_idx).
    get_dimension():
        Returns the dimension of the maze.
    """

    def __init__(self, dimension, difficulty=1.0):
        """
        Constructs all the necessary attributes for the Maze object.
        Args:
            1. dimension(list(int,int) or tuple(int,int)): Dimension of the maze[row,column].
            2. difficulty(float): Set the 'curviness' of the Maze. Default value: 1.0
        """
        if dimension[0] not in range(8, 17) or dimension[1] not in range(8, 17):
            raise ValueError('dimension must be within 8x8 and 16x16')
        self.the_maze = [['X' for _ in range(dimension[1])] for _ in range(dimension[0])]
        self._create_maze(difficulty)
        self.dimension = tuple(dimension)

    def _is_valid_step(self, next_step, visited):
        """
        Check whether next_step coordinate is valid, not visited, and not creating loop.
        Args:
            1. next_step(list(int,int) or tuple(int,int)): The coordinates needed to be validated[row_idx, col_idx].
            2. visited(list(tuple(int,int))): A list of visited coordinates tuples.
        Returns:
            bool: whether next_step is valid or not.
        """
        return next_step[0] >= 0 and next_step[1] >= 0 and next_step not in visited and next_step[0] <= len(
            self.the_maze) - 1 and next_step[1] <= len(self.the_maze[0]) - 1 and (
                           [(next_step[0] + 1, next_step[1]) in visited, (next_step[0] - 1, next_step[1]) in visited,
                            (next_step[0], next_step[1] + 1) in visited,
                            (next_step[0], next_step[1] - 1) in visited].count(True) == 1)

    def _is_available_step(self, current_step, visited):
        """
        Check whether there is available non-visited neighbour grids of the current grid.
        Args:
            1. current_step(list(int,int) or tuple(int,int)): The current coordinates[row_idx, col_idx].
            2. visited(list(tuple(int,int))): A list of visited coordinates tuples.
        Returns:
            bool: whether there is unexplored neighbouring coordinates.
        """
        return any([self._is_valid_step((current_step[0] - 1, current_step[1]), visited),
                    self._is_valid_step((current_step[0] + 1, current_step[1]), visited),
                    self._is_valid_step((current_step[0], current_step[1] - 1), visited),
                    self._is_valid_step((current_step[0], current_step[1] + 1), visited)])

    def _create_maze(self, difficulty):
        """
        Initialize the maze with a path from starting point to ending point.
        Args:
            1. difficulty(float): Set the 'curviness' of the Maze. Default value: 1.0
        """
        total_coor = [0, 0]
        visited = [(0, 0)]
        current = (0, 0)
        stepvals_positive = [-1, 0, 0, 1, 1, 1]
        stepvals_negative = [-1, -1, -1, 0, 0, 1]
        stepvals_zero = [-1, -1, 0, 0, 0, 1, 1]
        prev_step = (1, 0)
        while total_coor[0] < len(self.the_maze) - 1 or total_coor[1] < len(self.the_maze[0]) - 1:
            if not self._is_available_step(current, visited):
                total_coor = [0, 0]
                visited = [(0, 0)]
                current = (0, 0)
            step = (prev_step[0] == 1 and choice(stepvals_positive) or prev_step[0] == -1 and choice(
                stepvals_negative) or choice(stepvals_zero),
                    prev_step[1] == 1 and choice(stepvals_positive) or prev_step[1] == -1 and choice(
                        stepvals_negative) or choice(stepvals_zero))
            next_step = (current[0] + step[0], current[1] + step[1])
            while not (abs(sum(step)) == 1 and self._is_valid_step(next_step, visited)):
                step = (prev_step[0] == 1 and choice(stepvals_positive) or prev_step[0] == -1 and choice(
                    stepvals_negative) or choice(stepvals_zero),
                        prev_step[1] == 1 and choice(stepvals_positive) or prev_step[1] == -1 and choice(
                            stepvals_negative) or choice(stepvals_zero))
                next_step = (current[0] + step[0], current[1] + step[1])
            total_coor[0], total_coor[1] = total_coor[0] + step[0], total_coor[1] + step[1]
            visited.append(next_step)
            current = next_step
            prev_step = step

        random_space = []
        for _ in range(int(len(self.the_maze[0]) * len(self.the_maze) * difficulty * 0.3)):
            coor = (randint(0, len(self.the_maze) - 1), randint(0, len(self.the_maze[0]) - 1))
            trial = 0
            while coor in visited or [(coor[0] + 1, coor[1]) in visited, (coor[0] - 1, coor[1]) in visited,
                                      (coor[0], coor[1] + 1) in visited, (coor[0], coor[1] - 1) in visited].count(
                    True) != 1 or trial < min(len(self.the_maze), len(self.the_maze[0])):
                coor = (randint(0, len(self.the_maze) - 1), randint(0, len(self.the_maze[0]) - 1))
                trial += 1
            visited.append(coor)
        for path in visited:
            self.the_maze[path[0]][path[1]] = ' '

    def print_maze(self):
        """Print the maze."""
        print('start')
        print(' ↓')
        print('┌ ' + '─' * (len(self.the_maze[0]) * 2 - 2) + '┐')
        for row_idx in range(len(self.the_maze)):
            print('│' + ' '.join(self.the_maze[row_idx]) + '│')
        print('└' + '─' * (len(self.the_maze[0]) * 2 - 2) + ' ┘')
        print(' ' * (len(self.the_maze[0]) * 2 - 1) + '↓')
        print(' ' * (len(self.the_maze[0]) * 2 - 2) + 'End')

    def get_maze(self):
        """
        Returns the maze.
        Returns:
            list(list(str)): A 2D list of string representing the maze.
        """
        return self.the_maze

    def get_grid(self, row_idx, col_idx):
        """
        Returns the maze grid at (row_idx, col_idx).
        Returns:
            str: Value at self.the_maze[row_idx][col_idx]
        """
        return self.the_maze[row_idx][col_idx]

    def get_dimension(self):
        """
        Returns the dimension of the maze.
        Returns:
            tuple(int,int): dimension of the maze(number of rows, number of columns)
        """
        return self.dimension


if __name__ == "__main__":
    # The code below will be performed only if the script is run directly
    # It will not run when the script is imported
    a_maze = Maze([12, 12])
    print("Maze created.")
