import pygame as pg
import sys
import random
from pygame.locals import *

# --- Pelin globaalit vakiot ja muuttujat ---
# Värit
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Aloitusikkunalle
RED = (255, 0, 0)   # 'X':lle ja voittoviivalle
GREEN = (0, 255, 0) # 'O':lle
CYAN = (0, 255, 255)  # Tilan teksti

# Pelilaudan ja näytön mitat
BOARD_SIZE = 15  # Laudan koko NxN
WIDTH = 600      # Näytön leveys
HEIGHT = 600     # Näytön korkeus
CELL_SIZE = WIDTH // BOARD_SIZE  # Yhden ruudun koko (40 pikseliä)
STATUS_BAR_HEIGHT = 100
TOTAL_HEIGHT = HEIGHT + STATUS_BAR_HEIGHT

# Pelin tila
XO = 'x'  # Kumman pelaajan vuoro ('x' tai 'o')
WINNER = None  # Voittaja (None jos ei ole)
DRAW = False   # Tasapeli-tila (False jos ei ole)
BOARD = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]  # Pelilauta
GAME_MODE = None  # Pelimuoto: 'pvp' (kaksinpeli) tai 'pve' (konetta vastaan)

# --- Pygame-alustus ---
pg.init()
FPS = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, TOTAL_HEIGHT), 0, 32)
pg.display.set_caption("Five in a Row (Gomoku)")

# --- Piirtofunktiot ---
def draw_board():
    """Piirtää pelilaudan viivat."""
    screen.fill(WHITE)
    for i in range(1, BOARD_SIZE):
        # Pystysuorat viivat
        pg.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)
        # Vaakasuorat viivat
        pg.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)

def draw_status():
    """Näyttää pelin tilan (vuoro, voittaja, tasapeli) alapalkissa."""
    global WINNER, DRAW, XO
    if WINNER is None and not DRAW:
        message = XO.upper() + " vuoro"
    elif DRAW:
        message = "Tasapeli!"
    else:
        message = WINNER.upper() + " voitti!"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, CYAN)
    screen.fill(BLACK, (0, HEIGHT, WIDTH, STATUS_BAR_HEIGHT))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT + STATUS_BAR_HEIGHT / 2))
    screen.blit(text, text_rect)
    pg.display.update()

def draw_victory_screen():
    """Näyttää selkeän voitto- tai tasapeli-ilmoituksen overlayna."""
    global WINNER, DRAW
    overlay = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    overlay.fill((255, 255, 255, 200))  # Läpinäkyvä valkoinen (alpha 200)
    screen.blit(overlay, (0, 0))
    if DRAW:
        message = "Tasapeli!"
    else:
        message = f"{WINNER.upper()} Voitti!"
    font = pg.font.Font(None, 80)
    text = font.render(message, 1, BLACK)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))
    screen.blit(text, text_rect)
    font = pg.font.Font(None, 40)
    instruction = font.render("Paina R jatkaaksesi, Q lopettaaksesi", 1, BLACK)
    instruction_rect = instruction.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(instruction, instruction_rect)
    pg.display.update()

def draw_xo(row, col):
    """Piirtää 'X' tai 'O' pelilautaan annettuun (0-indeksoituun) sijaintiin."""
    global BOARD, XO
    if BOARD[row][col] is not None:
        return
    posx = col * CELL_SIZE + CELL_SIZE / 2
    posy = row * CELL_SIZE + CELL_SIZE / 2
    margin = CELL_SIZE * 0.1
    BOARD[row][col] = XO
    if XO == 'x':
        pg.draw.line(screen, RED, (posx - CELL_SIZE / 2 + margin, posy - CELL_SIZE / 2 + margin),
                     (posx + CELL_SIZE / 2 - margin, posy + CELL_SIZE / 2 - margin), 3)
        pg.draw.line(screen, RED, (posx + CELL_SIZE / 2 - margin, posy - CELL_SIZE / 2 + margin),
                     (posx - CELL_SIZE / 2 + margin, posy + CELL_SIZE / 2 - margin), 3)
        XO = 'o'
    else:
        pg.draw.circle(screen, GREEN, (posx, posy), CELL_SIZE / 2 - 5, 3)
        XO = 'x'
    pg.display.update()

# --- Pelilogiikka ---
def is_winning_move(player, row, col):
    """Tarkistaa, johtaako siirto (row, col) pelaajan 'player' voittoon."""
    global BOARD
    BOARD[row][col] = player
    # Tarkista vaakasuorat
    for c in range(max(0, col - 4), min(BOARD_SIZE - 4, col + 1)):
        if (BOARD[row][c] == player and
            BOARD[row][c] == BOARD[row][c+1] == BOARD[row][c+2] == BOARD[row][c+3] == BOARD[row][c+4]):
            BOARD[row][col] = None
            return True
    # Tarkista pystysuorat
    for r in range(max(0, row - 4), min(BOARD_SIZE - 4, row + 1)):
        if (BOARD[r][col] == player and
            BOARD[r][col] == BOARD[r+1][col] == BOARD[r+2][col] == BOARD[r+3][col] == BOARD[r+4][col]):
            BOARD[row][col] = None
            return True
    # Tarkista diagonaalit (oikealle alas)
    for r, c in [(row - i, col - i) for i in range(-4, 1) if 0 <= row - i < BOARD_SIZE - 4 and 0 <= col - i < BOARD_SIZE - 4]:
        if (BOARD[r][c] == player and
            BOARD[r][c] == BOARD[r+1][c+1] == BOARD[r+2][c+2] == BOARD[r+3][c+3] == BOARD[r+4][c+4]):
            BOARD[row][col] = None
            return True
    # Tarkista diagonaalit (vasemmalle alas)
    for r, c in [(row - i, col + i) for i in range(-4, 1) if 0 <= row - i < BOARD_SIZE - 4 and 4 <= col + i < BOARD_SIZE]:
        if (BOARD[r][c] == player and
            BOARD[r][c] == BOARD[r+1][c-1] == BOARD[r+2][c-2] == BOARD[r+3][c-3] == BOARD[r+4][c-4]):
            BOARD[row][col] = None
            return True
    BOARD[row][col] = None
    return False

def check_win():
    """Tarkistaa, onko viisi merkkiä peräkkäin (vaaka, pysty, diagonaali)."""
    global BOARD, WINNER, DRAW
    # Tarkista vaakasuorat
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE - 4):
            if (BOARD[row][col] is not None and
                BOARD[row][col] == BOARD[row][col+1] == BOARD[row][col+2] == BOARD[row][col+3] == BOARD[row][col+4]):
                WINNER = BOARD[row][col]
                start_x = col * CELL_SIZE + CELL_SIZE / 2
                start_y = row * CELL_SIZE + CELL_SIZE / 2
                end_x = (col + 4) * CELL_SIZE + CELL_SIZE / 2
                end_y = row * CELL_SIZE + CELL_SIZE / 2
                pg.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 6)
                draw_victory_screen()
                return
    # Tarkista pystysuorat
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE - 4):
            if (BOARD[row][col] is not None and
                BOARD[row][col] == BOARD[row+1][col] == BOARD[row+2][col] == BOARD[row+3][col] == BOARD[row+4][col]):
                WINNER = BOARD[row][col]
                start_x = col * CELL_SIZE + CELL_SIZE / 2
                start_y = row * CELL_SIZE + CELL_SIZE / 2
                end_x = col * CELL_SIZE + CELL_SIZE / 2
                end_y = (row + 4) * CELL_SIZE + CELL_SIZE / 2
                pg.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 6)
                draw_victory_screen()
                return
    # Tarkista diagonaalit (oikealle alas)
    for row in range(BOARD_SIZE - 4):
        for col in range(BOARD_SIZE - 4):
            if (BOARD[row][col] is not None and
                BOARD[row][col] == BOARD[row+1][col+1] == BOARD[row+2][col+2] == BOARD[row+3][col+3] == BOARD[row+4][col+4]):
                WINNER = BOARD[row][col]
                start_x = col * CELL_SIZE + CELL_SIZE / 2
                start_y = row * CELL_SIZE + CELL_SIZE / 2
                end_x = (col + 4) * CELL_SIZE + CELL_SIZE / 2
                end_y = (row + 4) * CELL_SIZE + CELL_SIZE / 2
                pg.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 6)
                draw_victory_screen()
                return
    # Tarkista diagonaalit (vasemmalle alas)
    for row in range(BOARD_SIZE - 4):
        for col in range(4, BOARD_SIZE):
            if (BOARD[row][col] is not None and
                BOARD[row][col] == BOARD[row+1][col-1] == BOARD[row+2][col-2] == BOARD[row+3][col-3] == BOARD[row+4][col-4]):
                WINNER = BOARD[row][col]
                start_x = col * CELL_SIZE + CELL_SIZE / 2
                start_y = row * CELL_SIZE + CELL_SIZE / 2
                end_x = (col - 4) * CELL_SIZE + CELL_SIZE / 2
                end_y = (row + 4) * CELL_SIZE + CELL_SIZE / 2
                pg.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 6)
                draw_victory_screen()
                return
    # Tarkista tasapeli
    if all(cell is not None for row in BOARD for cell in row) and WINNER is None:
        DRAW = True
        draw_victory_screen()

def user_click():
    """Käsittelee käyttäjän hiiren klikkauksen."""
    x, y = pg.mouse.get_pos()
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and BOARD[row][col] is None:
        draw_xo(row, col)
        check_win()
        return True
    return False

# --- AI (Minimax) -ominaisuudet ---
def get_empty_cells():
    """Palauttaa listan tyhjien ruutujen koordinaateista."""
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if BOARD[r][c] is None]

def evaluate_board_heuristic():
    """Parannettu heuristinen arviointi koneen ('o') näkökulmasta."""
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vaaka, pysty, diag (alas-oik), diag (alas-vas)
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if BOARD[r][c] is None:
                continue
            player = BOARD[r][c]
            for dr, dc in directions:
                line = []
                for i in range(5):
                    nr, nc = r + i * dr, c + i * dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                        line.append(BOARD[nr][nc])
                    else:
                        line.append('border')
                if len(line) == 5:
                    if line.count('o') == 5:
                        return 100000
                    if line.count('x') == 5:
                        return -100000
                    if line.count('o') == 4 and line.count(None) == 1:
                        score += 1000
                    if line.count('x') == 4 and line.count(None) == 1:
                        score -= 1000
                    if line.count('o') == 3 and line.count(None) == 2:
                        score += 100
                    if line.count('x') == 3 and line.count(None) == 2:
                        score -= 100
                    if line.count('o') == 2 and line.count(None) == 3:
                        score += 10
                    if line.count('x') == 2 and line.count(None) == 3:
                        score -= 10
    return score

def minimax(depth, is_maximizing, alpha, beta):
    """Minimax-algoritmi alpha-beta-karsinnalla."""
    score = evaluate_board_heuristic()
    if score is not None and abs(score) >= 100000:
        return score
    if depth == 0 or not get_empty_cells():
        return score if score is not None else 0
    if is_maximizing:
        best_score = -float('inf')
        for r, c in get_empty_cells():
            BOARD[r][c] = 'o'
            current_score = minimax(depth - 1, False, alpha, beta)
            BOARD[r][c] = None
            best_score = max(best_score, current_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for r, c in get_empty_cells():
            BOARD[r][c] = 'x'
            current_score = minimax(depth - 1, True, alpha, beta)
            BOARD[r][c] = None
            best_score = min(best_score, current_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def computer_move():
    """Kone valitsee parhaan siirron minimax-algoritmilla."""
    global BOARD, XO
    # Tarkista voittava siirto koneelle
    for r, c in get_empty_cells():
        if is_winning_move('o', r, c):
            draw_xo(r, c)
            check_win()
            return
    # Tarkista estävä siirto (pelaajan voitto)
    for r, c in get_empty_cells():
        if is_winning_move('x', r, c):
            draw_xo(r, c)
            check_win()
            return
    # Käytä minimaxia strategiseen siirtoon
    best_score = -float('inf')
    best_move = None
    possible_moves = get_empty_cells()
    possible_moves.sort(key=lambda p: (abs(p[0] - BOARD_SIZE/2) + abs(p[1] - BOARD_SIZE/2)))
    for r, c in possible_moves:
        BOARD[r][c] = 'o'
        score = minimax(2, False, -float('inf'), float('inf'))
        BOARD[r][c] = None
        if score > best_score:
            best_score = score
            best_move = (r, c)
    if best_move:
        row, col = best_move
        draw_xo(row, col)
        check_win()
    else:
        available = get_empty_cells()
        if available:
            row, col = random.choice(available)
            draw_xo(row, col)
            check_win()
    draw_status()

# --- Pelin ohjausfunktiot ---
def reset_game():
    """Käynnistää pelin uudelleen alustamalla globaalit muuttujat."""
    global BOARD, WINNER, XO, DRAW, GAME_MODE
    XO = 'x'
    DRAW = False
    WINNER = None
    BOARD = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    GAME_MODE = None
    show_menu()

def show_menu():
    """Näyttää pelimuodon valintavalikon."""
    global GAME_MODE
    screen.fill(BLUE)
    font = pg.font.Font(None, 50)
    text1 = font.render("1: Kaksinpeli (PVP)", 1, WHITE)
    text2 = font.render("2: Konetta vastaan (PVE)", 1, WHITE)
    text1_rect = text1.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))
    text2_rect = text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    pg.display.update()
    while GAME_MODE is None:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    GAME_MODE = 'pvp'
                elif event.key == K_2:
                    GAME_MODE = 'pve'
        CLOCK.tick(FPS)
    game_initiating_window()

def game_initiating_window():
    """Alustaa pelinäkymän (piirtää laudan ja tilan)."""
    draw_board()
    draw_status()

# --- Pääsilmukka ---
show_menu()
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and GAME_MODE is not None and not (WINNER or DRAW):
            if GAME_MODE == 'pvp' or (GAME_MODE == 'pve' and XO == 'x'):
                user_click()
        elif event.type == KEYDOWN:
            if event.key == K_r:
                reset_game()
            elif event.key == K_q:
                pg.quit()
                sys.exit()
    if GAME_MODE == 'pve' and XO == 'o' and not (WINNER or DRAW):
        computer_move()
    draw_status()
    CLOCK.tick(FPS)