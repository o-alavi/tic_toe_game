"""
The input for each player include two numbers separated with comma.
Each number is 0, 1, or 2.

For example, inputs:    0,0
                        2,2
                        1,0
                        0,2
"""


game = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


def display():
    print('     ', game[0], game[1], game[2])
    print('     ', game[3], game[4], game[5])
    print('     ', game[6], game[7], game[8])


end = True
lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check():
    for i in range(0, len(lst)):
        if [game[lst[i][0]], game[lst[i][1]], game[lst[i][2]]] == ['X', 'X', 'X'] or \
                [game[lst[i][0]], game[lst[i][1]], game[lst[i][2]]] == ['O', 'O', 'O']:
            return True
    return False


while end:
    pl1 = input("Player 1 (x,y): ")
    (x1, y1) = int(pl1[0]), int(pl1[2])
    if game[(x1 * 3) + y1] == "-":
        game[(x1 * 3) + y1] = "O"
    display()
    if check():
        print("Player 1 Won!")
        break
    pl2 = input("Player 2 (x,y): ")
    (x2, y2) = int(pl2[0]), int(pl2[2])
    if game[(x2 * 3) + y2] == "-":
        game[(x2 * 3) + y2] = "X"
    display()
    if check():
        print("Player 2 Won!")
        break
