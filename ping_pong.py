from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_w, player_h, key_upmove, key_downmove):
        super().__init__(player_image, player_speed, player_x, player_y, player_w, player_h)
        self.key_upmove = key_upmove
        self.key_downmove = key_downmove
    def update(self):
        keys = key.get_pressed()
        if keys[self.key_upmove] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[self.key_downmove] and self.rect.y < 500-70:
            self.rect.y += self.speed
        

window = display.set_mode((700,500))
display.set_caption('Nothing')

player1 = Player('p_image.png', 1, 30, 250, 20, 50, K_w, K_s)
player2 = Player('p_image.png', 1, 650, 250, 20, 50, K_UP, K_DOWN)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if game != False:
        window.fill((0,0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()

    display.update()