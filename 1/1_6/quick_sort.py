"""
Een bucket sort begint met een een-dimensionale array van n positieve nummers die gesorteerd worden en een twee-dimensionale array van integers, met rijen genummerd van 0 tot 9 en kolommen geïndexeerd van 0 tot n-1. Elke rij in de twee-dimensionale array heeft een bucket.  Het algoritme werkt dan alsvolgt:

- Plaats elke waarde van de een-dimensionale array in een rij van de bucket array, gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. Deze stap heet de distribution pass.
- Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.
- Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). Na de laatste gathering pass is de array gesorteerd.
"""

def partition(arr, start, end):
    i = (start - 1)
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    i = i+1
    arr[i], arr[end] = arr[end], arr[i]
    return i

# Function which implements quick sort
def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)

        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

    return arr


if __name__ == "__main__":
    lst = [97, 3, 100, 93, 874, 74, 73]
    n = len(lst) - 1
    print(quick_sort(lst, 0, n))
