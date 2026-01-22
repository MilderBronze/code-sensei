"""
More complex DSA examples
"""


def longest_palindromic_substring(s):
    """Dynamic programming approach - O(n²) time complexity"""
    n = len(s)
    if n < 2:
        return s
    
    # Create DP table
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for palindromes of length 3 or more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]


def bfs_shortest_path(graph, start, end):
    """BFS for shortest path - O(V + E) time complexity"""
    from collections import deque
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


def dfs_all_paths(graph, start, end, path=None):
    """DFS to find all paths - exponential time complexity"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    if start not in graph:
        return []
    
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs_all_paths(graph, node, end, path)
            paths.extend(new_paths)
    
    return paths


def coin_change_dp(coins, amount):
    """Coin change DP - O(amount * len(coins)) time complexity"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def sliding_window_max(nums, k):
    """Sliding window maximum - O(n) time complexity"""
    from collections import deque
    
    if not nums:
        return []
    
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside window
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Remove smaller elements
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        # Add to result
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result


def quick_select(arr, k):
    """QuickSelect - O(n) average time complexity"""
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return quick_select(right, k - len(left) - len(mid))


if __name__ == "__main__":
    # Test examples
    print("Longest Palindrome:", longest_palindromic_substring("babad"))
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS Path:", bfs_shortest_path(graph, 'A', 'F'))
    print("DFS All Paths:", dfs_all_paths(graph, 'A', 'F'))
    print("Coin Change:", coin_change_dp([1, 2, 5], 11))
    print("Sliding Window Max:", sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("QuickSelect:", quick_select([3, 2, 1, 5, 6, 4], 2))
