
def fastFib(n, memo = {}):

    if n == 0 or n == 1:
        return 1
    
    # check if the current n is in the memo dict as a key. If Python raises a KeyError (detecting no matching key), perfrom the computation and save the result into the memo. If Python finds a matching key for the current n in the memo dict, return the precomputed results of fastFib(n).
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result
    

