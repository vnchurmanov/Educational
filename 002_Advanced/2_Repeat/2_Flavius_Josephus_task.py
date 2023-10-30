# n человек, пронумерованных числами от 11 до nn, стоят в кругу.
# Они начинают считаться, каждый kk-й по счету человек выбывает из круга,
# после чего счет продолжается со следующего за ним человека. Программа определяет номер человека,
# который останется в кругу последним
n, k = (int(input()) for _ in range(2))

competitors = [_ for _ in range(1, n + 1)]
counter = 1

# FIFO logic
def first_to_last(seq):
    seq.insert(len(seq), seq[0])
    seq.pop(0)
    return seq


while len(competitors) != 1:
    for player in competitors:
        if counter != k:
            counter += 1
            first_to_last(competitors)
        else:
            counter = 1
            competitors.pop(0)

print(competitors[0])
