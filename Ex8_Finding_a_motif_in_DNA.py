# Finding a Motif in DNA s: http://rosalind.info/problems/subs/
# Help link: http://blog.sciencenet.cn/blog-3158122-1084606.html

# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s
# (as a result, t must be no longer than s). The position of a symbol in a string is the total number of symbols found
# to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG"
# are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].
# A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the
# substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
# The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it
# occurs more than once as a substring of s (see the Sample below).

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Sample dataset: GATATATGCATATACTTATAT - ATAT
# Sample output: 2 4 10

# 1. Asking to the user for the DNA sequence and motif...
seq = input("Write the DNA sequence: ")
motif = input("Write the DNA motif: ")

# 2. Creating a loop for both DNA sequence and motif...
# NOTE 1: The range() function returns a sequence of numbers, starting from 0 by default and increments by 1
# (by default), and stops before a specified number --> range(start, stop, step)
# NOTE 2: (len(seq) - len(motif)) is the start position.
# NOTE 3: a = i is the evaluated position.
# NOTE 4: b is the result of adding the len of motif number + a (the evaluated position).
# NOTE 5: a + 1 because the first position in python is "0".
for i in range(len(seq) - len(motif) + 1):
    a = i
    b = len(motif) + a
    if seq[a:b] == motif:
        print(a+1)
        f''
