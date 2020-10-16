# Given a DNA string tt corresponding to a coding strand,
# its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

import re

dna = str(input("Please, enter a DNA sequence: "))

while True:
    if "b" in dna or "B" in dna or "d" in dna or "D" in dna or "e" in dna or "E" in dna or "f" in dna or "F" in dna or \
            "h" in dna or "H" in dna or "i" in dna or "I" in dna or "j" in dna or "J" in dna or "k" in dna \
            or "K" in dna or "l" in dna or "L" in dna or "m" in dna or "M" in dna or "n" in dna or "N" in dna \
            or "ñ" in dna or "Ñ" in dna or "p" in dna or "P" in dna or "q" in dna or "Q" in dna or "r" in dna \
            or "R" in dna or "s" in dna or "S" in dna or "u" in dna or "U" in dna or "v" in dna or "V" in dna \
            or "w" in dna or "W" in dna or "x" in dna or "X" in dna or "y" in dna or "Y" in dna or "z" in dna \
            or "Z" in dna in dna and dna.isalpha():
        print("There is something wrong in your input")
        dna = str(input("Please, try again... enter a true DNA sequence: "))
        continue
    elif "a" in dna or "A" in dna or "t" in dna or "T" in dna or "g" in dna or "G" in dna or "c" in dna or "C" in dna \
            and dna.isalpha():
        rna1 = re.sub("[^atcgATCG]", "", dna)
        rna2 = rna1.replace("T", "U").replace("t", "u")
        print(f"The RNA sequence for the given DNA is: {rna2.upper()}")
        break
    else:
        print("There is something wrong in your input")
        dna = str(input("Please, try again... enter a true DNA sequence: "))
        continue
