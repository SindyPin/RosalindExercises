""" Rabbits and Recurrence Relations: http://rosalind.info/problems/fib/
When finding the nn-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation
to generate terms for progressively larger values of nn. This problem introduces us to the computational technique
of dynamic programming, which successively builds up solutions by using the answers to smaller cases.
Given: Positive integers n≤40n≤40 and k≤5k≤5.
Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
More info:
https://medium.com/codingblackfemales/understanding-the-fibonacci-series-algorithm-rabbits-and-recurrence-eab9b4bdad5c
https://chrispresso.coffee/2019/02/21/rosalind-rabbits-and-recurrence-relations/
Function that calculates the total number of rabbits in a given month based on their reproductive cycle"""

months = int(input("Write the number of months: "))
rabbit_pairs = int(input("Write the number of rabbit pairs: "))


def rabbit_recursive(months, rabbit_pairs):
    if months < 2:
        return months
    else:
        return rabbit_recursive(months-1, rabbit_pairs) + rabbit_recursive(months-2, rabbit_pairs) * rabbit_pairs


print(rabbit_recursive(months, rabbit_pairs))
