import pygame as pg
import sys
import time
import random
from pygame.locals import *

# Pelin globaalit muuttujat
XO = 'x'  # Kumman pelaajan vuoro ('x' tai 'o')
winner = None  # Voittaja (None jos ei ole)
draw = False  # Tasapeli-tila (False jos ei ole)
width = 400  # Näytön leveys
height = 400  # Näytön korkeus
white = (255, 255, 255)  # Valkoinen väri
black = (0, 0, 0)  # Musta väri
blue = (0, 0, 255)  # Sininen väri aloitusikkunalle
red = (255, 0, 0)  # Punainen väri 'X':lle
green = (0, 255, 0)  # Vihreä väri 'O':lle
board = [[None]*3, [None]*3, [None]*3]  # 3x3 pelilauta
game_mode = None  # Pelimuoto: 'pvp' (kaksinpeli) tai 'pve' (konetta vastaan)

# Pygame-alustus
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("My Tic Tac Toe")

def draw_board():
    """Piirtää pelilaudan viivat"""
    pg.draw.line(screen, black, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, black, (width/3*2, 0), (width/3*2, height), 7)
    pg.draw.line(screen, black, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, black, (0, height/3*2), (width, height/3*2), 7)

def game_initiating_window():
    """Näyttää aloitusikkunan ja alustaa pelilaudan"""
    screen.fill(white)
    draw_board()
    draw_status()
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
    screen.fill(black, (0, height, width, 100))
    text_rect = text.get_rect(center=(width/2, height + 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    """Tarkistaa, onko peli voitettu tai tasapeli"""
    global board, winner, draw

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6),
                         (width, (row + 1)*height/3 - height/6), 4)
            break

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1)*width/3 - width/6, 0),
                         ((col + 1)*width/3 - width/6, height), 4)
            break

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if all([all(row) for row in board]) and winner is None:
        draw = True
    draw_status()

def drawXO(row, col):
    """Piirtää 'X' tai 'O' pelilautaan"""
    global board, XO
    posy = (row - 1) * height / 3 + 30
    posx = (col - 1) * width / 3 + 30
    cell_width = width / 3
    cell_height = height / 3

    board[row-1][col-1] = XO
    if XO == 'x':
        pg.draw.line(screen, red, (posx, posy), (posx + cell_width - 60, posy + cell_height - 60), 10)
        pg.draw.line(screen, red, (posx + cell_width - 60, posy), (posx, posy + cell_height - 60), 10)
        XO = 'o'
    else:
        pg.draw.circle(screen, green, (posx + cell_width/2 - 30, posy + cell_height/2 - 30), 50, 10)
        XO = 'x'
    pg.display.update()

def user_click():
    """Käsittelee käyttäjän hiiren klikkauksen"""
    x, y = pg.mouse.get_pos()
    if x < width / 3:
        col = 1
    elif x < width / 3 * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
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
        return True
    return False

def evaluate_board():
    """Arvioi pelilaudan tilan: +10 jos kone voittaa, -10 jos pelaaja voittaa, 0 tasapelille"""
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return 10 if board[row][0] == 'o' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return 10 if board[0][col] == 'o' else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return 10 if board[0][0] == 'o' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return 10 if board[0][2] == 'o' else -10
    if all(cell is not None for row in board for cell in row):
        return 0
    return None

def minimax(is_maximizing):
    """Minimax-algoritmi, joka palauttaa parhaan siirron pistemäärän"""
    score = evaluate_board()
    if score is not None:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] is None:
                    board[r][c] = 'o'
                    score = minimax(False)
                    board[r][c] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] is None:
                    board[r][c] = 'x'
                    score = minimax(True)
                    board[r][c] = None
                    best_score = min(best_score, score)
        return best_score

def computer_move():
    """Kone valitsee parhaan siirron minimax-algoritmilla"""
    global board, XO
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] is None:
                board[r][c] = 'o'
                score = minimax(False)
                board[r][c] = None
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    if best_move:
        row, col = best_move
        drawXO(row + 1, col + 1)
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

def show_menu():
    """Näyttää pelimuodon valintavalikon"""
    global game_mode
    screen.fill(blue)
    font = pg.font.Font(None, 50)
    text1 = font.render("1: Kaksinpeli", 1, white)
    text2 = font.render("2: Konetta vastaan", 1, white)
    text1_rect = text1.get_rect(center=(width/2, height/2 - 30))
    text2_rect = text2.get_rect(center=(width/2, height/2 + 30))
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    pg.display.update()

    while game_mode is None:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    game_mode = 'pvp'
                elif event.key == K_2:
                    game_mode = 'pve'
    game_initiating_window()

# Näytä valikko
show_menu()

# Pääsilmukka
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and not (winner or draw):
            if game_mode == 'pvp' or (game_mode == 'pve' and XO == 'x'):
                if user_click() and game_mode == 'pve' and XO == 'o' and not (winner or draw):
                    computer_move()

    if game_mode == 'pve' and XO == 'o' and not (winner or draw):
        computer_move()

    if winner or draw:
        reset_game()

    pg.display.update()
    CLOCK.tick(fps)