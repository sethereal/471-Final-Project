# CS471 Spring 2024: PRODCONS Report

## Seth Groves

## Link to PROD CON OUTPUT FILE: [PRODCON](PRODCONOutput.txt)

## Findings

During the implementation and countless hours of debugigng, I worked out several issues were identified and resolved:

    Incorrect calculation of sale month in local statistics
    Duplicate updates of global statistics
    Incorrect month-wise total sales calculation
    Adjustments needed for updating global statistics with month-wise totals

After addressing these issues, the program produced accurate local and global statistics for each combination of producers and consumers.

For the sake of keeping this document organized, I have attached the PRODCON output [here](PRODCONOutput.txt) and at the top of the page, instead of directly in this file to keep the length down.

## Conclusion

 I successfully implemented a solution to the producer-consumer problem in a retail chain scenario -- the program effectively handled different combinations of producers and consumers, providing detailed local and global sales statistics. After flattening all the bugs out, being able to see how the shared buffer ensured thread safety and smooth communication between producers and consumers was rewarding after several and several hours put into it. This project serves as a hands-on example of how the producer-consumer pattern can be applied to solve real-world challenges. It showcases the importance of meticulous design, effective synchronization mechanisms, and seamless data sharing in concurrent systems.
