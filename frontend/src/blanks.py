import pygame
from config.colors import WHITE, BLACK, INPUT_ACTIVE, INPUT_PASSIVE
from config.sizes import WIDTH, HEIGHT
from config.other import FONT


class GUIBlanks:
    def __init__(self):
        self.text_surfaces = []
        self.text_rects = []
        self.input_rect = None
        
        self.compiler_rect = None
        self.compiler_code_surfaces = []
        self.compiler_code_rects = []

        self.cursor_rect = []




    def create_text(self, text, x, y, color=WHITE, font_size=30, font=FONT):
        lines = text.split('\n')
        line_height = font.get_height()
        y_indent = y

        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(topleft=(x, y_indent))

            self.text_surfaces.append(text_surface)
            self.text_rects.append(text_rect)

            y_indent += line_height


    def render_text(self, surface):
        for text_surface, text_rect in zip(self.text_surfaces, self.text_rects):
            surface.blit(text_surface, text_rect)


    def create_input(self, x, y, width, height):
        self.input_rect = pygame.Rect(x, y, width, height)
    
    
    def render_input(self, surface, text):
        color = INPUT_ACTIVE if self.input_rect.collidepoint(pygame.mouse.get_pos()) else INPUT_PASSIVE
        pygame.draw.rect(surface, color, self.input_rect, 2)

        text_surface = FONT.render(text, True, WHITE)
        surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(self.input_rect.w, text_surface.get_width() + 10) #TODO: add min() if text_surface.width < input_rect.width


    def create_compiler(self, x, y, width, height):
        self.compiler_rect = pygame.Rect(x, y, width, height)


    def render_compiler(self, surface, lines):
        self.compiler_code_surfaces = []
        self.compiler_code_rects = []

        # render compiler rect
        color = INPUT_ACTIVE if self.compiler_rect.collidepoint(pygame.mouse.get_pos()) else INPUT_PASSIVE
        pygame.draw.rect(surface, color, self.compiler_rect, 2)
        
        line_height = FONT.get_height()
        y_indent = self.compiler_rect.y
        
        for line in lines:
            text_surface = FONT.render(line, True, WHITE)
            text_rect = text_surface.get_rect(topleft=(self.compiler_rect.x, y_indent))
            self.compiler_code_surfaces.append(text_surface)
            self.compiler_code_rects.append(text_rect)

            y_indent += line_height


        # render multi-line code inside compiler
        for compiler_code_surface, compiler_code_rect in zip(self.compiler_code_surfaces, self.compiler_code_rects):
            surface.blit(compiler_code_surface, compiler_code_rect)
        
    def create_cursor(self, x, y, width, height):
        x = x + self.compiler_rect.x
        y = y + self.compiler_rect.y
        self.cursor_rect = pygame.Rect(x, y, width, height)

    def render_cursor(self, surface):
        pygame.draw.rect(surface, WHITE, self.cursor_rect)

    @staticmethod
    def get_center_x(width):
        return ( WIDTH // 2 ) - (width // 2)    


    @staticmethod
    def get_center_y(height):
        return ( HEIGHT // 2 ) - (height // 2) 