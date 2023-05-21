import filecmp
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command
import copy
from typing import List, Any


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear screen command as function of OS
    command = 'cls' if system_name().lower() == 'windows' else 'clear'

    # Action
    system_call([command])


def check_move(board, x, y, color, dir):
    moves = []
    if dir == 0:
        if x < 7:
            for i in range(x, 7):
                i = i + 1
                if color == Color.black:
                    if board.get_color(i, y) == Color.empty:
                        moves.append([i, y])
                    elif board.get_color(i, y) == Color.black:
                        # moves.append([i - 1, y])
                        break
                    else:
                        moves.append([i, y])
                        break
                else:
                    if board.get_color(i, y) == Color.empty:
                        moves.append([i, y])
                    elif board.get_color(i, y) == Color.black:
                        moves.append([i, y])
                        break
                    else:
                        # moves.append([i - 1, y])
                        break
        if x > 0:
            for i in range(x):
                i = x - i - 1
                if color == Color.black:
                    if board.get_color(i, y) == Color.empty:
                        moves.append([i, y])
                    elif board.get_color(i, y) == Color.black:
                        # moves.append([i + 1, y])  # или если там уже лежит такой ход то ничего не добавлять?
                        break
                    else:
                        moves.append([i, y])
                        break
                else:
                    if board.get_color(i, y) == Color.empty:
                        moves.append([i, y])
                    elif board.get_color(i, y) == Color.black:
                        moves.append([i, y])
                        break
                    else:
                        # moves.append([i + 1, y])
                        break

    if dir == 1:
        if y < 7:
            for i in range(y, 7):
                i = i + 1  # вниз
                if color == Color.black:
                    if board.get_color(x, i) == Color.empty:
                        moves.append([x, i])
                    elif board.get_color(x, i) == Color.black:
                        # moves.append([x, i - 1])
                        break
                    else:
                        moves.append([x, i])
                        break
                else:
                    if board.get_color(x, i) == Color.empty:
                        moves.append([x, i])
                    elif board.get_color(x, i) == Color.black:
                        moves.append([x, i])
                        break
                    else:
                        # moves.append([x, i - 1])
                        break
        if y > 0:
            for i in range(y):
                i = y - i - 1  # вверх
                if color == Color.black:
                    if board.get_color(x, i) == Color.empty:
                        moves.append([x, i])
                    elif board.get_color(x, i) == Color.black:
                        # moves.append([x, i + 1])
                        break
                    else:
                        moves.append([x, i])
                        break
                else:
                    if board.get_color(x, i) == Color.empty:
                        moves.append([x, i])
                    elif board.get_color(x, i) == Color.black:
                        moves.append([x, i])
                        break
                    else:
                        # moves.append([x, i + 1])
                        break

    if dir == 2:
        if x < 7 and y < 7:
            j = y
            for i in range(x, 7):
                i = i + 1
                j = j + 1
                if j < 8:
                    if color == Color.black:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            # moves.append([i - 1, j - 1])
                            break
                        else:
                            moves.append([i, j])
                            break
                    else:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            moves.append([i, j])
                            break
                        else:
                            # moves.append([i - 1, j - 1])
                            break
        if x > 0 and y > 0:
            j = y
            for i in range(x):
                i = x - i - 1
                j = j - 1
                if j > -1:
                    if color == Color.black:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            # moves.append([i + 1, j + 1])
                            break
                        else:
                            moves.append([i, j])
                            break
                    else:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            moves.append([i, j])
                            break
                        else:
                            # moves.append([i + 1, j + 1])
                            break

    if dir == 3:
        if x < 7 and y > 0:
            j = y
            for i in range(x, 7):     # AAÆAÃÄAAAAAAAA
                i = i + 1
                j = j - 1
                if j > -1:
                    if color == Color.black:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            # moves.append([i - 1, j + 1])
                            break
                        else:
                            moves.append([i, j])
                            break
                    else:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            moves.append([i, j])
                            break
                        else:
                            # moves.append([i - 1, j + 1])
                            break
        if x > 0 and y < 7:
            j = y
            for i in range(x):
                i = x - i - 1
                j = j + 1
                if j < 8:
                    if color == Color.black:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            # moves.append([i + 1, j - 1])
                            break
                        else:
                            moves.append([i, j])
                            break
                    else:
                        if board.get_color(i, j) == Color.empty:
                            moves.append([i, j])
                        elif board.get_color(i, j) == Color.black:
                            moves.append([i, j])
                            break
                        else:
                            # moves.append([i + 1, j - 1])
                            break
    return moves


def check_king(board, x, y, color):

    if x < 7 and isinstance(board.board[y][x + 1], King) and board.board[y][x + 1].color == color:
        return False
    if x > 0 and isinstance(board.board[y][x - 1], King) and board.board[y][x - 1].color == color:
        return False
    if y < 7 and isinstance(board.board[y + 1][x], King) and board.board[y + 1][x].color == color:
        return False
    if y > 0 and isinstance(board.board[y - 1][x], King) and board.board[y - 1][x].color == color:
        return False
    if x < 7 and y < 7 and isinstance(board.board[y + 1][x + 1], King) and board.board[y + 1][x + 1].color == color:
        return False
    if x > 0 and y > 0 and isinstance(board.board[y - 1][x - 1], King) and board.board[y - 1][x - 1].color == color:
        return False
    if x > 0 and y < 7 and isinstance(board.board[y + 1][x - 1], King) and board.board[y + 1][x - 1].color == color:
        return False
    if x < 7 and y > 0 and isinstance(board.board[y - 1][x + 1], King) and board.board[y - 1][x + 1].color == color:
        return False

    return True


class Color(object):
    empty = 0
    black = 1
    white = 2


class Empty(object):
    color = Color.empty

    def is_empty(self):
        return True

    def get_moves(self, board, x, y):
        raise Exception('Error')

    def __repr__(self):
        return '.'


class ChessMan(object):
    IMG = None

    def is_empty(self):
        return False

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[0 if self.color == Color.white else 1]


class Pawn(ChessMan):
    IMG = ('♟', '♙')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.black:
            if y < 7 and board.get_color(x, y + 1) == Color.empty:
                moves.append([x, y + 1])
            if y < 7 and x < 7 and board.get_color(x + 1, y + 1) == Color.white:
                moves.append([x + 1, y + 1])
            if y < 7 and x > 0 and board.get_color(x - 1, y + 1) == Color.white:
                moves.append([x - 1, y + 1])
            if y == 1 and board.get_color(x, y + 2) == Color.empty:
                moves.append([x, y + 2])
        else:
            if y > 0 and board.get_color(x, y - 1) == Color.empty:
                moves.append([x, y - 1])
            if y > 0 and x > 0 and board.get_color(x - 1, y - 1) == Color.black:
                moves.append([x - 1, y - 1])
            if y > 0 and x < 7 and board.get_color(x + 1, y - 1) == Color.black:
                moves.append([x + 1, y - 1])
            if y == 6 and board.get_color(x, y - 2) == Color.empty:
                moves.append([x, y - 2])
        return moves


class King(ChessMan):
    IMG = ('♚', '♔')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.black:
            if y < 7 and (board.get_color(x, y + 1) == Color.empty or board.get_color(x, y + 1) == Color.white):
                if check_king(board, x, y + 1, Color.white):
                    moves.append([x, y + 1])
            if y < 0 and (board.get_color(x, y - 1) == Color.empty or board.get_color(x, y - 1) == Color.white):
                if check_king(board, x, y - 1, Color.white):
                    moves.append([x, y - 1])
            if x > 0 and (board.get_color(x + 1, y) == Color.empty or board.get_color(x + 1, y) == Color.white):
                if check_king(board, x + 1, y, Color.white):
                    moves.append([x + 1, y])
            if x < 7 and (board.get_color(x - 1, y) == Color.empty or board.get_color(x - 1, y) == Color.white):
                if check_king(board, x - 1, y, Color.white):
                    moves.append([x - 1, y])
            if y < 7 and x > 0 and \
                    (board.get_color(x + 1, y + 1) == Color.empty or board.get_color(x + 1, y + 1) == Color.white):
                if check_king(board, x + 1, y + 1, Color.white):
                    moves.append([x + 1, y + 1])
            if y > 0 and x > 0 and \
                    (board.get_color(x + 1, y - 1) == Color.empty or board.get_color(x + 1, y - 1) == Color.white):
                if check_king(board, x + 1, y - 1, Color.white):
                    moves.append([x + 1, y - 1])
            if y < 7 and x < 7 and \
                    (board.get_color(x - 1, y + 1) == Color.empty or board.get_color(x - 1, y + 1) == Color.white):
                if check_king(board, x - 1, y + 1, Color.white):
                    moves.append([x - 1, y + 1])
            if y > 0 and x < 7 and \
                    (board.get_color(x - 1, y - 1) == Color.empty or board.get_color(x - 1, y - 1) == Color.white):
                if check_king(board, x - 1, y - 1, Color.white):
                    moves.append([x - 1, y - 1])

        else:
            if y < 7 and (board.get_color(x, y + 1) == Color.empty or board.get_color(x, y + 1) == Color.black):
                if check_king(board, x, y + 1, Color.black):
                    moves.append([x, y + 1])
            if y > 0 and (board.get_color(x, y - 1) == Color.empty or board.get_color(x, y - 1) == Color.black):
                if check_king(board, x, y - 1, Color.black):
                    moves.append([x, y - 1])
            if x > 0 and (board.get_color(x + 1, y) == Color.empty or board.get_color(x + 1, y) == Color.black):
                if check_king(board, x + 1, y, Color.black):
                    moves.append([x + 1, y])
            if x < 7 and (board.get_color(x - 1, y) == Color.empty or board.get_color(x - 1, y) == Color.black):
                if check_king(board, x - 1, y, Color.black):
                    moves.append([x - 1, y])
            if y < 7 and x > 0 and \
                    (board.get_color(x + 1, y + 1) == Color.empty or board.get_color(x + 1, y + 1) == Color.black):
                if check_king(board, x + 1, y + 1, Color.black):
                    moves.append([x + 1, y + 1])
            if y > 0 and x > 0 and \
                    (board.get_color(x + 1, y - 1) == Color.empty or board.get_color(x + 1, y - 1) == Color.black):
                if check_king(board, x + 1, y - 1, Color.black):
                    moves.append([x + 1, y - 1])
            if y < 7 and x < 7 and \
                    (board.get_color(x - 1, y + 1) == Color.empty or board.get_color(x - 1, y + 1) == Color.black):
                if check_king(board, x - 1, y + 1, Color.black):
                    moves.append([x - 1, y + 1])
            if y > 0 and x < 7 and \
                    (board.get_color(x - 1, y - 1) == Color.empty or board.get_color(x - 1, y - 1) == Color.black):
                if check_king(board, x - 1, y - 1, Color.black):
                    moves.append([x - 1, y - 1])
        return moves


class Rook(ChessMan):
    IMG = ('♜', '♖')

    def get_moves(self, board, x, y):
        moves = []
        for i in check_move(board, x, y, self.color, 0):
            moves.append(i)
        for j in check_move(board, x, y, self.color, 1):
            moves.append(j)
        return moves


class Bishop(ChessMan):
    IMG = ('♝', '♗')

    def get_moves(self, board, x, y):
        moves = []
        for i in check_move(board, x, y, self.color, 2):
            moves.append(i)
        for j in check_move(board, x, y, self.color, 3):
            moves.append(j)
        return moves


class Queen(ChessMan):
    IMG = ('♛', '♕')

    def get_moves(self, board, x, y):
        moves = []
        for i in check_move(board, x, y, self.color, 0):
            moves.append(i)
        for j in check_move(board, x, y, self.color, 1):
            moves.append(j)
        for i in check_move(board, x, y, self.color, 2):
            moves.append(i)
        for j in check_move(board, x, y, self.color, 3):
            moves.append(j)
        return moves


class Knight(ChessMan):
    IMG = ('♞', '♘')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.black and x + 1 <= 7 and y - 2 >= 0 and \
                (board.get_color(x + 1, y - 2) == Color.empty or board.get_color(x + 1, y - 2) == Color.white):
            moves.append([x + 1, y - 2])
        if self.color == Color.black and x - 1 >= 0 and y - 2 >= 0 and \
                (board.get_color(x - 1, y - 2) == Color.empty or board.get_color(x - 1, y - 2) == Color.white):
            moves.append([x - 1, y - 2])
        if self.color == Color.black and x + 1 <= 7 and y + 2 <= 7 and \
                (board.get_color(x + 1, y + 2) == Color.empty or board.get_color(x + 1, y + 2) == Color.white):
            moves.append([x + 1, y + 2])
        if self.color == Color.black and x - 1 >= 0 and y + 2 <= 7 and \
                (board.get_color(x - 1, y + 2) == Color.empty or board.get_color(x - 1, y + 2) == Color.white):
            moves.append([x - 1, y + 2])
        if self.color == Color.black and x + 2 <= 7 and y + 1 <= 7 and \
                (board.get_color(x + 2, y + 1) == Color.empty or board.get_color(x + 2, y + 1) == Color.white):
            moves.append([x + 2, y + 1])
        if self.color == Color.black and x + 2 <= 7 and y - 1 >= 0 and \
                (board.get_color(x + 2, y - 1) == Color.empty or board.get_color(x + 2, y - 1) == Color.white):
            moves.append([x + 2, y - 1])
        if self.color == Color.black and x - 2 >= 0 and y + 1 <= 7 and \
                (board.get_color(x - 2, y + 1) == Color.empty or board.get_color(x - 2, y + 1) == Color.white):
            moves.append([x - 2, y + 1])
        if self.color == Color.black and x - 2 >= 0 and y - 1 >= 0 and \
                (board.get_color(x - 2, y - 1) == Color.empty or board.get_color(x - 2, y - 1) == Color.white):
            moves.append([x - 2, y - 1])

        if self.color == Color.white and x + 1 <= 7 and y - 2 >= 0 and \
                (board.get_color(x + 1, y - 2) == Color.empty or board.get_color(x + 1, y - 2) == Color.black):
            moves.append([x + 1, y - 2])
        if self.color == Color.white and x - 1 >= 0 and y - 2 >= 0 and \
                (board.get_color(x - 1, y - 2) == Color.empty or board.get_color(x - 1, y - 2) == Color.black):
            moves.append([x - 1, y - 2])
        if self.color == Color.white and x + 1 <= 7 and y + 2 <= 7 and \
                (board.get_color(x + 1, y + 2) == Color.empty or board.get_color(x + 1, y + 2) == Color.black):
            moves.append([x + 1, y + 2])
        if self.color == Color.white and x - 1 >= 0 and y + 2 <= 7 and \
                (board.get_color(x - 1, y + 2) == Color.empty or board.get_color(x - 1, y + 2) == Color.black):
            moves.append([x - 1, y + 2])
        if self.color == Color.white and x + 2 <= 7 and y + 1 <= 7 and \
                (board.get_color(x + 2, y + 1) == Color.empty or board.get_color(x + 2, y + 1) == Color.black):
            moves.append([x + 2, y + 1])
        if self.color == Color.white and x + 2 <= 7 and y - 1 >= 0 and \
                (board.get_color(x + 2, y - 1) == Color.empty or board.get_color(x + 2, y - 1) == Color.black):
            moves.append([x + 2, y - 1])
        if self.color == Color.white and x - 2 >= 0 and y + 1 <= 7 and \
                (board.get_color(x - 2, y + 1) == Color.empty or board.get_color(x - 2, y + 1) == Color.black):
            moves.append([x - 2, y + 1])
        if self.color == Color.white and x - 2 >= 0 and y - 1 >= 0 and \
                (board.get_color(x - 2, y - 1) == Color.empty or board.get_color(x - 2, y - 1) == Color.black):
            moves.append([x - 2, y - 1])

        return moves


def color_print(figure, color):
    color_bg = ""
    color_clear = "\033[0m"
    black = "\033[38;5;233m"
    white = "\033[38;5;233m"
    color_fig = ""
    color_bg_fig = ''
    if figure.color == 2:
        color_fig = white
    else:
        color_fig = black

    if color == 0:
        color_bg = "\033[48;5;179m"
        color_bg_fig = "\033[38;5;179m"
    if color == 1:
        color_bg = "\033[48;5;229m"
        color_bg_fig = "\033[38;5;229m"

    if figure.__class__ == Empty:
        print(color_bg + color_bg_fig + ' ' + '♚' + ' ' + color_clear, end='')
    else:
        print(color_bg + color_fig + ' ' + figure.IMG[figure.color - 1] + ' ' + color_clear, end='')


class Board(object):
    def __init__(self):
        self.board = [[Empty()] * 8 for i in range(8)]
        self.board[1][0] = Pawn(Color.black)
        self.board[1][1] = Pawn(Color.black)
        self.board[1][2] = Pawn(Color.black)
        self.board[1][3] = Pawn(Color.black)
        self.board[1][4] = Pawn(Color.black)
        self.board[1][5] = Pawn(Color.black)
        self.board[1][6] = Pawn(Color.black)
        self.board[1][7] = Pawn(Color.black)

        self.board[6][0] = Pawn(Color.white)
        self.board[6][1] = Pawn(Color.white)
        self.board[6][2] = Pawn(Color.white)
        self.board[6][3] = Pawn(Color.white)
        self.board[6][4] = Pawn(Color.white)
        self.board[6][5] = Pawn(Color.white)
        self.board[6][6] = Pawn(Color.white)
        self.board[6][7] = Pawn(Color.white)

        self.board[0][4] = King(Color.black)
        self.board[7][4] = King(Color.white)
        self.board[0][3] = Queen(Color.black)
        self.board[7][3] = Queen(Color.white)

        self.board[0][0] = Rook(Color.black)
        self.board[0][7] = Rook(Color.black)
        self.board[7][0] = Rook(Color.white)
        self.board[7][7] = Rook(Color.white)

        self.board[0][2] = Bishop(Color.black)
        self.board[0][5] = Bishop(Color.black)
        self.board[7][2] = Bishop(Color.white)
        self.board[7][5] = Bishop(Color.white)

        self.board[0][1] = Knight(Color.black)
        self.board[0][6] = Knight(Color.black)
        self.board[7][1] = Knight(Color.white)
        self.board[7][6] = Knight(Color.white)

        self.currentMoveColor = Color.white
        self.king_white = [[4, 7]]
        self.king_black = [[4, 0]]
        self.fig_moves_black = []
        self.fig_moves_white = []
        self.cmd = ''
        self.sp_cmd_black = []
        self.sp_cmd_white = []

    def get_color(self, x, y):
        return self.board[y][x].color

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        if self.board[xy_from[1]][xy_from[0]].is_empty():
            print('Ошибка: нет фигуры')
            return False
        else:
            if self.board[xy_from[1]][xy_from[0]].color != self.currentMoveColor:
                print('Ошибка: не тот цвет')
                return False

            m = b.get_moves(xy_from[0], xy_from[1])
            if xy_to in m:

                old_board = copy.deepcopy(self.board)
                self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]

                self.fig_moves_black = []
                self.fig_moves_white = []
                for y in range(8):
                    for x in range(8):
                        if not self.board[y][x].is_empty() and self.board[y][x].color == Color.black:
                            for i in b.get_moves(x, y):
                                if i not in self.fig_moves_black:
                                    self.fig_moves_black.append(i)
                        if not self.board[y][x].is_empty() and self.board[y][x].color == Color.white:
                            for i in b.get_moves(x, y):
                                if i not in self.fig_moves_white:
                                    self.fig_moves_white.append(i)
                # print('ходы черных:', fig_moves_black)
                # print('ходы белых:', fig_moves_white)

                if isinstance(self.board[xy_to[1]][xy_to[0]], King) and \
                        self.board[xy_to[1]][xy_to[0]].color == Color.white:
                    self.king_white = [[xy_to[0], xy_to[1]]]  # [[4, 7]]
                if isinstance(self.board[xy_to[1]][xy_to[0]], King) and \
                        self.board[xy_to[1]][xy_to[0]].color == Color.black:
                    self.king_black = [[xy_to[0], xy_to[1]]]

                # если координаты короля совпадают с координатами куда может
                # пойти фигура противоположного цвета то вызываем шах
                for i in self.king_white:
                    if i in self.fig_moves_black:
                        print('У ВАС ШАХ белым')
                        if self.currentMoveColor != Color.black:
                            self.board = old_board
                            return False

                for i in self.king_black:
                    if i in self.fig_moves_white:
                        print('У ВАС ШАХ черным')
                        if self.currentMoveColor != Color.white:
                            self.board = old_board
                            return False

                if self.board[xy_from[1]][xy_from[0]].color == Color.white:
                    self.sp_cmd_white.append(self.cmd)
                    self.currentMoveColor = Color.black
                else:
                    self.sp_cmd_black.append(self.cmd)
                    self.currentMoveColor = Color.white

                self.board[xy_from[1]][xy_from[0]] = Empty()
                return True

            else:
                print('Ошибка: неправильный ход')
                return False

    def show(self):
        print('')
        color = 0
        coord = 0
        for i in range(8):
            print(8 - i, end=' ')
            for j in range(8):
                color_print(self.board[i][j], color)
                if j != 7:
                    color += 1
                    if color == 2:
                        color = 0
            if i == 0:
                print('           белые', end=' ')
                print('          черные', end=' ')
            if i != 0:
                if len(self.sp_cmd_white) > 7:
                    print('   ', len(self.sp_cmd_white) - 7 + i, '      ', self.sp_cmd_white[len(self.sp_cmd_white) - 8 + i], end='  ')
                elif i <= len(self.sp_cmd_white):
                    print('   ', i, '      ', self.sp_cmd_white[i-1], end='  ')

                if len(self.sp_cmd_black) < len(self.sp_cmd_white):
                    x = 1
                else:
                    x = 0
                if len(self.sp_cmd_black) > 6 and i + x < 8:
                    print('      ', self.sp_cmd_black[len(self.sp_cmd_black) - 8 + i + x], end='  ')
                elif i <= len(self.sp_cmd_black) and i + x < 8:
                    print('      ', self.sp_cmd_black[i-1], end='  ')

            print()
        print('   a  b  c  d  e  f  g  h')

    def __repr__(self):
        res = ''
        for i in range(8):
            res += ''.join(map(str, self.board[i])) + '\n'
        return res


clear_screen()
b = Board()
b.show()


# m = b.get_moves(3, 2)
# b.move([3, 2], m[0])

dict_move = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}
sp = ['1', '2', '3', '4', '5', '6', '7', '8']
num = 1
while num < 2:
    if b.currentMoveColor == Color.white:
        print('Ход белых:', end=' ')
    else:
        print('Ход черных:', end=' ')
    b.cmd = input()

    if len(b.cmd) == 4 and b.cmd[0] in dict_move and b.cmd[2] in dict_move and b.cmd[1] in sp and b.cmd[3] in sp:
        count = 0
        xy_who = []
        xy_where = []
        for i in b.cmd:
            count += 1
            if i in dict_move:
                i = dict_move[i]
                if count < 3:
                    xy_who.append(i)
                else:
                    xy_where.append(i)

            else:
                j = 8-int(i)
                if count < 3:
                    xy_who.append(j)
                else:
                    xy_where.append(j)

        # print(xy_who, xy_where)
        k = [xy_who, xy_where]
        # print(*k)

        if b.move(*k):
            clear_screen()
            b.show()

            for i in b.king_white:
                if i in b.fig_moves_black:
                    print('шах белым')
            for i in b.king_black:
                if i in b.fig_moves_white:
                    print('шах черным')

    else:
        if b.cmd == 'список':
            print('белые: ', *b.sp_cmd_white)
            print('черные:', *b.sp_cmd_black)
        else:
            print('Ошибка: попробуй еще раз')
# b.move([0, 2], [5, 7])


input()
