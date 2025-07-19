# Lecture 1: Introduction, Optimization Problems

- Optimization Model: 
    - Start with an **objective function** that's goal is to be maximized or minimized.

    - Constraints go *on-top* of the **objective function** to influence the outcomes/results.

    - Example: Knapsack Problem (backpack)
        - Robber has a backpack that he can only fill so much. What will he steal? 

    - Greedy Algorithm: Always choose the *best* available item if the knapsack is not full.
        - What is the *best* item? 
            - Raw value?
            - Least weight?
            - Ratio max(value/weight)?

    - Brute Force Algorithm:
        1. Enumerate all possible combinations of items. That is to say, generate all subsets of the set of subjects. This is called the **power set**.
        2. Remove all of the combinations whose total units exceeds the allowed weight.
        3. From the remaining combinations choose any one whose value is the largest.

- Lambda Function: used to create anon. functions.
    - lamba {id1, id2, ... idn}: {expression}
    - returns a function of n aruguments.  