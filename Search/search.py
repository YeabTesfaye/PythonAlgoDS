class Search:
    """
    Class for implementing various search algorithms.
    """

    def __init__(self, arr):
        """
        Initialize the Search object with an array.

        Args:
        - arr: The array to perform the search operations on.
        """
        self.arr = arr

    def binary_search(self, target):
        """
        Perform binary search on the array iteratively.

        Args:
        - target: The value to search for.

        Returns:
        - The index of the target value if found, otherwise -1.

        TimeComplexity:
        - O(n) where n is the length of the array 
        - SpaceComplexity:O(1) means constant space for variable declaration 
        """
        low, high = 0, len(self.arr) - 1

        while high >= low:
            mid = (low + high) // 2

            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def binary_search_recursive(self, target, low, high):
        """
        Perform binary search on the array recursively.

        Args:
        - target: The value to search for.
        - low: The lower index of the search range.
        - high: The upper index of the search range.

        Returns:
        - The index of the target value if found, otherwise -1.

        TimeComplexity:
        - O(logn) where n is the length of the array 
        - SpaceComplexity:O(1) means constant space for variable declaration 
        """
        if low > high:
            return -1
        mid = (low + high) // 2
        if self.arr[mid] == target:
            return mid
        if self.arr[mid] < target:
            return self.binary_search_recursive(target, mid + 1, high)
        else:
            return self.binary_search_recursive(target, low, mid - 1)

    def linear_search(self, target):
        """
        Perform linear search on the array.

        Args:
        - target: The value to search for.

        Returns:
        - The index of the target value if found, otherwise -1.

        TimeComplexity:
        - O(n) where n is the length of the array 
        - SpaceComplexity:O(1) means constant space for variable declaration 
        """
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1


# Dynamic testing
arr = [2, 5, 7, 10, 15, 20]
search = Search(arr)

target = 2
print("Binary Search (Iterative):", search.binary_search(target))
print("Binary Search (Recursive):", search.binary_search_recursive(target, 0, len(arr) - 1))
print("Linear Search:", search.linear_search(target))
