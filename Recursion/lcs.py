
''' 
QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences.
 E.g. Given the strings "serendipitous" and "precipitation", 
the longest common subsequence is "reipito" and its length is 7.
'''

def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcq_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcq_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcq_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)

        # return max(lcq_recursive(seq1, seq2, idx1 + 1, idx2), lcq_recursive(seq1, seq2,idx1, idx2 + 1))
    


def lcq_memo(seq1,seq2):
    memo = {}

    def recures(idx1=0,idx2=0):
        key = (idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recures(idx1 + 1, idx2 + 1)
        else:
            # option1 = recures(idx1  + 1, idx2)
            # option2 = recures(idx1, idx2 + 1)
            # memo[key] = max(option1,option2)
            memo[key] = max(recures(idx1+1,idx2), recures(idx1,idx2 + 1))
        return memo[key]
    return recures(0,0)

def lcq_dynamic(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[j + 1][i + 1] = 1 + table[j][i]
            else:
                table[j + 1][i + 1] = max(table[j + 1][i], table[j][i + 1])
    return table[-1][-1]


T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]



for test in lcq_tests:
    result = lcq_dynamic(**test['input'])
    print("Test Passed:", result == test['output'])
    print()


# for test in lcq_tests:
#     result = lcq_memo(**test['input'])
#     print("Test Passed:", result == test['output'])
#     print()

# for test in lcq_tests:
#     result = lcq_recursive(**test['input'])
#     print("Test Passed:", result == test['output'])
#     print()

'''
time complexity

the worest case occur when the two elements doesn't have a commonn sequence at that time we'll have two 
sub trees for each call the time complexity we'll become O(2^m+n) where m = len(seq1) and n = len(seq2)
this is for the recursive solution 

but for  memoized version is O(m*n) the same is for the dynamic version 
'''
