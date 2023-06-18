# Sorting Algorithms

This repository contains various sorting algorithms implemented in Python. Each algorithm is described below along with its time and space complexities.

## Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the entire array is sorted.

| Method       | Description                                 | Time Complexity | Space Complexity |
|--------------|---------------------------------------------|-----------------|------------------|
| bubble_sort  | Sorts the given array using Bubble Sort      | O(n^2)          | O(1)             |

## Insertion Sort

Insertion Sort is a simple comparison-based sorting algorithm. It builds the final sorted array one element at a time by repeatedly inserting a given element into the correct position.

| Method         | Description                                      | Time Complexity | Space Complexity |
|----------------|--------------------------------------------------|-----------------|------------------|
| insertion_sort | Sorts the given array using Insertion Sort        | O(n^2)          | O(1)             |

## Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm. It divides the unsorted list into sublists until each sublist contains only one element. Then, it repeatedly merges sublists to produce a sorted final list.

| Method      | Description                               | Time Complexity | Space Complexity |
|-------------|-------------------------------------------|-----------------|------------------|
| merge_sort  | Sorts the given array using Merge Sort    | O(n log n)      | O(n)             |

## Quick Sort

Quick Sort is a comparison-based sorting algorithm that follows the divide-and-conquer approach. It selects an element as the pivot and partitions the array around the pivot. It recursively sorts the subarrays before and after the pivot.

| Method     | Description                             | Time Complexity | Space Complexity |
|------------|-----------------------------------------|-----------------|------------------|
| quicksort  | Sorts the given array using Quick Sort  | O(n log n)     | O(log n)         |

Note: n is the number of elements in the list.
