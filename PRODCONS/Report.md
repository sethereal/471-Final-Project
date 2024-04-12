# CS471 Spring 2024: PRODCONS Report

## Seth Groves

### Overview

For the PRODCON portion of this assignment, we were to tackle the producer-consumer problem. Given a shared buffer, I was to create an object that consisted of sales date, storeID, the register number, and the sale amount.

From the described requirements, I created four classes, and a main driver as follows:

1. `ProducerClass.py`  
    Responsible for producing a `sale` which is a dictonary that contains `sale_date`, `store_id`, `register_number`, and `sale_amount`. Per the instructions, Producer will generate 500 sale records.

2. `ConsumerClass.py`  
    The `ConsumerClass` is directly responsible for take `sales` from the buffer to compute the `local_stats` of the `sale_records` to append to the `GlobalStats` and also provide calculation for the `local_stats` too.

3. `SharedBuffer.py`  
    This class is directly responsible for adding and removing of records, checking the buffer capacity, and also providing the items produced.

4. `GlobalStats.py`  
    Per the name, this class is directly with providing the `storewide` `month` and `aggregate` total of the sales per the instructions of the project. This has a method to append incoming totals to the overall total, and utilizes the use of Python decorators (`@property`) to ensure that the values are appended in a thread-safe manner.

5. `Main.py`  
    The Driver file, `main.py`, is directly responsible for creating instances from each class to use in conjunction. This is also where `producers` and `consumers` are explicitly started as different threads.

---

### Issues I Ran Into

#### 1. Race Issue

![first issue](/PRODCONS/ReportResources/1.png)

 When I ran the program after I had fixed some minor issues with how I was calling `GlobalStats`, I noticed that the `ProducerClass` seemed to be producing way more entries than I needed. I added a counter to the `run` function, and to no surprise, it seemed that there was a race condition. As the iterations got closer to 500, it became more erratic and as expected, went over 500 iterations.
