# heap_assignment.py
"""
Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications

This file includes:
1. Heapsort implementation using a max-heap
2. Priority Queue implementation using a binary heap (max-heap)
3. A simple task scheduler simulation demonstrating priority-based execution
4. Empirical comparison of Heapsort with Quicksort, Merge Sort, and Timsort
"""

import random, time

# -------------------------
# Part 1: Heapsort
# -------------------------
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# -------------------------
# Part 2: Priority Queue
# -------------------------
class Task:
    """Represents a task for the scheduler"""
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"

class PriorityQueue:
    """Binary max-heap priority queue"""
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def increase_key(self, index, new_priority):
        if new_priority > self.heap[index].priority:
            self.heap[index].priority = new_priority
            self._heapify_up(index)

# -------------------------
# Part 3: Scheduler Simulation
# -------------------------
def scheduler_simulation():
    print("=== Scheduler Simulation ===")
    pq = PriorityQueue()
    
    # Generate some sample tasks
    tasks = [Task(f"T{i}", random.randint(1, 100)) for i in range(1, 11)]
    print("Generated Tasks:")
    for t in tasks:
        print(t)
    
    for t in tasks:
        pq.insert(t)

    print("\nExecuting tasks based on priority:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Executing {task}")

# -------------------------
# Part 4: Sorting Comparisons
# -------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
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

def compare_sorting_algorithms():
    print("\n=== Sorting Algorithm Comparison ===")
    arr_sizes = [1000, 5000, 10000]
    for size in arr_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        # Heapsort
        start = time.time()
        heapsort(arr.copy())
        print(f"Heapsort ({size}): {time.time() - start:.5f}s")

        # Quicksort
        start = time.time()
        quicksort(arr.copy())
        print(f"Quicksort ({size}): {time.time() - start:.5f}s")

        # Merge Sort
        start = time.time()
        merge_sort(arr.copy())
        print(f"Merge Sort ({size}): {time.time() - start:.5f}s")

        # Python’s built-in Timsort
        start = time.time()
        sorted(arr.copy())
        print(f"Timsort ({size}): {time.time() - start:.5f}s")
        print("-" * 40)

# -------------------------
# Main function
# -------------------------
if __name__ == "__main__":
    # Heapsort demonstration
    print("\n=== Heapsort Demo ===")
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Original array:", arr)
    heapsort(arr)
    print("Sorted array:  ", arr)

    # Scheduler demo
    scheduler_simulation()

    # Sorting algorithm comparison
    compare_sorting_algorithms()
