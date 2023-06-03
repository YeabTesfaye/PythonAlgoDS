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

    def count_rotation_recursive(self):
        def condition(mid):
            next_index = (mid + 1) % len(self.arr)
            prev_index = (mid - 1) % len(self.arr)
            return (
                self.arr[mid] < self.arr[next_index]
                and self.arr[mid] < self.arr[prev_index]
            )
        def binary_search(low, high, condition):
            while low <= high:
                mid = (low + high) // 2
                if condition(mid):
                    return mid
                elif self.arr[mid] < self.arr[high]:
                    high = mid - 1
                else:
                    low = mid + 1
            return 0
        return binary_search(0, len(self.arr) - 1, condition)

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


    def handle_reapeating_number(self):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low + high) // 2
            next_index = (mid + 1) % len(self.arr)
            prev_index = (mid - 1) % len(self.arr)

            if self.arr[mid] < self.arr[next_index] and self.arr[mid] < self.arr[prev_index]:
                return mid

            # If the elements at mid, low, and high are equal, we can't determine which half to search
            # In this case, we decrement high and increment low to exclude the duplicates
            if self.arr[mid] == self.arr[low] == self.arr[high]:
                high -= 1
                low += 1
            # If the element at mid is equal to the element at high, search in the left half
            elif self.arr[mid] == self.arr[high]:
                high = mid - 1
            # If the element at mid is equal to the element at low, search in the right half
            elif self.arr[mid] == self.arr[low]:
                low = mid + 1
            # If the element at mid is less than the element at high, search in the left half
            elif self.arr[mid] < self.arr[high]:
                high = mid - 1
            # Otherwise, search in the right half
            else:
                low = mid + 1

        return 0



# Example usage
arr = [4,5, 6, 9, 0, 2, 3]
rotation = Rotation(arr)
rotations = rotation.count_rotation()
rotations = rotation.count_rotation_linear()
rotations = rotation.count_rotation_recursive()
print(rotations)  # Output: 4
print(rotation.search_in_rotated_array(3))

##for duplicates 
duplicates = [4, 5, 6, 6, 6, 9, 0, 2, 3, 4]
duplicates_rotation = Rotation(duplicates)
# print(duplicates_rotation.handle_reapeating_number())





'''
to count just try to find the index of the smallest element in the array
'''