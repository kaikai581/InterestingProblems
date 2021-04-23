#!/usr/bin/env python
'''
This is the problem I got on the phone screening on 4/23/2021.
I did not manage to solve it.
After the time was out, the manager hinted that this was a combinitorial problem, and instead of the resursion method I tried, it could actually be done sequentially.
After the interview, I came up with the following idea.

Problem: Given n pairs of parentheses, generate all valid permutations.
1. Generate all permutations.
2. ( gains 1 point, and ) gains -1 point. For each permutation, calculate the accumulated points one parenthesis by one parenthesis.
   If at any step the cumulative score is less than zero, remove that permutation.

Leetcode page:
https://leetcode.com/problems/generate-parentheses/
'''

from itertools import permutations
import argparse

def valid_permutation(par_str):
    score = 0
    for c in par_str:
        if c == '(': score += 1
        else:
            score -= 1
            if score < 0: return False
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--npairs', type=int, default=3)
    args = parser.parse_args()
    npairs = args.npairs

    base_par = '()'*npairs
    all_par_pers = list(set(permutations(base_par)))
    all_par_pers = [''.join(list(v)) for v in all_par_pers]
    
    res = all_par_pers.copy()
    for par_str in all_par_pers:
        if not valid_permutation(par_str): res.remove(par_str)
    
    print(res)
    