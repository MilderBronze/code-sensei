# Code-Sensei 🥋

A powerful tool that analyzes Data Structures & Algorithms (DSA) logic and time complexity.

## Features

- **Time Complexity Analysis**: Automatically detect time complexity of your code
- **DSA Pattern Recognition**: Identify common algorithm patterns (sorting, searching, dynamic programming, etc.)
- **Loop Analysis**: Detect nested loops and recursive calls
- **Data Structure Detection**: Identify usage of arrays, linked lists, trees, graphs, etc.
- **Code Quality Insights**: Get recommendations for optimization

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Analyze a single file
python code_sensei.py analyze path/to/your/code.py

# Analyze with detailed output
python code_sensei.py analyze path/to/your/code.py --detailed

# Interactive mode
python code_sensei.py interactive
```

## Example

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Code-Sensei Analysis:**

- Time Complexity: O(log n)
- Space Complexity: O(1)
- Pattern: Binary Search
- Data Structures: Array

## License

MIT
