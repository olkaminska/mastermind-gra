import random

print('LEGENDA: \n :( - wrong guess \n :0 - wrong position \n :) - u got this one right \n colors: y, o, r, g, p, b \n')

colour_list = ['y', 'o', 'r', 'g', 'p', 'b']


def stat(pos=[]):
    count = 0
    proc = 0
    for i in range(0, 4):
        if (pos[i] == 1):
            count = count + 1
    proc = (count / 4) * 100
    return proc


def change(pos=[]):
    for i in range(0, 4):
        if pos[i] == 1:
            pos[i] = ':)'
        if pos[i] == 0:
            pos[i] = ':('
        if pos[i] == 2:
            pos[i] = ':0'

    print(pos)


def game(code=[]):
    statistics = []
    i = 10
    pom = 1
    wrong = 0
    win = [1, 1, 1, 1]
    may = 2
    pos = []

    while pos != win or i > 0:
        print(str(pom) + " turn| Guess code: ")
        pos = [input(), input(), input(), input()]

        for g in range(0, 4):
            if pos[g] == code[g]:
                pos[g] = win[g]
            if pos[g] != win[g]:
                for p in range(0, 4):
                    if p != g:
                        if pos[g] == code[p]:
                            pos[g] = may
            if pos[g] != win[g] and pos[g] != may:
                pos[g] = wrong

        i = i - 1
        statistics.append(stat(pos))
        print()
        change(pos)
        print("Statistics: ")
        for i in range(0, pom):
            print("Turn " + str(pom) + " - " + str(statistics[i]) + "% right")
        print()
        pom = int(pom) + 1
        if pos == win:
            print('\n \n YOU WIN')
            break

    if i == 0: print('\n \n LOSER!')


def dif():
    code = [random.choice(colour_list), random.choice(colour_list), random.choice(colour_list),
            random.choice(colour_list)]
    print(code)
    game(code)


def eas():
    code = ['', '', '', '']
    for i in range(0, 4):
        code[i] = random.choice(colour_list)
        colour_list.remove(code[i])
    print(code)
    game(code)

    print(code)


def main():
    print("choose level: easy-1, difficult-2")
    level = int(input())

    if (level == 2):
        dif()

    if (level == 1):
        eas()


main()