

def buble_sort(nums):

    for _ in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums


def insertion_sort(nums):
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums 

def meregeSort(nums):
    if len(nums) <= 1:
        return nums

    #get mid point 
    mid = len(nums)//2
    left,right = nums[:mid],nums[mid:]

    left_sort,right_sort = meregeSort(left),meregeSort(right) 
    sorted_nums = merege(left_sort, right_sort)
    return sorted_nums
def merege(nums1,nums2):
    mereged = []
    i,j = 0,0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            mereged.append(nums1[i])
            i += 1
        else:
            mereged.append(nums2[j])
            j += 1
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    return mereged + nums1_tail + nums2_tail

def quicksort(nums, start=0, end=None):
    print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    l, r = start, end-1
    
    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

nums = [1,3,4,3,5,7,2]
# print(insertion_sort(nums))
print(quicksort(nums))


#timc complexity analysis 
#buble sort time complexity O(n^2) and O(1) space complexit
#insertion sort time complexity O(n^2) and o(1) space complexity
#merege sort time complextiy O(nlogn) and space complexity O(n)
#quick sort time Worst case: O(n^2) for squee(un balanced) tree
# Best case: O(n*log(n))  space complexity O(log n) that is the height of the recursive call 