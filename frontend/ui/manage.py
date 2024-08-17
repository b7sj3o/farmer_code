import pygame
import sys
import requests

from config import *


 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Farmer code")

    running = True
    base_font = pygame.font.Font(None, 32) 
    clock = pygame.time.Clock()
    user_text = '' 
    # img = pygame.image.load(IMG_BLOCK)

    input_rect = pygame.Rect(200, 200, 140, 32) 

    color_active = pygame.Color('lightskyblue3') 
    color_passive = pygame.Color('chartreuse4') 
    color = color_passive 

    active = False

    
    while running:
        screen.fill(BLACK)

        # screen.blit(img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    sys.exit()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE: 
                    user_text = user_text[:-1] 

                elif event.key == pygame.K_RETURN:
                    response = requests.post(FASTAPI_URL_LOGIN, json={
                        "username": user_text
                    })
                
                elif event.unicode.isalnum() or event.unicode in ["_"]: 
                    user_text += event.unicode


        if active: 
            color = color_active 
        else: 
            color = color_passive     

        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255)) 

        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
    
        input_rect.w = max(100, text_surface.get_width()+10) 

        pygame.display.flip()
 
