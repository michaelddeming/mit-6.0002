# Problem A.5: Writeup 

## Answer the following questions in a PDF file called ps1_answers.pdf. 
1.  What were your results from compare_cow_transport_algorithms? Which 
algorithm runs faster? Why? 

My results for the `compare_cow_transport_algorithms` are as follows:
- Greedy: 1.0967254638671875e-05 seconds
- Brute Force: 0.19210410118103027 seconds
- Performance Difference: ~1751515% 

The Greedy algorithm runs faster because it chooses cows based on the max weight available within the bounds of the remaining weight limit. 

The Brute Force algorithm exhausts all possible scenarios up-front, exponentially growing in proportion to the number of cows.

2.  Does the greedy algorithm return the optimal solution? Why/why not? 

The Greedy algorithm does not always return the optimal solution as it does not take into account any future outcomes or cascading impact. It only evaluates the input at face-value on each pass. The solution could be an optimal one, but could also have room for improvement.


3.  Does the brute force algorithm return the optimal solution? Why/why not?

The Brute Force algorithm does return the optimal solution as it evaluates the conditions across all possible combinations of trip and returns an answer that best satisfies satisfies the weight limit and minimizes the number of trips.