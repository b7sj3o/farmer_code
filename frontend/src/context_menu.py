from pygame import *
from config import *


class ContextMenu:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = [UIElement(x, y + ind * 30, 150, 30, text=item) for ind, item in enumerate(items)]
        self.last_clicked = None
    
    def render(self, surface):
        for item in self.items:
            item.render(surface)

    def handle_event(self, event):
        for item in self.items:
            if item.is_clicked(event):
                return item.text
        return None



class UIElement:
    def __init__(self, x, y, width, height, color=WHITE, border_color=BLACK, text='', text_color=BLACK, font_size=FONT_SIZE_SMALL):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.border_color = border_color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(FONT_REGULAR, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        surface.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False
