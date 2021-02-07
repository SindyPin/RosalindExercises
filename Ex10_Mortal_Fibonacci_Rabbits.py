# Mortal Fibonacci Rabbit: http://rosalind.info/problems/fibd/
# More info: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci
# http://oeis.org/


"""Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence
relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair
of offspring (one male, one female) each subsequent month.
Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all
rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months."""


def mortal_fibonacci(n, m):
    # Create an array of length m to keep track of the number of rabbits...
    rabbit_pairs = [0] * m
    # Start with one rabbit being alive with m months to live...
    rabbit_pairs[-1] = 1
    # Iterate over the number of n months to track the number of rabbits...
    for i in range(1, n):
        # Newborns...
        new_rabbits = sum(rabbit_pairs[:-1])
        # Shift ages left, i.e. getting older
        rabbit_pairs[:-1] = rabbit_pairs[1:]
        # Assign newborns
        rabbit_pairs[-1] = new_rabbits

    # At the end we have an array containing the number of rabbits alive
    # for each possible month in the rabbits lifespan (m).
    # The sum of all ages is then a representation of all rabbits currently alive.
    return sum(rabbit_pairs)


if __name__ == '__main__':
    print(mortal_fibonacci(6, 3))  # Prints 4

