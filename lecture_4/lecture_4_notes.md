# Lecture 4: Stochastic Thinking

- Newtonian Mechanics: Every effect has a cause.
    - The world can be understood causally.

- Copenhagen Doctrine (Bohr and Heisenberg) of **causal nondeterminism**: At its very most fundamental level, the behavior of the physical world cannot be predicted.
    - "x is highly likely to occur", but not of the form "x is certain to occur".
    - **predictive nondeterminism**: 
        - Our lack of knowledge does not allow us to make accurate predictions.
        - Therefore we might as well treat the world as inherently unpredictable.

- Stochastic Processes: An ongoing process where the next state might depend on both the previous states and **some random element**. 

```py
import random
def rollDie():
    """Returns a random int between 1 and 6."""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ""
    for i in range(n):
        result += str(rollDie())
    print(result)
```

- Three Basic Facts About Probability:
    1. Probabilities are always in the range of 0 to 1. 0 if impossible, and 1 if guaranteed.
    2. If the probability of an event occuring is *p*, the probability of it not occuring is *1 - p*. 
    3. When events are **independent** of eachother, the probabilty of all the events occuring is equal to the **product** of the probabilities of each of the events occuring.
        - Independence: 2 events are **independent** if the outcomes of one event has no influence on the outcome of the other.
    
- Simulation of Die Rolling

```py
def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ""
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=', round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=', round(estProbability, 8))

runSim('11111', 1000, '11111')
```

- Pseudorandom Numbers: Given one number, the next number is "randomly" generated, the starting place is called a *seed*. The same *seed* will produce the same sequence of "random" numbers. 
    - Typically computers use the **timestamp** for the seed at that given time to generate "random" numbers, but not actually random.

- Morals
    1. It takes a lot of trials to get a good estimate of the frequency of occurances of a rare event. 
    2. One should not confuse the **sample probability** with the actual probability.
    3. There was really no need to do this by simulation, since there is a perfectly good closed form answer. We will see many examples where this is not true. 

- Simulation Models:
    - A descrtiption of computations that provide useful information about the possible behaviors of the system being modeled.
    - Descriptive NOT prescriptive.
    - Only an approximation to reality.

- Random Walks