"""Algorytm rekurencyjny składa się z następujących kroków:

    przenieś (rekurencyjnie)  n-1 krążków ze słupka A na słupek B posługując się słupkiem C,
    przenieś jeden krążek ze słupka A na słupek C,
    przenieś (rekurencyjnie)  n-1 krążków ze słupka B na słupek C posługując się słupkiem A"""


def hanoi(n, a, b, c):  # hanoi(elementy, z, do, uzywajac do tego)
    if n == 1:
        print(a, "do", c)
    else:
        hanoi(n-1, a, c, b)
        print(a, 'do', c)
        hanoi(n - 1, b, a, c)


hanoi(3, "A",  "B",  "C")
