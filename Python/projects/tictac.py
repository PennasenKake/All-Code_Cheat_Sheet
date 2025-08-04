import pygame as pg
import sys
import time
import os
from pygame.locals import *

# Pelin globaalit muuttujat
XO = 'x'  # Kumman pelaajan vuoro ('x' tai 'o')
winner = None  # Voittaja (None jos ei ole)
draw = False  # Tasapeli-tila (False jos ei ole)
width = 400  # Näytön leveys
height = 400  # Näytön korkeus
white = (255, 255, 255)  # Valkoinen väri
line_color = (0, 0, 0)  # Musta väri
board = [[None]*3, [None]*3, [None]*3]  # 3x3 pelilauta

# Pygame-alustus
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("My Tic Tac Toe")

# Kuvat
base_path = os.path.dirname(__file__)  # Hakee scriptin hakemiston
try:
    initiating_window = pg.image.load(os.path.join(base_path, "modified_cover.png"))
    x_img = pg.image.load(os.path.join(base_path, "x_modified.png"))
    o_img = pg.image.load(os.path.join(base_path, "o_modified.png"))
except FileNotFoundError as e:
    print(f"Error: {e}")
    pg.quit()
    sys.exit()

# Skaalataan kuvat
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))

def draw_board():
    """Piirtää pelilaudan viivat"""
    # Pystysuorat viivat
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
    # Vaakasuorat viivat
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)

def game_initiating_window():
    """Näyttää aloitusikkunan ja alustaa pelilaudan"""
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)
    draw_board()  # Piirretään pelilauta
    draw_status()  # Näytetään pelin tila
    pg.display.update()

def draw_status():
    """Näyttää pelin tilan (vuoro, voittaja, tasapeli)"""
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game Draw!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (1, 255, 255))
    screen.fill((0, 0, 0), (0, height, width, 100))  # Tilanäytön tausta
    text_rect = text.get_rect(center=(width/2, height + 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    """Tarkistaa, onko peli voitettu tai tasapeli"""
    global board, winner, draw

    # Tarkista rivit
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6),
                         (width, (row + 1)*height/3 - height/6), 4)
            break

    # Tarkista sarakkeet
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1)*width/3 - width/6, 0),
                         ((col + 1)*width/3 - width/6, height), 4)
            break

    # Tarkista diagonaalit
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    # Tarkista tasapeli
    if all([all(row) for row in board]) and winner is None:
        draw = True
    draw_status()

def drawXO(row, col):
    """Piirtää 'X' tai 'O' pelilautaan"""
    global board, XO
    # Määritä koordinaatit (korjattu x ja y oikein)
    posy = (row - 1) * height / 3 + 30  # Rivin y-koordinaatti
    posx = (col - 1) * width / 3 + 30   # Sarakkeen x-koordinaatti

    board[row-1][col-1] = XO
    if XO == 'x':
        screen.blit(x_img, (posx, posy))
        XO = 'o'
    else:
        screen.blit(o_img, (posx, posy))
        XO = 'x'
    pg.display.update()

def user_click():
    """Käsittelee käyttäjän hiiren klikkauksen"""
    x, y = pg.mouse.get_pos()

    # Määritä sarake
    if x < width / 3:
        col = 1
    elif x < width / 3 * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None

    # Määritä rivi
    if y < height / 3:
        row = 1
    elif y < height / 3 * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None

    if row and col and board[row-1][col-1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    """Käynnistää pelin uudelleen"""
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
    game_initiating_window()

# Käynnistä peli
game_initiating_window()

# Pääsilmukka
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)