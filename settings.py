class Settings: 
    """Klasa przeznaczona do przechowywania ustawień gry"""
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        #Ustawienia ekranu:
        self.screen_width = 1000
        self.screen_height = 640
        self.bg_color = (230,230,230)

        #Ustawienia dotyczące pocisku
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #Ustawienie dotyczzące statku
        self.ship_speed = 0.5