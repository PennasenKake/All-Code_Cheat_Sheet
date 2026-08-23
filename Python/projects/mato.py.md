<!-- tags: python -->

# mato.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/projects/mato.py)

```python
import pygame
import random
import sys

# Alustetaan Pygame
pygame.init()

# Värit
MUSTA     = (0, 0, 0)
VIHREÄ    = (0, 255, 0)
PUNAINEN  = (255, 50, 50)
VALKOINEN = (220, 220, 220)

# Ruudun mitat
LEVYYS = 600
KORKEUS = 500
Ruutukoko = 20

# Ruutu
naytto = pygame.display.set_mode((LEVYYS, KORKEUS))
pygame.display.set_caption("Mato - Grok edition 🐍")
kello = pygame.time.Clock()

# Fontti
fontti = pygame.font.SysFont("segoeuisymbol", 28)
pieni_fontti = pygame.font.SysFont("consolas", 18)

class MatoPeli:
    def __init__(self):
        self.reset()

    def reset(self):
        self.mato = [(LEVYYS//2, KORKEUS//2)]
        self.suunta = (Ruutukoko, 0)          # aluksi oikealle
        self.ruoka = self.uusi_ruoka()
        self.pisteet = 0
        self.pelin_loppuminen = False
        self.nopeus = 10                      # frames per second

    def uusi_ruoka(self):
        while True:
            x = random.randrange(0, LEVYYS, Ruutukoko)
            y = random.randrange(0, KORKEUS, Ruutukoko)
            if (x, y) not in self.mato:
                return (x, y)

    def liikuta(self):
        if self.pelin_loppuminen:
            return

        # Uusi pää
        px, py = self.mato[0]
        uusi_pa = (px + self.suunta[0], py + self.suunta[1])

        # Törmäykset
        if (uusi_pa[0] < 0 or uusi_pa[0] >= LEVYYS or
            uusi_pa[1] < 0 or uusi_pa[1] >= KORKEUS or
            uusi_pa in self.mato):
            self.pelin_loppuminen = True
            return

        # Lisätään uusi pää
        self.mato.insert(0, uusi_pa)

        # Syötiinkö ruokaa?
        if uusi_pa == self.ruoka:
            self.pisteet += 1
            self.ruoka = self.uusi_ruoka()
            # Nopeutuu vähän isomman madon myötä
            self.nopeus = 10 + self.pisteet // 3
        else:
            self.mato.pop()   # häntä pois jos ei syöty

    def piirra(self):
        naytto.fill(MUSTA)

        # Ruoka
        pygame.draw.rect(naytto, PUNAINEN,
                        (self.ruoka[0], self.ruoka[1], Ruutukoko, Ruutukoko))

        # Mato
        for i, osa in enumerate(self.mato):
            vari = VIHREÄ if i == 0 else (0, 200, 0)  # pää kirkkaampi
            pygame.draw.rect(naytto, vari,
                            (osa[0], osa[1], Ruutukoko, Ruutukoko))
            # pieni valkoinen reuna osiin
            pygame.draw.rect(naytto, VALKOINEN,
                            (osa[0], osa[1], Ruutukoko, Ruutukoko), 1)

        # Pisteet
        teksti = fontti.render(f"Pisteet: {self.pisteet}", True, VALKOINEN)
        naytto.blit(teksti, (15, 10))

        if self.pelin_loppuminen:
            game_over = fontti.render("GAME OVER – paina R aloittaaksesi", True, PUNAINEN)
            naytto.blit(game_over, (LEVYYS//2 - game_over.get_width()//2, KORKEUS//2 - 30))
            vinkki = pieni_fontti.render("(nuolinäppäimet tai WASD)", True, (140,140,140))
            naytto.blit(vinkki, (LEVYYS//2 - vinkki.get_width()//2, KORKEUS//2 + 20))

        pygame.display.flip()

    def kasittele_nappaimet(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if tapahtuma.type == pygame.KEYDOWN:
                if self.pelin_loppuminen:
                    if tapahtuma.key == pygame.K_r:
                        self.reset()
                    continue

                if tapahtuma.key in (pygame.K_UP, pygame.K_w) and self.suunta != (0, Ruutukoko):
                    self.suunta = (0, -Ruutukoko)
                elif tapahtuma.key in (pygame.K_DOWN, pygame.K_s) and self.suunta != (0, -Ruutukoko):
                    self.suunta = (0, Ruutukoko)
                elif tapahtuma.key in (pygame.K_LEFT, pygame.K_a) and self.suunta != (Ruutukoko, 0):
                    self.suunta = (-Ruutukoko, 0)
                elif tapahtuma.key in (pygame.K_RIGHT, pygame.K_d) and self.suunta != (-Ruutukoko, 0):
                    self.suunta = (Ruutukoko, 0)


def main():
    peli = MatoPeli()

    while True:
        peli.kasittele_nappaimet()
        peli.liikuta()
        peli.piirra()
        kello.tick(peli.nopeus)


if __name__ == "__main__":
    main()
```
