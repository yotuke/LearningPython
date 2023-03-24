import tkinter as tk

class Board:
    def __init__(self):
        self.color = 'black'
        self.board = [['empty' for _ in range(15)] for _ in range(15)]

    def play_move(self, row, col):
        if self.board[row][col] == 'empty':
            self.board[row][col] = self.color
            if self.color == 'black':
                self.color = 'white'
            else:
                self.color = 'black'

    def get_color(self, row, col):
        return self.board[row][col]

class Game:
    def __init__(self):
        self.board = Board()

    def play(self, row, col):
        self.board.play_move(row, col)
        self.update_board()

    def update_board(self):
        for row in range(15):
            for col in range(15):
                color = self.board.get_color(row, col)
                if color == 'empty':
                    color = 'gray'
                if color == 'black':
                    color = 'black'
                if color == 'white':
                    color = 'white'
                canvas.itemconfig(board[row][col], fill=color)

def create_board():
    for row in range(15):
        for col in range(15):
            x0, y0 = col * cell_size, row * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            board[row][col] = canvas.create_rectangle(x0, y0, x1, y1, fill='gray', tags='board')
            canvas.tag_bind(board[row][col], '<Button-1>', lambda event, row=row, col=col: game.play(row, col))

root = tk.Tk()
root.title('Five in a row')
cell_size = 40
canvas = tk.Canvas(root, width=cell_size*15, height=cell_size*15)
canvas.pack()
board = [[None for _ in range(15)] for _ in range(15)]
game = Game()
create_board()
root.mainloop()