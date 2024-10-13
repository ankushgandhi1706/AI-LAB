# Eight Puzzle Solver

This repository contains implementations of the **Eight Puzzle** problem using two different search algorithms:

- **A* Search Algorithm** (`EightPuzzleAStar.py`)
- **Breadth-First Search (BFS) Algorithm** (`EightPuzzleBFS.py`)

## Problem Overview

The Eight Puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty space. The goal is to move the tiles around until they are in a specific configuration (usually the tiles are in numerical order from 1 to 8, with the empty space in the bottom-right corner).

## Files in This Repository

1. **EightPuzzleAStar.py**  
   This file implements the Eight Puzzle problem using the **A* Search Algorithm**. The A* algorithm is an informed search algorithm that uses both the cost to reach a node (g(n)) and a heuristic estimate of the cost to reach the goal (h(n)) to find the most optimal solution.

2. **EightPuzzleBFS.py**  
   This file implements the Eight Puzzle problem using the **Breadth-First Search (BFS)** algorithm. BFS is an uninformed search algorithm that explores all possible configurations level by level, guaranteeing the shortest solution but not always the most efficient in terms of time complexity.

## How the Algorithms Work

### A* Search Algorithm
- **Heuristic:** The A* algorithm used here likely employs the **Manhattan Distance** or **Misplaced Tiles** heuristic to evaluate how far each state is from the goal state.
- **Optimality:** A* is guaranteed to find the optimal solution (if one exists) by expanding the least-cost path first.
- **Efficiency:** A* is more efficient than BFS as it uses heuristics to reduce the number of states to explore.

### Breadth-First Search (BFS)
- **Uninformed Search:** BFS explores the search space level by level, considering all possible moves at each depth.
- **Guarantee of Solution:** BFS is guaranteed to find a solution if one exists, and it will find the shortest sequence of moves to reach the goal.
- **Time Complexity:** Since BFS explores all nodes at a given level before moving to the next, it can be slower and require more memory than A*, especially for larger search spaces.

## How to Run

### Requirements
- Python 3.x
- No external libraries are required

### Running A* Solver

To run the A* solution:

```bash
python EightPuzzleAStar.py
```

### Running BFS Solver

To run the BFS solution:

```bash
python EightPuzzleBFS.py
```

## Example

Here’s an example of how the program works. The puzzle starts in a random configuration, and the algorithms will attempt to solve it by sliding the tiles into the correct position:

```
Initial State:
1 2 3
4 5 6
7 8 _

Goal State:
1 2 3
4 5 6
7 8 _
```

The output will include the steps taken to solve the puzzle, the number of nodes expanded, and other relevant statistics for the chosen algorithm.

## Future Improvements

- Add more heuristic functions to the A* implementation.
- Implement additional search algorithms such as Depth-First Search (DFS) or Iterative Deepening Search (IDS).
- Improve the UI by adding a graphical interface for solving the puzzle visually.

## Contributing

Feel free to open a pull request or issue if you find any bugs or have suggestions for improving the code or documentation.
