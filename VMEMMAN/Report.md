# CS471 Spring 2024: Virtual Memory Management Problem

## James Tieu

# Findings
- All algorithms, except Optimal, show a page fault percentage close to 100%, which is unusually high and suggests that either the page reference pattern is highly diverse (leading to few repetitions and thus many faults), or there is an issue with the simulation logic.

- As expected, the Optimal algorithm consistently outperforms the other three algorithms, demonstrating lower page fault percentages. This is in line with the understanding that the Optimal algorithm has future knowledge, allowing it to minimize page faults.

- Increasing the number of frames from 4 to 12 does not appear to significantly affect the page fault percentages for FIFO, LRU, and MRU algorithms. This could indicate that most page references are unique, causing high page turnover and faults regardless of the number of frames.

# Conclusions
- The Optimal algorithm's lower page fault percentages confirms its advantage over the other algorithsm when full knowledge of future requests is available.

- The similar page fault percentages for FIFO, LRU, and MRU suggest that for this particular set of page references, all three algorithms perform similarly under high page diversity.

- The lack of improvement with increased frames may point to an issue with the data set's diversity or a possible flaw with the simulation logic.



