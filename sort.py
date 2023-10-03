# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Main program
while True:
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        bubble_sort(arr)
        print("Sorted Array (Bubble Sort):", arr)
    elif choice == '2':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        selection_sort(arr)
        print("Sorted Array (Selection Sort):", arr)
    elif choice == '3':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        insertion_sort(arr)
        print("Sorted Array (Insertion Sort):", arr)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
'''
Sure, let's analyze the time complexity of the three sorting algorithms
(Bubble Sort, Selection Sort, and Insertion Sort) and compare their performance on different types of input data.

1. **Bubble Sort**:
   - Worst-case Time Complexity**: O(n^2) - Occurs when the input array is in reverse order, and the algorithm has to perform swaps for each pair of elements.
   - Best-case Time Complexity**: O(n) - Occurs when the input array is already sorted, and no swaps are needed.
   - Average-case Time Complexity**: O(n^2) - It has a quadratic time complexity in most cases.
   - Stability**: Bubble Sort is a stable sort.
   - Performance on Different Input Data**:
     - Best for small datasets or nearly sorted data.
     - Poor performance on large or random datasets.

2. **Selection Sort**:
   -Worst-case Time Complexity**: O(n^2) - Regardless of input data, it always performs the same number of comparisons and swaps.
   - Best-case Time Complexity**: O(n^2) - Same as the worst-case as it always searches for the minimum element.
   - Average-case Time Complexity**: O(n^2) - It has a quadratic time complexity in all cases.
   - Stability**: Selection Sort is not stable.
   - Performance on Different Input Data**:
     - Similar performance on all types of input data.
     - Inefficient for large datasets.

3. **Insertion Sort**:
   - **Worst-case Time Complexity**: O(n^2) - Occurs when the input array is in reverse order.
   - **Best-case Time Complexity**: O(n) - Occurs when the input array is already sorted.
   - **Average-case Time Complexity**: O(n^2) - It typically performs better than Bubble and Selection Sort for random data.
   - **Stability**: Insertion Sort is a stable sort.
   - **Performance on Different Input Data**:
     - Well-suited for small datasets or nearly sorted data.
     - Better performance on already sorted or partially sorted data compared to Bubble and Selection Sort.

In comparison, Bubble Sort and Selection Sort have similar worst-case and average-case time complexities,
making them less efficient than Insertion Sort in most cases.
Insertion Sort performs better when the data is already partially sorted.
However, none of these sorting algorithms are suitable for very large datasets,
as their time complexity is quadratic.
'''

If you need a more efficient sorting algorithm for large datasets, consider algorithms like Quick Sort or Merge Sort, which have an average-case time complexity of O(n log n). These algorithms are generally preferred for larger datasets due to their better scalability.
