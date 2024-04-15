# CS471 Spring 2024: Prod-Con Problem

## Seth Groves

For the PRODCON portion of this assignment, we were to tackle the producer-consumer problem. Given a shared buffer, I was to create an object that consisted of sales date, storeID, the register number, and the sale amount.

From the described requirements, I created five classes, and a main driver as follows:

1. `ProducerClass.py`  
    The Producer class is in charge of producing sales records. Each record contains information such as sales date, store ID, register number, and sale amount. The producers randomly generate these records and place them in the shared buffer Per the instructions, Producer will generate 500 sale records.

2. `ConsumerClass.py`  
    The Consumer class is responsbile for reading sales records from the shared buffer and compute sales statistics. Each consumer maintains local statistics, including storewide totals, month-wise totals, and an aggregate total. Once all sales records have been processed, the consumers add their local statistics to the global statistics.

3. `SharedBuffer.py`  
    This class is directly responsible for adding and removing of records, checking the buffer capacity, and also providing the items produced.

4. `GlobalStats.py`  
    Per the name, this class maintains the global sales statistics, including storewide totals, month-wise totals, and an aggregate total. It provides methods to update the global statistics based on the local statistics computed by the consumers.

5. `StoreSimulation.py`  
 The StoreSimulation class orchestrates the entire simulation. It creates the producers, consumers, and shared buffer instances. It starts the producer and consumer threads and waits for them to complete. Once all threads have finished, it collects the local statistics from the consumers, updates the global statistics, and prints the results.

6. `Main.py`  
    The Driver file, `main.py`, It creates instances of the StoreSimulation class with different configurations (number of producers and consumers) and runs the simulations. It also measures the total simulation time and prints the global statistic

---

## Command

```python -m PRODCONS.src.main```

Run this command in the terminal while in the project's root directory and it will print out the output.
