class Settings: 
    """Klasa przeznaczona do przechowywania ustawień gry"""
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        #Ustawienia ekranu:
        self.screen_width = 1000
        self.screen_height = 640
        self.bg_color = (230,230,230)

        #Ustawienia dotyczące pocisku
        #self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #Ustawienie dotyczzące statku
        #self.ship_speed = 0.5
        self.ship_limit = 3

        #Ustawienia dotyczące obcego.
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 13

       

        #Zmiana szybkości gry
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        #Zmiana liczby puntków przyznawanych za zestrzelenie obcego.
        self.score_scale = 1.5
    
    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry"""
        self.ship_speed = 1.2
        self.bullet_speed = 2.5
        self.alien_speed = 0.6

        #Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 1

        #Punktacja 
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana ustawueń dotyczących szybkości i liczby przyznawanych punktów"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        