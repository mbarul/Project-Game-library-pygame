import sys

import pygame

from ship import Ship
from settings import Settings


class AlienInvasion:
    """General class for resource management and way the game works"""

    def __init__(self):
        """Initalization game and making resources"""
        pygame.init()
        self.settings = Settings()

        #Wielkość ekranu
        self.screen= pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obców!")


        self.ship = Ship(self)
        #Kolor tła
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """"Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        #Oczekiwanie na naciśnięcie klawisza lub muszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        #Odświeżenie ekranu w trakcie każdej iteracji pętli.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        #Wyświetlenie ostatno zmodyfikowanego ekranu
        pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
