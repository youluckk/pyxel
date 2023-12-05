import pyxel

class Player:
    def __init__(self, window_size):
        self.size = 8
        self.window_size = window_size
        self.x = 512  # Commence au milieu de la tilemap totale
        self.y = 512  # Commence au milieu de la tilemap totale

    def update(self):
        speed = 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(0, self.y - speed)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(1024 - self.window_size, self.y + speed)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(0, self.x - speed)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(1024 - self.window_size, self.x + speed)

    def draw(self):
        pyxel.blt(self.window_size // 2, self.window_size // 2, 0, 24, 0, self.size, self.size, 1)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 8

    def update(self, player):
        if self.x < player.x:
            self.x += 1
        elif self.x > player.x:
            self.x -= 1

        if self.y < player.y:
            self.y += 1
        elif self.y > player.y:
            self.y -= 1

    def draw(self, scroll_x, scroll_y):
        pyxel.blt(self.x - scroll_x, self.y - scroll_y, 0, 0, 0, self.size, self.size, 1)

class Game:
    def __init__(self):
        self.window_size = 80  # Taille de la fenêtre de jeu
        pyxel.init(80, 80)
        self.player = Player(self.window_size)
        self.enemies = [Enemy(120, 120) for i in range(5)]

        # Liste de tilemaps
        self.tilemaps = [0, 1, 2]  #numéros de tilemaps créés
        self.current_tilemap = self.tilemaps[0]

        pyxel.load("res.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

        # Vérifie si le joueur atteint les bords de la tilemap actuelle
        if self.player.x < self.window_size // 2:
            self.player.x = self.window_size // 2
        elif self.player.x > 1024 - self.window_size // 2:
            self.player.x = 1024 - self.window_size // 2

        if self.player.y < self.window_size // 2:
            self.player.y = self.window_size // 2
        elif self.player.y > 1024 - self.window_size // 2:
            self.player.y = 1024 - self.window_size // 2

        for enemy in self.enemies:
            enemy.update(self.player)

    def draw(self):             
        pyxel.cls(0)

        # Dessiner la tilemap actuelle
        pyxel.bltm(0, 0, self.current_tilemap, self.player.x - self.window_size // 2, self.player.y - self.window_size // 2, self.window_size, self.window_size)

        self.player.draw()

        for enemy in self.enemies:
            enemy.draw(self.player.x - self.window_size // 2, self.player.y - self.window_size // 2)

Game() 