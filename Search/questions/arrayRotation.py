'''
you are given a list of numbers, obatined by rotating a sorted list unknown number of times.
write a function to determine the minimum number of times the original sorted list was rotated
to obtain the given list. Your function should have the worest-case complextity of O(log N),
where N is the length of the list. You can assume that all the number in the list are unique 

Example. The list [5,6,9,0,2,3,4] was obained by rotating the sorted list [0,2,3,4,5,6,9] 3 times

we define rotating a list as removing the last element of the list and add it before the first 
element. E.g rotating the list [3,2,4,1] produce [1,3,2,4]

"Sorting list" refers to a list where the elements are arranged in the increasing order

'''

class Rotation:
    def __init__(self, arr):
        self.arr = arr

    def count_rotation(self):
        low=0
        high=len(self.arr) - 1

        while low <= high:
            mid = (low+high)//2
            next_index = (mid+1)%len(self.arr)
            prev_index = (mid-1)%len(self.arr)
            # Check if the element at 'mid' is smaller than both its next and previous elements
            if self.arr[mid] < self.arr[next_index] and self.arr[mid] < self.arr[prev_index]:
                return mid
            elif self.arr[mid] < self.arr[high]:
                # If the element at 'mid' is smaller than the element at 'high', search in the left half
                high = mid - 1
            else:
                # Otherwise, search in the right half
                low = mid + 1
        return 0  
    def count_rotation_linear(self):
        position = 0

        while position < len(self.arr):
            if position > 0 and self.arr[position] < self.arr[position - 1]:
                return position
            position += 1
        
        return -1

    def search_in_rotated_array(self, target):

        low,high = 0,len(self.arr) - 1

        while low <= high:
            mid = (low+high)// 2

            if self.arr[mid] == target:
                return mid
            
            # If the left half is sorted 
            if self.arr[low] <= self.arr[mid]:
                # Check if the target is in the left half
                if self.arr[low]<=target<=self.arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                # If the right half is sorted
            else:
                # Check if the target is in the right half
                if self.arr[mid] <= target <= self.arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1


    def handle_repeating_numbers(self):
        pass


# Example usage
arr = [4,5, 6, 9, 0, 2, 3]
arr=[1,3]
rotation = Rotation(arr)
rotations = rotation.count_rotation()
rotations = rotation.count_rotation_linear()
print(rotations)  # Output: 4
print(rotation.search_in_rotated_array(3))

'''
Certainly! Let me clarify the statement.

In the given problem, we start with a sorted list of numbers. When we perform a rotation on this sorted list,
we remove the last element from the list and place it before the first element. This rotation operation shifts 
all the elements in the list to the right, and the last element becomes the new first element.

For example, if we start with the sorted list `[1, 2, 3, 4, 5]` and perform one rotation,
it becomes `[5, 1, 2, 3, 4]`. If we perform two rotations, it becomes `[4, 5, 1, 2, 3]`, and so on.

The goal of the problem is to determine the minimum number of times the original sorted list was rotated to obtain the given rotated list.

Now, here's the key insight: When we rotate a sorted list, the smallest element in the original sorted 
list moves to the beginning of the rotated list.

For example, consider the original sorted list `[0, 2, 3, 4, 5, 6, 9]`. If we rotate it three times,
 it becomes `[5, 6, 9, 0, 2, 3, 4]`. Notice that the smallest element, `0`, is now at the 3rd index of the rotated list.

Based on this observation, we can determine the minimum number of rotations by finding the index of the smallest element 
in the rotated list. The index of the smallest element corresponds to the number of rotations performed on the original sorted list.

In the implementation I provided earlier, the condition `self.arr[mid] < self.arr[next_index] and self.arr[mid] < self.arr[prev_index]` checks if the element at the middle index (`mid`) is smaller than both its next element (`next_index`) and previous element (`prev_index`). If this condition is true, it means that the element at `mid` is the smallest element in the rotated list. Therefore, we return `mid` as the number of rotations.

By finding the index of the smallest element, we are effectively determining how many times the original sorted list was rotated to obtain the given rotated list.

I hope this clarifies the context and the reasoning behind finding the index of the smallest element to determine the number of rotations.
'''