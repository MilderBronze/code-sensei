"""
Example DSA implementations for testing Code-Sensei
"""


def binary_search(arr, target):
    """Binary search - O(log n) time complexity"""
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


def bubble_sort(arr):
    """Bubble sort - O(n²) time complexity"""
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def fibonacci_recursive(n):
    """Recursive fibonacci - O(2^n) time complexity"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dp(n):
    """Dynamic programming fibonacci - O(n) time complexity"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def two_sum(nums, target):
    """Two sum with hash map - O(n) time complexity"""
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None


def merge_sort(arr):
    """Merge sort - O(n log n) time complexity"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def find_max_subarray(arr):
    """Kadane's algorithm - O(n) time complexity"""
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # Test the functions
    print("Binary Search:", binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
    print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("Fibonacci (recursive):", fibonacci_recursive(10))
    print("Fibonacci (DP):", fibonacci_dp(10))
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Merge Sort:", merge_sort([38, 27, 43, 3, 9, 82, 10]))
    print("Max Subarray:", find_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
