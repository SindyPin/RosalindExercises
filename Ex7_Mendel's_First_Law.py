# Mendel's First Law: http://rosalind.info/problems/iprb/
# Help Link: https://www.youtube.com/watch?v=8X7WNs6R2zQ

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k = homozygous dominant individuals for a factor = 2/6
# m = heterozygous individuals for a factor = 2/6
# n = homozygous recessive individuals for a factor = 2/6
#
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
# allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k = int(input("Type the number for the homozygous dominant individuals from the studied population: "))
m = int(input("Type the number for the heterozygous individuals from the studied population: "))
n = int(input("Type the number for the homozygous recessive individuals from the studied population: "))

# The total number of individuals in the population before choosing the first individual:
total_1 = k + m + n

# The total number of individuals in the population after choosing the first individual:
total_2 = (k + m + n) - 1

# The probability 1 (p1) of choosing a first parent (before combing the parents):
p1_k = k/total_1
p1_m = m/total_1
p1_n = n/total_1

# The probability 2 (p2) of combing a first k, m or n phenotype parent with a second one (after choosing the first one):
p2_k = k/total_2
p2_m = m/total_2
p2_n = n/total_2

# The probability 3 (p3) of combing a k, m or n phenotype parent with another same phenotype parent:
p3_k = (k-1)/total_2
p3_m = (m-1)/total_2
p3_n = (n-1)/total_2

# See the Punnet squares in my notebook to understand the next lines...

# Probability to having dominant phenotype offspring from parents with homozygous dominant phenotypes
# (k x k - k x m - k x n - m x k - n x k):
d_phen = 1

# Probability to having dominant phenotype offspring from parents with heterozygous phenotypes 1 (m x m):
het1_phe = 0.75

# Probability to having dominant phenotype offspring from parents with heterozygous phenotypes 2 (m x n - n x m):
het2_phe = 0.5

# Probability to having dominant phenotype offspring from parents with homozygous recessive phenotypes (n x n):
rec_phe = 0

# Final equation showing the probability to have individuals with dominant phenotypes from the given number of
# individuals from a certain population (number of individuals given by the user):
d1_offspring = (p1_k * p3_k * d_phen) + (p1_k * p2_m * d_phen) + (p1_k * p2_n * d_phen)
d2_offspring = (p1_m * p2_k * d_phen) + (p1_m * p3_m * het1_phe) + (p1_m * p2_n * het2_phe)
d3_offspring = (p1_n * p2_k * d_phen) + (p1_n * p2_m * het2_phe) + (p1_n * p3_n * 0)

d_total_offspring = d1_offspring + d2_offspring + d3_offspring

print(d_total_offspring)
