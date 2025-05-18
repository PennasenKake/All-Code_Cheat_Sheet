# hangman.py - Hirsipuu-peli Pythonilla ja Pygamella

import pygame
import sys
import random

# Käynnistetään Pygame
pygame.init()

# Asetetaan pelin kellotusnopeus (FPS)
clock = pygame.time.Clock()

# Määritellään peliruudun mitat
width = 800
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

# Värit (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pelin tilamuuttujat
game_over = False

# Kirjainnappien asettelun parametrit
row = 2        # Rivejä 2
col = 13       # Sarakkeita 13
gap = 20       # Väli nappien välillä
size = 40      # Nappien koko (leveys/korkeus)
boxes = []     # Lista napeille

# Luodaan kirjainnappien sijainnit ruudukkoon
for r in range(row):
    for c in range(col):
        x = ((c * gap) + gap) + (size * c)
        y = ((r * gap) + gap) + (size * r) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

# Kirjainnappien luonti (A–Z)
buttons = []
A = 65  # ASCII-koodi kirjaimelle A
for ind, box in enumerate(boxes):
    letter = chr(A + ind)  # Muunnetaan ASCII-koodi kirjaimeksi
    button = [box, letter]
    buttons.append(button)

# Fontit
font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

# Piirretään kirjainnappulat ruudulle
def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, BLACK)
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, BLACK, box, 2)

# Näytetään arvattava sana (kirjaimet tai _)
def display_guess():
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f"{letter} "
        else:
            display_text += "_ "
    text = letter_font.render(display_text, True, BLACK)
    screen.blit(text, (400 - text.get_width() // 2, 200))

# Piirretään hirsipuu ja sen osat virheiden perusteella
def draw_hangman(status):
    # Hirsipuun rakenne
    pygame.draw.line(screen, BLACK, (150, 300), (250, 300), 5)  # Alusta
    pygame.draw.line(screen, BLACK, (200, 300), (200, 100), 5)  # Pystypalkki
    pygame.draw.line(screen, BLACK, (200, 100), (250, 100), 5)  # Ylätanko
    pygame.draw.line(screen, BLACK, (250, 100), (250, 120), 5)  # Köysi

    # Piirretään hirsipuun osat tilanteen mukaan
    if status >= 1:  # Pää
        pygame.draw.circle(screen, BLACK, (250, 140), 20, 2)
    if status >= 2:  # Vartalo
        pygame.draw.line(screen, BLACK, (250, 160), (250, 220), 2)
    if status >= 3:  # Vasen käsi
        pygame.draw.line(screen, BLACK, (250, 170), (230, 200), 2)
    if status >= 4:  # Oikea käsi
        pygame.draw.line(screen, BLACK, (250, 170), (270, 200), 2)
    if status >= 5:  # Vasen jalka
        pygame.draw.line(screen, BLACK, (250, 220), (230, 260), 2)
    if status >= 6:  # Oikea jalka
        pygame.draw.line(screen, BLACK, (250, 220), (270, 260), 2)

# Peliin liittyvät muuttujat
hangman_status = 0
words = [ 'KOIRA', 'KISSA', 'AUTO', 'TALO', 'PUU', 'JÄRVI', 'SUOMI', 'KESÄ', 'TALVI', 'KEVÄT',
    'SYKSY', 'LUMI', 'SATAA', 'AURINKO', 'KUUKAUSI', 'VIIKKO', 'PÄIVÄ', 'YÖ', 'ILTA', 'AAMU',
    'RUOKA', 'JUOMA', 'LEIPÄ', 'MAITO', 'KAHVI', 'TEE', 'VESI', 'MEHU', 'OMENA', 'BANAANI',
    'APPELSIINI', 'MANSIKKA', 'MUSTIKKA', 'VADELMA', 'PERUNA', 'PORKKANA', 'SIPULI', 'KURKKU',
    'TOMAATTI', 'JUUSTO', 'LIHA', 'KALA', 'KANANMUNA', 'SOKERI', 'SUOLA', 'PIPPURI', 'VOI',
    'ÖLJY', 'ETIKKA', 'JÄÄTELÖ', 'KAKKU', 'SUKLAA', 'KARKKI', 'LEIVÄNTUOTANTO', 'KIRJA',
    'SANOMA', 'LEHTI', 'UUTISET', 'RADIO', 'TELEVISIO', 'ELOKUVA', 'MUSIIKKI', 'LAULU',
    'SOITIN', 'KITARA', 'PIANO', 'RUMPU', 'VIULU', 'SÄVEL', 'RITMI', 'TAHTI', 'KONSERTTI',
    'TEATTERI', 'NÄYTELMÄ', 'ROOLI', 'NÄYTTELIJÄ', 'OHJAAJA', 'ELOKUVATEATTERI', 'KIRJASTO',
    'KOULU', 'OPETTAJA', 'OPISKELIJA', 'LUOKKA', 'KIRJA', 'VIHKO', 'KYNÄ', 'KUMI', 'VIIVOITIN',
    'TIETOKONE', 'NÄYTTÖ', 'NÄPPÄIMISTÖ', 'HIIRI', 'TULOSTIN', 'SKANNERI', 'INTERNET',
    'SÄHKÖPOSTI', 'SIVUSTO', 'SELAAJA', 'HAKU', 'LINKKI', 'TIEDOSTO', 'KANSIO', 'OHJELMA',
    'SOVELLUS', 'PELI', 'KAMERA', 'KUVA', 'VIDEO', 'ÄÄNI', 'MIKROFONI', 'KAIUTIN', 'KUULOKE',
    'PUHELIN', 'MATKAPUHELIN', 'ÄLYPUHELIN', 'TABLETTI', 'KELLO', 'HERÄTYSKELLO', 'KALENTERI',
    'SÄÄ', 'LÄMPÖTILA', 'TUULI', 'SATEENKAARI', 'PILVI', 'UKKONEN', 'SALAMA', 'MYRSKY',
    'LUMIMYRSKY', 'RAESADE', 'SUMU', 'AURINGONNOUSU', 'AURINGONLASKU', 'PIMEYS', 'VALO',
    'VARJO', 'HEIJASTUS', 'PEILI', 'IKKUNA', 'OVI', 'SEINÄ', 'KATTO', 'LATTI', 'PORTAAT',
    'HISSI', 'PARVEKE', 'PIHA', 'PUUTARHA', 'KUKKA', 'PENSA', 'PUISTO', 'METSA', 'POLKU',
    'SILTA', 'JOKI', 'MERI', 'SAARI', 'NIEMI', 'LAHTI', 'RANTA', 'HIEKKA', 'KALLIO', 'VUORI',
    'KUKKULA', 'LAKKA', 'TUNTURI', 'LUMI', 'JÄÄ', 'VESIPUTOUS', 'LAMPI', 'SUIHKU', 'KAIVO',
    'VESIHANA', 'PESUALLAS', 'KYLPYAMME', 'SAUNA', 'KIUAS', 'LAUDE', 'LÖYLY', 'PESUSIENI',
    'SHAMPOO', 'SAIPPUA', 'PYJAMA', 'YÖPAITA', 'ALUSVAATTEET', 'SUKAT', 'KENGÄT', 'TAKKI',
    'PAITA', 'HOUSUT', 'HAME', 'MEKKO', 'PUSERO', 'NEULE', 'VILLATAKKI', 'TAKKI', 'HUPPARI',
    'TAKAPUOLI', 'KÄSI', 'JALKA', 'PÄÄ', 'HIUKSET', 'SILMÄ', 'KORVA', 'NENÄ', 'SUU', 'HAMPAAT',
    'KIELI', 'LEUKA', 'KAULA', 'OLKAPÄÄ', 'KYYNÄRPÄÄ', 'RANNE', 'SORMI', 'KYNNET']
word = random.choice(words)  # Arvotaan sana
guessed = []  # Lista arvatuista kirjaimista

# Pelin otsikko
title = "Hangman"
title_text = game_font.render(title, True, BLACK)
title_rect = title_text.get_rect(center=(width // 2, title_text.get_height() // 2 + 10))

# Pelin pääsilmukka
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Jos klikataan hiirellä ja peli ei ole ohi
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            click_pos = event.pos
            buttons_to_remove = []
            for button, letter in buttons:
                if button.collidepoint(click_pos):  # Tarkista osuiko nappiin
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in word:
                            hangman_status += 1  # Väärä arvaus
                    buttons_to_remove.append([button, letter])
            for btn in buttons_to_remove:
                buttons.remove(btn)  # Poista käytetty kirjain

    # Piirretään peliin liittyvät elementit
    draw_hangman(hangman_status)
    draw_buttons(buttons)
    display_guess()
    screen.blit(title_text, title_rect)

    # Voitto- tai häviötarkistus
    won = all(letter in guessed for letter in word)
    lost = hangman_status >= 6

    if won or lost:
        game_over = True
        game_text = "VOITIT!" if won else "HÄVISIT!"
        screen.fill(WHITE)
        text = game_font.render(game_text, True, BLACK)
        text_rect = text.get_rect(center=(width // 2, height // 2 - 40))
        screen.blit(text, text_rect)

        # Uudelleenkäynnistyspainike
        restart_text = font.render("Klikkaa aloittaaksesi uudelleen", True, (0, 0, 255))
        restart_rect = restart_text.get_rect(center=(width // 2, height // 2 + 20))
        screen.blit(restart_text, restart_rect)

        pygame.display.update()

        # Odotetaan pelaajaa klikkaamaan uudelleenkäynnistystä
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = event.pos
                    if restart_rect.collidepoint(click_pos):
                        # Palautetaan pelin alkuasetukset
                        game_over = False
                        hangman_status = 0
                        word = random.choice(words)
                        guessed = []
                        buttons = []
                        for ind, box in enumerate(boxes):
                            letter = chr(A + ind)
                            button = [box, letter]
                            buttons.append(button)
                        waiting_for_restart = False

    # Päivitä näyttö ja rajoita ruudunpäivitystä
    clock.tick(50)
    pygame.display.update()

# Sulje peli
pygame.quit()
sys.exit()
