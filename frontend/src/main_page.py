import pygame
from pygame.locals import *
from config import *
from .compiler import Compiler
from .context_menu import ContextMenu
from .block import Block


class MainPage:
    def __init__(self):
        self.compilers = []
        self.blocks = []
        self.surface = None
        self.context_menu = None
        self.blocks = []

    def update(self):
        if self.compilers:
            for compiler in self.compilers:
                compiler.update()

    def handle_event(self, event):
        if event.type == MOUSEBUTTONUP:
            if event.button == 3: # Right click
                self.context_menu = ContextMenu(event.pos[0], event.pos[1], ['Create compiler', 'Delete compiler', 'Create block'])
            elif event.button == 1: # Left click
                if self.context_menu:
                    clicked_item_text = self.context_menu.handle_event(event)
                    if clicked_item_text == "Create compiler":
                        self.create_compiler(event.pos)
                    elif clicked_item_text == "Delete compiler":
                        self.delete_compiler(event.pos)
                    elif clicked_item_text == "Create block":
                        self.create_block(event.pos)

                    self.context_menu = None
                

        
        if self.compilers:
            for compiler in self.compilers:
                compiler.handle_event(event)
    
    def render(self, surface):
        self.surface = surface

        if self.compilers:
            for compiler in self.compilers:
                compiler.render(surface)

        if self.context_menu:
            self.context_menu.render(surface)

        if self.blocks:
            for block in self.blocks:
                block.render(surface)

        
    def create_elements(self):
        ...


    def create_compiler(self, pos):
        if not any(compiler.x == pos[0] and compiler.y == pos[0] for compiler in self.compilers):
            new_x = min(pos[0], WIDTH - COMPILER_WIDTH)
            new_y = min(pos[1], HEIGHT - COMPILER_HEIGHT)
            self.compilers.append(Compiler(x=new_x, y=new_y, parent=self))


    def create_block(self, pos):
        if not any(block.x == pos[0] and block.y == pos[1] for block in self.blocks):
            new_x = min(pos[0], WIDTH - COMPILER_WIDTH)
            new_y = min(pos[1], HEIGHT - COMPILER_HEIGHT)
            self.blocks.append(Block(x=new_x, y=new_y))
    

    def delete_compiler(self, pos):
        selected_compilers = [compiler for compiler in self.compilers if compiler.rect.collidepoint(pos)]
        for compiler in selected_compilers:
            self.compilers.remove(compiler)