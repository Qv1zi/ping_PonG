from pygame import *
windows = display.set_mode((700, 500))
display.set_caption('Настольный теннис')
background = transform.scale(image.load('back.jpg'), (700, 500))
clock = time.Clock()
game = True
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        #self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += 10
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += 10

player1 = Player('wall.jpg',750,250)
player2 = Player('wall.jpg',0,250)
while game:
    windows.blit((background),(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()