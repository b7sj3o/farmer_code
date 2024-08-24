import pygame
from config import *


class GUIBlanks:
    def __init__(self):
        self.text_surfaces = []
        self.text_rects = []
        self.text_const_surfaces = []
        self.text_const_rects = []
        self.input_rect = None
        self.compiler_rect = None
        self.compiler_code_surfaces = []
        self.compiler_code_rects = []
        self.compiler_start_rect = None
        self.compiler_stop_rect = None
        self.cursor_rect = []

    def create_const_text(self, text, x, y, color=BLACK, font_size=20):
        font = pygame.font.Font(FONT_REGULAR, size=font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.text_const_surfaces.append(text_surface)
        self.text_const_rects.append(text_rect)

    def create_text(self, text, x, y, color=BLACK, font_size=20):
        self.text_surfaces.clear()
        self.text_rects.clear()

        font = pygame.font.Font(FONT_REGULAR, size=font_size)
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
        
        for text_surface, text_rect in zip(self.text_const_surfaces, self.text_const_rects):
            surface.blit(text_surface, text_rect)

    def create_input(self, x, y, width, height):
        self.input_rect = pygame.Rect(x, y, width, height)

    def render_input(self, surface, text):
        font = pygame.font.Font(FONT_REGULAR, FONT_SIZE_SMALL)
        color = INPUT_ACTIVE if self.input_rect.collidepoint(pygame.mouse.get_pos()) else INPUT_PASSIVE
        pygame.draw.rect(surface, color, self.input_rect)

        text_surface = font.render(text, True, BLACK)
        surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(self.input_rect.w, text_surface.get_width() + 10)

    def create_compiler(self, x, y, width, height):
        # compiler
        self.compiler_rect = pygame.Rect(x, y, width, height)

        #compiler buttons
        self.compiler_start_rect = pygame.Rect(x, y-40, 30, 30)  
        self.compiler_stop_rect = pygame.Rect(x+40, y-40, 30, 30)

        # cursor
        font = pygame.font.Font(FONT_REGULAR, FONT_SIZE_SMALL)
        cursor_width = 3
        cursor_height = font.get_height()
        self.cursor_rect = pygame.Rect(x, y, cursor_width, cursor_height)


    def render_compiler(self, surface, lines):
        self.compiler_code_surfaces.clear()
        self.compiler_code_rects.clear()

        color = INPUT_ACTIVE if self.compiler_rect.collidepoint(pygame.mouse.get_pos()) else INPUT_PASSIVE
        pygame.draw.rect(surface, color, self.compiler_rect, 2)

        font = pygame.font.Font(FONT_REGULAR, 18)
        line_height = font.get_height()
        y_indent = self.compiler_rect.y

        # create compiler text (multiline)
        for line in lines:
            text_surface = font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(topleft=(self.compiler_rect.x, y_indent))
            self.compiler_code_surfaces.append(text_surface)
            self.compiler_code_rects.append(text_rect)
            y_indent += line_height

        # render compiler text
        for compiler_code_surface, compiler_code_rect in zip(self.compiler_code_surfaces, self.compiler_code_rects):
            surface.blit(compiler_code_surface, compiler_code_rect)

        # render compiler buttons
        button_surface = font.render("START", True, WHITE)
        button_rect = button_surface.get_rect(center=self.compiler_start_rect.center)
        surface.blit(button_surface, button_rect)

        self.compiler_start_rect.width = button_rect.width + 10
        pygame.draw.rect(surface, INPUT_PASSIVE, self.compiler_start_rect, 3)

        button_surface = font.render("STOP", True, WHITE)
        button_rect = button_surface.get_rect(center=self.compiler_stop_rect.center)
        surface.blit(button_surface, button_rect)

        self.compiler_stop_rect.width = button_rect.width + 10
        self.compiler_stop_rect.x = self.compiler_start_rect.x + self.compiler_start_rect.width + 10
        pygame.draw.rect(surface, INPUT_PASSIVE, self.compiler_stop_rect, 3)


    def update_cursor(self, pos_x, pos_y, lines):
        font = pygame.font.Font(FONT_REGULAR, FONT_SIZE_SMALL)
        line_width = 0
        try:
            line_width = self.compiler_code_rects[pos_y].width / len(lines[pos_y]) * (pos_x + 1)
        except:
            pass
        self.cursor_rect.x = line_width + self.compiler_rect.x
        self.cursor_rect.y = (font.get_height() * pos_y) + self.compiler_rect.y

    
    def render_cursor(self, surface):
        pygame.draw.rect(surface, WHITE, self.cursor_rect)
        

    @staticmethod
    def get_center_x(width):
        return (WIDTH // 2) - (width // 2)

    @staticmethod
    def get_center_y(height):
        return (HEIGHT // 2) - (height // 2)
