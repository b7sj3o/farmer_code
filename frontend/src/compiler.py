import requests
import pygame
import pyperclip
from config import *
from .blanks import GUIBlanks
from .executor import Executor
import threading

class Compiler:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.executor = Executor(parent)
        self.blanks = GUIBlanks()
        self.lines = [""]
        self.code = {
            "text": "",
            "line": 1
        }
        self.cursor_position = 0
        self.active_input = False
        self.last_line_tabs = 0
        self.create_elements()
        self.rect = self.blanks.compiler_rect
        # self.executor_thread = threading.Thread(target=self.executor.execute)
        # self.executor_thread.start()
        # self.console_rect = None
        # self.create_console()
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            self.active_input = self.blanks.compiler_rect.collidepoint(event.pos)   

            if self.blanks.compiler_start_rect.collidepoint(event.pos):
                self.start_execution()
            elif self.blanks.compiler_stop_rect.collidepoint(event.pos):
                self.stop_execution()

        elif ( event.type == pygame.KEYDOWN ) and self.active_input: 
            # remove char || previous line
            if event.key == pygame.K_BACKSPACE: 
                if not self.code["text"]:
                    self.previous_line()
                else:
                    self.code["text"] = self.code["text"][:self.cursor_position-1] + self.code["text"][self.cursor_position:]
                    self.cursor_position -= 1

            # next line
            elif event.key == pygame.K_RETURN:
                self.next_line()
            
            # Ctrl + [key]
            # elif pygame.key.get_mods() & pygame.KMOD_CTRL:
            #     if event.key == pygame.K_s:
            #         self.execute_code()
            #     elif event.key == pygame.K_v:
            #         self.code["text"] += pyperclip.paste()

            # move curson among the code
            elif event.key == pygame.K_LEFT:
                self.move_cursor(x=-1, y=0)
            elif event.key == pygame.K_RIGHT:
                self.move_cursor(x=1, y=0)
            elif event.key == pygame.K_UP:
                self.move_cursor(x=0, y=-1)
            elif event.key == pygame.K_DOWN:
                self.move_cursor(x=0, y=1)

            # add char to code
            else: 
                if event.unicode:
                    self.code["text"] = self.code["text"][:self.cursor_position] + event.unicode + self.code["text"][self.cursor_position:]
                    self.cursor_position += 1
            
            self.lines[self.code["line"]-1] = self.code["text"]


    def update(self):
        ...
            

    def render(self, surface):
        self.blanks.render_compiler(surface, self.lines)
        self.blanks.render_text(surface)

        if self.active_input:
            self.blanks.render_cursor(surface)
        

        self.blanks.update_cursor(
            pos_x=self.cursor_position-1,
            pos_y=self.code["line"]-1,
            lines=self.lines
        )

        # pygame.draw.rect(surface, BLACK, self.console_rect, 2)


    def create_elements(self):
        self.blanks.create_compiler(
            x=self.x,
            y=self.y,
            width=COMPILER_WIDTH,
            height=COMPILER_HEIGHT
        )

    
    # def create_console(self):
    #     console_x = self.x
    #     console_y = self.y + COMPILER_HEIGHT

    #     self.console_rect = pygame.Rect(console_x, console_y, COMPILER_WIDTH, COMPILER_HEIGHT//2)
    #     self.blanks.create_const_text("Output", self.console_rect.x + 50, self.console_rect.y + 20, font_size=30)


    def next_line(self):
        text = self.code["text"]

        self.lines.append("")
        self.code["line"] += 1
        self.last_line_tabs = len(text) - len(text.lstrip())


        # spacing
        if text and text[-1] == ":":
            self.code["text"] = " " * max(self.last_line_tabs + SPACES, SPACES)
        else:
            if self.last_line_tabs:
                self.code["text"] = " "*self.last_line_tabs
            else:
                self.code["text"] = ""

        self.cursor_position = len(self.code["text"])
        
    
    def previous_line(self):
        if self.code["line"] > 1:
            self.lines.pop(self.code["line"]-1)
            self.code["line"] += -1
            self.code["text"] = self.lines[self.code["line"]-1 or 0]
        else:
            self.code["text"] = ""

        self.cursor_position = len(self.code["text"])
        

    def move_cursor(self, x, y):
        line = self.code["line"] - 1  # Adjust for zero-based indexing
        current_line_length = len(self.lines[line])

        if x:
            new_position = self.cursor_position + x
            # move in the same line
            if 0 <= new_position <= current_line_length: 
                self.cursor_position = new_position
            
            # previous line
            elif new_position < 0 and line > 0:
                self.code["line"] -= 1
                self.cursor_position = len(self.lines[self.code["line"] - 1])
            
            # next line
            elif new_position > current_line_length and line < len(self.lines) - 1: 
                self.code["line"] += 1
                self.cursor_position = 0
            self.code["text"] = self.lines[self.code["line"]-1]

        if y:
            new_line = self.code["line"] + y
            if 1 <= new_line <= len(self.lines):
                self.code["line"] = new_line
                self.code["text"] = self.lines[self.code["line"]-1]
                self.cursor_position = min(self.cursor_position, len(self.lines[new_line - 1]))


    def start_execution(self):
        code_to_execute = """"""
        for line in self.lines:
            code_to_execute += line
            code_to_execute += "\n"
            if "while" in line or "for" in line:
                line_tabs = len(line) - len(line.lstrip())
                code_to_execute += "{}update_locals()".format(" "*(line_tabs + SPACES)) + "\n"

        self.executor.code = code_to_execute
        
        self.executor_thread = threading.Thread(target=self.executor.execute)
        self.executor_thread.start()
        


    def stop_execution(self):
        # self.executor.stop_execution()
        ...
