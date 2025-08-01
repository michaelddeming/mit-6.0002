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

# Problem B.2: Writeup 

## Answer the following questions in the same PDF file ps1_answers.pdf.

1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there were 30 different egg weights. You do not need to implement a brute force algorithm in order to answer this.

It would be difficult to use Brute Force for larger len(egg_weights) due to the recursive call stack growing increasingly large because repeated work is done for duplicate inputs causing exponential time-complexity. 

2. If you were to implement a greedy algorithm for finding the minimum number of eggs needed, what would the objective function be? What would the constraints be? What strategy would your greedy algorithm follow to pick which eggs to take? You do not need to implement a greedy algorithm in order to answer this.

- Object Function: Minimum number of golden eggs needed to reach target weight.

- Constraints:
    - Weight limit of the ship.
    - Heavier eggs are more valuable as all eggs are the same volume. 
    - Unlimited number of eggs.

- Strategy: Always take the heaviest egg that will fit within the limit, else continue on to the next egg until the limit reaches 0.


3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is optimal or give an example of when it will not return the optimal solution. Again, you do not need to implement a greedy algorithm in order to answer this.

A greedy algorithm is locally optimal, meaning it always makes the best decision at each step without considering the broader consequences. This lack of foresight can lead to suboptimal results. In some systems, choosing a smaller or less valuable item early on may unlock better combinations later. If you always select the largest egg that fits, the algorithm follows a single path, potentially missing out on better combinations hidden in the search space. Therefore, greedy algorithms may fail to find the globally optimal solution, especially in cases where more than one sub-solution exists.