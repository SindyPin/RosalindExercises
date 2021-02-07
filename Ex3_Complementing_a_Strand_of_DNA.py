# Complementing a Strand of DNA: http://rosalind.info/problems/revc/
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss,
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string ss of length at most 1000 bp.
# Return: The reverse complement scsc of ss.

# More info:
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://www.geeksforgeeks.org/python-replace-multiple-characters-at-once/

DNA = input(str("Write a DNA sequence: "))
DNA_reverse = DNA[::-1]
DNA_reverse_replace = DNA_reverse.replace("T", "%temp%").replace("A", "T").replace("%temp%", "A")\
    .replace("G", "%temp%").replace("C", "G").replace("%temp%", "C")
print(DNA_reverse_replace)
