import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Ariel", 30)

dice_size = (100, 100)
dice1_position = (200, 250)
dice2_position = (500, 250)

dice_img1 = pygame.image.load('dice-six-faces-one.png').convert_alpha()
dice_img1 = pygame.transform.scale(dice_img1, dice_size)
dice_img2 = pygame.image.load('dice-six-faces-two.png').convert_alpha()
dice_img2 = pygame.transform.scale(dice_img2, dice_size)
dice_img3 = pygame.image.load('dice-six-faces-three.png').convert_alpha()
dice_img3 = pygame.transform.scale(dice_img3, dice_size)
dice_img4 = pygame.image.load('dice-six-faces-four.png').convert_alpha()
dice_img4 = pygame.transform.scale(dice_img4, dice_size)
dice_img5 = pygame.image.load('dice-six-faces-five.png').convert_alpha()
dice_img5 = pygame.transform.scale(dice_img5, dice_size)
dice_img6 = pygame.image.load('dice-six-faces-six.png').convert_alpha()
dice_img6 = pygame.transform.scale(dice_img6, dice_size)

def type_text(text, font, text_col, x, y):
    img = font.render(str(text), True, text_col)
    screen.blit(img, (x, y))

def dice_roll():
    global dice1, dice2, dice_value
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_value = int(dice1 + dice2)
    print(dice1, dice2, dice_value)
    return dice_value

run = True
while run:

    screen.fill((0, 0, 0))
    
    type_text("Dice rolling", text_font, (255, 255, 255), 350, 150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                dice_roll()
                if dice1 == 1:
                    screen.blit(dice_img1, dice1_position)
                elif dice1 == 2:
                    screen.blit(dice_img2, dice1_position)
                elif dice1 == 3:
                    screen.blit(dice_img3, dice1_position)
                elif dice1 == 4:
                    screen.blit(dice_img4, dice1_position)
                elif dice1 == 5:
                    screen.blit(dice_img5, dice1_position)
                else:
                    screen.blit(dice_img6, dice1_position)
                type_text(f"1st Dice: {dice1}", text_font, (255, 255, 255), 200, 350)

                if dice2 == 1:
                    screen.blit(dice_img1, dice2_position)
                elif dice2 == 2:
                    screen.blit(dice_img2, dice2_position)
                elif dice2 == 3:
                    screen.blit(dice_img3, dice2_position)
                elif dice2 == 4:
                    screen.blit(dice_img4, dice2_position)
                elif dice2 == 5:
                    screen.blit(dice_img5, dice2_position)
                else:
                    screen.blit(dice_img6, dice2_position)
                type_text(f"2nd Dice: {dice2}", text_font, (255, 255, 255), 500, 350)

                type_text(f"Dice Value: {dice_value}", text_font, (255, 255, 255), 340, 450)

            pygame.display.update()

pygame.quit()