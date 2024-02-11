import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player class
class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 1
        self.jump_power = -15
        self.health = 100
        self.lives = 3

    def update(self):
        self.speed_y += self.gravity
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check for collision with ground
        if self.rect.bottom > HEIGHT - 50:
            self.speed_y = 0
            self.rect.bottom = HEIGHT - 50

        # Check for collision with enemy
        hits = pygame.sprite.spritecollide(self, enemies, False)
        for hit in hits:
            self.health -= 10
            if self.health <= 0:
                self.lives -= 1
                self.rect.center = (WIDTH / 2, HEIGHT - 50)
                self.health = 100
                if self.lives <= 0:
                    self.kill()

    def jump(self):
        self.speed_y = self.jump_power

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(0, HEIGHT - 50)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y = -self.speed_y

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

        # Check for collision with enemy
        hits = pygame.sprite.spritecollide(self, enemies, True)
        for hit in hits:
            score += 10

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame