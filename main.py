board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
line = "--------------"

def rules():
    print("Правила игры")
    print("Игроки по очереди ставят на свободные клетки поля 3×3 знаки")
    print("Первый, выстроивший в ряд 3 своих фигуры выигрывает")
    print("Если игроки заполнили все 9 ячеек партия считается закончившейся в ничью")
    print("Веселитесь")


def print_board():
    print(line)
    for row in board:
        print("|", row[0], "|", row[1], "|", row[2], "|")
        print(line)


def valid(row, col):
    return all([
        row >= 0,
        row < 3,
        col >= 0,
        col < 3,
        board[row][col] == ' '
    ])


def make_move(player):
    valid_move = False
    while not valid_move:
        print_board()
        print("Игрок", player)
        row = int(input("Введи строку (0-2):"))
        col = int(input("Введи столбец (0-2):"))
        if valid(row, col):
            board[row][col] = player
            valid_move = True
        else:
            print("Клетка занята")


def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    return False


def play():
    rules()
    player = "X"
    while not check_win():
        make_move(player)
        if player == "X":
            player = "O"
        else:
            player = "X"
    print_board()
    print("Игрок", player, "Победил")


play()
