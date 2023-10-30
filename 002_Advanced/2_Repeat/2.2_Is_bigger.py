# программа подсчета количества чисел, которые больше предшествующего им в этом списке числа

sequence = [int(_) for _ in input().split()]
counter = 0


def bigger_or_not(seq):
    if seq[1] > seq[0]:
        seq.pop(0)
        return True
    else:
        seq.pop(0)


for _ in range(len(sequence) - 1):
    if bigger_or_not(sequence):
        counter += 1

print(counter)