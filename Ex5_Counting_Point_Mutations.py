""" Counting Point Mutations: http://rosalind.info/problems/hamm/
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
More info: https://neilsonwilson.github.io/counting-point-mutations.html"""


def hamming_distance(s, t):
    ham_distance = 0
    for i in range(0, len(s)):
        if s[i] == t[i]:
            continue
        else:
            ham_distance += 1
    return ham_distance


s = input("Write the first seq: ")
t = input("Write the second seq: ")

print(hamming_distance(s, t))
