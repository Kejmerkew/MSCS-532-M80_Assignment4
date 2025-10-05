# Heap Data Structures: Implementation, Analysis, and Applications

## Running the Code

### Requirements

* Python 3.8+
* No external libraries required (uses only the standard library)

### Steps

1. Clone this repository or download the files.
2. Open a terminal in the project folder.
3. Run the program with:

   ```bash
   python HeapSort.py
   ```

There will be three outputs:

1. A **Heapsort demo** showing the original and sorted array.
2. A **Scheduler simulation** that executes tasks based on priority.
3. A **Sorting algorithm comparison** table measuring runtime for Heapsort, Quicksort, Merge Sort, and Timsort across different input sizes.

---

## Summary of Findings

* **Heapsort Performance:** Consistently runs in O(n log n) time across best, average, and worst cases.
* **Space Complexity:** Requires only O(1) auxiliary space since it operates in-place.
* **Scheduler Application:** Demonstrated that heaps efficiently handle task prioritization in operating system scheduling.
* **Comparison with Other Algorithms:**

  * Quicksort and Merge Sort performed faster on average for large inputs.
  * Python’s built-in **Timsort** significantly outperformed all other algorithms in practice.
  * Despite this, Heapsort remains valuable due to its predictable time complexity and low memory overhead.

---
