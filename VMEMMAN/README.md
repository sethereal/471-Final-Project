# CS471 Spring 2024: Virtual Memory Management Problem

## James Tieu

### Overview

For the VMEMMAN (Virutal Memory Management) portion of this assignment, we are to compare the performance of four different page replacing algorithms: FIFO, LRU, MRU, and Optimal. We are to use these algorithms with the text file containing virtual addresses that are being referenced by a single program. We are to collect and print the following statistics: Page Size, Number of Pages, Page Replacement Algorithm Used, and Page Fault Percentage.

The Report.md file contains those statistics along with the summary and conclusion of those runs.

Based off the problem, I created four classes (one for each algorithm) and one main class to run the program.

1. `fifo.py`
    This class is responsible for simulating the FIFO (First In, First Out) page replacement algorithm in a memory management context. It maintains a queue of pages to track which page was loaded first and should be replaced next when a page fault occurs.
2. `lru.py`
    This class is responsible for simulating the LRU (Least Recently Used) page replacement algorithm, which replaces the least recently accessed page when a page fault occurs and there is no free frame available. It manages a cache that records the order of page accesses, allowing it to identify which page has been unused for the longest period.

3. `mru.py`
    This class is responsible for simulating the MRU (Most Recently Used) page replacement algorithm, which contrasts with LRU by replacing the most recently used page. The class maintains a stack to keep track of page usage order.

4. `optimal.py`
    The Optimal class represents an ideal page replacement algorithm that has future knowledge of page accesses. It decides which page to replace by predicting which one will not be needed for the longest time in the future. 

5. `main.py`
    The driver file scipt is responsible for running the simulation with all the imported algorithms and global constants for page sizes and frame numbers. It reads in the data from `data.txt` and runs it through the `simulation` function to set up all the algorithms. After taking all the algorithms through the simulation, it prints out the output in the terminal and in the 'Report.md' file.

---

### Command

```python -m VMEMMAN.src.main```

Run this command in the terminal while in the project's root directory and it will print out the output.