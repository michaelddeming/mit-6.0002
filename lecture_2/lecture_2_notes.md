# Lecture 1: Optimization Problems

## The Pros and Cons of Greedy

- Pros
    1. Easy to implement.
    2. Computationally efficient.
- Cons
    1. But does not always yield the best solution.
        - You don't even know how good the approximation is.

## Search Tree
- Given a list of items, the first item (root) is taken.
    - For each following item a decision is made:
        1. Take the item.
        2. Don't take the item.
    - Left-first, depth-first enumeration.
- Computational Complexity:
    - Time is based on number of nodes generated.
    - Number of levels is the number of items to choose from, n.
    - Number of nodes at level *i* is 2^*i*.

## Dynamic Programming
- Dynamic Programming: 
- Recursive Implementation of Fibonnaci
```py 
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```
- Memoization: Storing the results of previously done work to avoid repeating work.
    - Trade time for space.
    - Create a table (dict) to record what *work* we have already computed. 
        - In Fibonnaci, before computing `fib(x)`, check if the value of `fib(x)` is already stored in the table.
            - If so... take value from the table instead of computing.
            - If not, compute it and then add it to the table of seen computations.

- When to use memoization?
    1. **Optimal Substructure**: A globally optimal solution can be found by combining optimal solutions to local subproblems.
        - Example: `for x > 1, fib(x) = fib(x - 1) + fib(x - 2)`
        - Solve the *smaller* subproblems to achieve the *larger* result. 
        
    2. **Overlapping Subproblems**: Finding an optimal solution involves solving the same problems multiple times.
        - Example: `computing fib(x) multiple times`

- What about the 0/1 Knapsack Problem?
    - 