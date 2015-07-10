#!/usr/bin/env python
from Tkinter import *
from game import game
from game import persist
from tetromino import rectangle
from tetromino import point

class Application():
    WIDTH = 10
    HEIGHT = 22
    PIECE_SIZE = 30
    BG_CANVAS = '#00141A'
    BG_APP = '#001F27'
    FG_LABELS1 = '#2AA198'
    FG_LABELS2 = '#859900'
    FG_LINE = '#002B36'
    FG_LABELS3 = '#C44B16'
    FONT = 'Ubuntu'

    def __init__(self, root):
        self.textvarScore = StringVar()
        self.textvarScore.set('0')
        self.textvarBest = StringVar()
        self.textvarBest.set('0')
        self.game = game.Game(self.WIDTH, self.HEIGHT, self)
        self.window = root
        self.window.resizable(width=FALSE, height=FALSE)
        self.createMainWidgets()
        self.center()
        self.drawGrids()
        self.flasy = self.writeFlashyText('Press any key')

    def center(self):
        self.window.update_idletasks()
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        size = tuple(int(_) for _ in self.window.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.window.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def mainloop(self):
        self.window.mainloop()

    def createMainWidgets(self):
        frameL = Frame(self.window, bg = self.BG_APP, width=400, padx='20')
        labelNext = Label(frameL, text='Next', fg=self.FG_LABELS1, bg=self.BG_APP, font='''"%s" 24''' % self.FONT)
        labelNext.pack({'side':'top', 'fill':'x'})
        self.canvasNext = Canvas(frameL, bg=self.BG_CANVAS, highlightthickness=0, width=4*self.PIECE_SIZE, height = 4*self.PIECE_SIZE)
        self.canvasNext.pack({'side':'top'})
        labelHold = Label(frameL, text='Hold', fg=self.FG_LABELS1, bg=self.BG_APP, font='''"%s" 24''' % self.FONT)
        labelHold.pack({'side':'top', 'fill':'x'})
        self.canvasHold = Canvas(frameL, bg=self.BG_CANVAS, highlightthickness=0, width=4*self.PIECE_SIZE, height = 4*self.PIECE_SIZE)
        self.canvasHold.pack({'side':'top'})
        frameL.pack({'fill':'y', 'side':'left'})

        frameMain = Frame(self.window)
        self.canvas = Canvas(frameMain, bg=self.BG_CANVAS, highlightthickness = 0, width = self.WIDTH * self.PIECE_SIZE, height = self.HEIGHT * self.PIECE_SIZE)
        self.canvas.pack()
        frameMain.pack({'fill':'y', 'side':'left'})

        frameR = Frame(self.window, bg = self.BG_APP, width=200, padx='10')
        labelScore = Label(frameR, text='Your Score', fg=self.FG_LABELS1, bg=self.BG_APP, font='''"%s" 12''' % self.FONT)
        labelScore.pack({'side':'top','anchor':'w'})
        self.labelVScore = Label(frameR, textvariable=self.textvarScore, fg=self.FG_LABELS2, bg=self.BG_APP, font='''"%s" 24''' % self.FONT)
        self.labelVScore.pack({'side':'top', 'anchor':'w'})
        labelBest = Label(frameR, text='The Best Score', fg=self.FG_LABELS1, bg=self.BG_APP, font='''"%s" 12''' % self.FONT)
        labelBest.pack({'side':'top', 'anchor':'w'})
        self.labelVBest = Label(frameR, textvariable=self.textvarBest, fg=self.FG_LABELS2, bg=self.BG_APP, font='''"%s" 24''' % self.FONT)
        self.labelVBest.pack({'side':'top', 'anchor':'w'})
        frameR.pack({'fill':'y', 'side':'left'})
        root.bind('<Key>', self.keypress)

    def drawGrids(self):
        self.drawGridInCanvas(self.canvas, self.WIDTH, self.HEIGHT)
        self.drawGridInCanvas(self.canvasNext, 4, 4)
        self.drawGridInCanvas(self.canvasHold, 4, 4)

    def drawGridInCanvas(self, canvas, x, y):
        for i in range (0, x):
            l = canvas.create_line(
                i * self.PIECE_SIZE, 0,
                i * self.PIECE_SIZE, y * self.PIECE_SIZE,
                fill=self.FG_LINE
            )
        for i in range (0, y):
            l = canvas.create_line(
                0, i * self.PIECE_SIZE,
                x * self.PIECE_SIZE, i * self.PIECE_SIZE,
                fill=self.FG_LINE
            )

    def keypress(self, key):
        if not self.game.running :
            self.canvas.delete(self.flasy)
            self.game.start()
        if key.keysym == 'Escape':
            self.game.stop = 1
            return
        if key.keysym in ['Left','Right','Up','Down']:
            self.game.direction = key.keysym
            return

    def drawTetromino(self, canvas, tetromino, position):
        for i in tetromino.points:
            p = point.Point(i.x + position.x, i.y + position.y)
            r = rectangle.Rectangle(p, self.PIECE_SIZE, self.PIECE_SIZE)
            r.homothetie()
            im = canvas.create_rectangle(r.x0, r.y0, r.x1, r.y1, fill=tetromino.color)
            i.image = im

    def clearTetromino(self, canvas, tetromino):
        for i in tetromino.points:
            canvas.delete(i.image)

    def drawMatrice(self, matrice):
        self.clearMatrice()
        self.game.imageMatrice = []
        for i in range(1,matrice.n - 1):
            for j in range(1,matrice.m - 1):
                if matrice.get(i,j) != 1 : continue
                p = point.Point(j - 1, i)
                r = rectangle.Rectangle(p, self.PIECE_SIZE, self.PIECE_SIZE)
                r.homothetie()
                im = self.canvas.create_rectangle(r.x0, r.y0, r.x1, r.y1, fill=self.FG_LABELS1)
                self.game.imageMatrice.append(im)

    def clearMatrice(self):
        for i in self.game.imageMatrice:
            self.canvas.delete(i)

    def clearCanvas(self, canvas):
        canvas.delete(ALL)

    def writeFlashyText(self, string):
        return self.canvas.create_text(150, self.HEIGHT * self.PIECE_SIZE / 2, text=string, font='''"%s" 28''' % self.FONT, fill=self.FG_LABELS3)


root = Tk()
root.wm_title = 'Tetris'
app = Application(root)
app.mainloop()
