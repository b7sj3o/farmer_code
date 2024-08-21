import requests
import pygame
from config.urls import FASTAPI_URL_LOGIN, FASTAPI_URL_GET_USER
from config.sizes import WIDTH, COMPILER_WIDTH, COMPILER_HEIGHT
from config.other import TABS, FONT
from .blanks import GUIBlanks


class Compiler:
    def __init__(self):
        self.blanks = GUIBlanks()
        self.code_to_execute = """"""
        self.lines = [""]
        self.code = {
            "text": "",
            "line": 1
        }
        self.cursor_position = 0
        self.active_input = False

        self.title_text = "Compiler"
        self.last_line_tabs = 0

        self.create_elements()

        self.current_line_width = 0

        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            self.active_input = self.blanks.compiler_rect.collidepoint(event.pos)           

        elif ( event.type == pygame.KEYDOWN ) and self.active_input: 
            # remove char || previous line
            if event.key == pygame.K_BACKSPACE: 
                if not self.code["text"]:
                    self.previous_line()
                else:
                    self.code["text"] = self.code["text"][:-1]

            # next line
            elif event.key == pygame.K_RETURN:
                self.next_line()
            

            # move curson among the code
            elif event.key == pygame.K_LEFT:
                ...
            elif event.key == pygame.K_RIGHT:
                ...
            elif event.key == pygame.K_UP:
                ...
            elif event.key == pygame.K_DOWN:
                ...



            # add char to code
            else: 
                if event.unicode:
                    self.code["text"] += event.unicode

            try:
                self.lines[self.code["line"]-1] = self.code["text"]
            except:
                print(self.lines)


    def update(self):
        ...
            

    def render(self, surface):
        self.blanks.render_compiler(surface, self.lines)
        self.blanks.render_text(surface)

        if self.active_input:
            self.blanks.render_cursor(surface)

        self.update_cursor_position()


    def create_elements(self):
        self.blanks.create_text(
            text=self.title_text,
            x=100,
            y=100,
        )

        self.blanks.create_compiler(
            x=self.blanks.get_center_x(COMPILER_WIDTH),
            y=self.blanks.get_center_y(COMPILER_HEIGHT),
            width=COMPILER_WIDTH,
            height=COMPILER_HEIGHT
        )

        self.blanks.create_cursor(
            x=0,
            y=0,
            width=3,
            height=FONT.get_height()
        )
        


    def next_line(self):
        text = self.code["text"]

        self.lines.append("")
        self.code["line"] += 1
        self.last_line_tabs = len(text) - len(text.lstrip())

        # spacing
        if text and text[-1] == ":":
            self.code["text"] = " " * max(self.last_line_tabs + TABS, TABS)
        else:
            if self.last_line_tabs:
                self.code["text"] = " "*self.last_line_tabs
            else:
                self.code["text"] = ""

    
    def previous_line(self):

        if self.code["line"] > 1:
            self.lines.pop(self.code["line"]-1)
            self.code["line"] += -1
            self.code["text"] = self.lines[self.code["line"]-1 or 0]
        else:
            self.code["text"] = ""


    def move_cursor(self, move_x, move_y):
        self.code["line"] += move_y
        self.cursor_position += move_x


    def cursor_line(self):
        ...


    def update_cursor_position(self):
        self.blanks.cursor_rect.x = self.blanks.compiler_code_rects[self.code["line"]-1].width + self.blanks.compiler_rect.x
        self.blanks.cursor_rect.y = ( FONT.get_height() * (self.code["line"] - 1) ) + self.blanks.compiler_rect.y