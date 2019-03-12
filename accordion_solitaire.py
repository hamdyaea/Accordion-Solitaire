
# accordion solitaire
# rules of the game can be found here
# https://en.wikipedia.org/wiki/Accordion_(solitaire)

import tkinter as tk
import random


class Card:
    def __init__(self, name, value, suit, image_path, image):
        self.name = name
        self.value = value
        self.suit = suit
        self.image_path = image_path
        self.image = image


# create tkinter.grid root window
root = tk.Tk()
root.title('Accordion Solitaire')

bottom_frame = tk.Frame(root)
bottom_frame.grid(column=0, row=1)


# create and shuffle deck
def start():

    # create deck
    values = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    suits = ['H', 'C', 'D', 'S']
    deck = []

    for deck_suit in suits:
        for deck_value in values:
            deck.append(Card(None, deck_value, deck_suit, f'Cards\\{deck_value}{deck_suit}.png', None))

    # shuffle Deck
    matrix = []

    while True:
        if not deck:
            break
        matrix.append(deck.pop(random.randrange(len(deck))))

    build_matrix(matrix)


# build card matrix
def build_matrix(matrix):

    surface = tk.Frame(root, bg='lightgreen')
    surface.grid(column=0, row=0)

    row = 0
    for card in matrix:
        if matrix.index(card) != 0 and matrix.index(card) % 13 == 0:
            row += 1

        card.name = tk.Frame(surface, bg='lightgreen')
        card.name.grid(column=matrix.index(card) % 13, row=row, padx=3, pady=3)
        card.image = tk.PhotoImage(file=card.image_path)
        tk.Label(card.name, bg='lightgreen', image=card.image).grid(column=0, row=0, columnspan=2, padx=3, pady=3)

        button_col = 0
        button_sticky = 'e'
        for button in [1, 3]:

            tk.Button(card.name,
                      text='<'*button,
                      width=4,
                      command=lambda
                           go=button,
                           x_coor=matrix.index(card):
                      stack(go, x_coor, surface, matrix)) \
                .grid(column=button_col, row=1, padx=0.5, pady=0.5, sticky=button_sticky)

            button_col = 1
            button_sticky = 'w'


# 2 stacking buttons, directly to the left and jump over 2 to the left
def stack(go, x_coor, surface, matrix):

    if matrix[x_coor - go].suit == matrix[x_coor].suit \
            or matrix[x_coor - go].value == matrix[x_coor].value:
        if go == 1:
            del matrix[x_coor - go]
        if go == 3:
            pos_1, pos_2 = x_coor - 3, x_coor
            matrix[pos_2], matrix[pos_1] = matrix[pos_1], matrix[pos_2]
            del matrix[x_coor]
        surface.destroy()
        build_matrix(matrix)

    else:
        print('\a')


# main buttons
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(0, weight=0)

tk.Button(bottom_frame, width=8, text='Quit', command=root.destroy).grid(column=0, row=0, sticky='e')
tk.Button(bottom_frame, width=8, text='Restart', command=start).grid(column=1, row=0, sticky='e')

start()
root.mainloop()
