"""
Een bucket sort begint met een een-dimensionale array van n positieve nummers die gesorteerd worden en een twee-dimensionale array van integers, 
met rijen genummerd van 0 tot 9 en kolommen geïndexeerd van 0 tot n-1. Elke rij in de twee-dimensionale array heeft een bucket.  Het algoritme werkt dan alsvolgt:

- Plaats elke waarde van de een-dimensionale array in een rij van de bucket array, gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. Deze stap heet de distribution pass.
- Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.
- Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). Na de laatste gathering pass is de array gesorteerd.
"""

import math

def bucket_sort(array): 
    buckets = [[] for _ in range(10)]
    max_length = len(repr(max(array)))

    for n in range(1, max_length+1):
        count = 0
        for number in array:
            i = math.floor((number % 10**n) / 10**(n-1))
            buckets[i].append(number)

        for bucket in buckets:
            for number in bucket:
                array[count] = number
                count += 1

        buckets = [[] for _ in range(10)]
    return array

if __name__ == "__main__":
    print(bucket_sort([97, 3, 100, 93, 874, 74, 73]))
