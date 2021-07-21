class Settings: 
    """Klasa przeznaczona do przechowywania ustawień gry"""
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        #Ustawienia ekranu:
        self.screen_width = 1000
        self.screen_height = 640
        self.bg_color = (230,230,230)

        #Ustawienie dotyczzące statku
        self.ship_speed = 0.5