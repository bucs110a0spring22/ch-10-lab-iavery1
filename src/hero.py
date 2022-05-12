import pygame
import random

#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have initialized these values
        #and uses them to update the screen
      #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 3
    def heal(self, amount):
      self.health += 1

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def fight(self, opponent):
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
import pygame
import random

class Food(pygame.sprite.Sprite):
  def __init__(self, x, y, img_file):
    """
    Adds food for character to consume, restores health
    """
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    