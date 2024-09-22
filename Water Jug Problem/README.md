# Water Jug Problem

## Problem Statement

You are given two jugs with capacities of 3 liters and 4 liters, respectively. The goal is to measure exactly 2 liters using these jugs. Initially, both jugs are empty, but you can start by placing 2 liters of water in any jug. The available operations you can perform are:

1. Fill either jug completely.
2. Empty either jug.
3. Pour water from one jug to the other until one jug is either full or the other is empty.

```
     4L Jug                 3L Jug
                
    |       |             |       |
    |       |             |       |
    |       |             |       |
    |       |             |       |
    +-------+             +-------+
       0L                    0L
```

## Approach

This implementation uses a breadth-first search (BFS) approach to explore all possible states of the jugs until the target of 2 liters is achieved. The main functions are defined for different operations involving the jugs:

- **Fill3**: Fills the 3L jug to its capacity.
- **Fill4**: Fills the 4L jug to its capacity.
- **From3to4**: Transfers water from the 3L jug to the 4L jug.
- **From4to3**: Transfers water from the 4L jug to the 3L jug.
- **Empty3**: Empties the 3L jug.
- **Empty4**: Empties the 4L jug.

The main loop continues until the desired amount of water (2 liters) is found.

### Code Explanation

```python
InitJugs = [0, 0]  # Initial state of both jugs

# Function definitions for operations on the jugs...

explored = []
frontier = []
frontier.append(InitJugs)
count = 0

while len(frontier) != 0:
    InitJugs = frontier.pop(0)
    print(f"{InitJugs}")

    if InitJugs[0] == 2:  # Check if the goal is reached
        print(f"Goal state {InitJugs} found after searching {count} nodes.")
        break

    # Explore possible states and add to frontier...
```

## Time Complexity

- Each operation has a constant time complexity, O(1), since the number of operations is fixed and the states are limited.
- The overall complexity is O(n) where n is the number of unique states explored until the solution is found.

## Space Complexity

- The space complexity is O(n) due to the storage of the explored and frontier states in lists.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

   ```bash
   python WaterJug.py
   ```

4. The output will display the series of states explored until the goal is reached.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes. Contributions are welcome!

## License

This project is licensed under the MIT License.
