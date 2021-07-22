import sys

import pygame

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """General class for resource management and way the game works"""

    def __init__(self):
        """Initalization game and making resources"""
        pygame.init()
        self.settings = Settings()

        #Wielkość ekranu
        self.screen= pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obców!")


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #Kolor tła
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """"Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            
    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        #Oczekiwanie na naciśnięcie klawisza lub muszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        """Naciśnięcie przycisku"""    
        if event.key == pygame.K_RIGHT:
            #Przesunięcie statku w prawo
            self.ship.moving_right = True
                #Przesunięcie statku w lewo
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):   
        """Reakcja na zwolnienie przycisku"""     
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków"""
        if len (self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewdicznych na ekranie"""
        #Uaktualnienie położenia pocisków
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)        
            
    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        #Utworzenie obcego.
        alien = Alien(self)
        self.aliens.add(alien)


    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        #Odświeżenie ekranu w trakcie każdej iteracji pętli.
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        #Wyświetlenie ostatno zmodyfikowanego ekranu
        pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
