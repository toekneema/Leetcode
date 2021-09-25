# returns an arr of 2*len(s) + 1
# so for ababbb
# returns [0, 1, 0, 3, 0, 3, 0, 1, 2, 3, 2, 1, 0]
# this represents the empty string, and then the even/odd idxs
# so the [000220] is for the even combos starting with 'ab' and the [133131] is the odd combos starting with 'a'

def manachers(S):
    A = '@#' + '#'.join(S) + '#$'
    Z = [0] * len(A)
    center = right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z[1:-1]