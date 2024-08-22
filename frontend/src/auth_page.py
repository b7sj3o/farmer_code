import requests
import pygame
from config import *
from .blanks import GUIBlanks

class AuthPage:
    def __init__(self):
        self.blanks = GUIBlanks()
        self.username = ""
        self.active_input = False
        self.response = None

        self.elapsed_time = 0  # in ms
        self.timer = 2  # in seconds
        self.clock = pygame.time.Clock()

        self.title_text = "Login Page"
        self.subtitle_text = (
            "Log in to your account.\n"
            "(write your username)\n"
            "If you don't have an account, open the Telegram bot @farmercode_bot.\n"
            "After signing up, return to the game and write your username,\n"
            "then confirm it in the chat with the Telegram bot."
        )

        self.background_image = pygame.image.load('frontend/assets/images/bg.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        self.create_elements()


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active_input = self.blanks.input_rect.collidepoint(event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.username = self.username[:-1]

            elif event.key == pygame.K_RETURN:
                self.post_form()

            elif event.unicode.isalnum() or event.unicode in ["_"]:
                self.username += event.unicode

    def update(self):
        dt = self.clock.tick()
        self.elapsed_time += dt
        self.check_confirmation()

    def check_confirmation(self):
        if self.elapsed_time > (self.timer * 1000):
            if self.response:
                self.response = requests.get(FASTAPI_URL_GET_USER, params={
                    "username": self.username
                })

                data = self.response.json()
                if data:
                    status_code = data.get("status_code")

                    if status_code in [401, 404]:
                        self.title_text = data.get("message")
                        self.blanks.create_text(
                            text=self.title_text,
                            x=self.blanks.get_center_x(500),
                            y=100,
                            font_size=FONT_SIZE_MEDIUM,
                            color=BLACK
                        )

                    elif status_code == 200:
                        self.title_text = "Logged in successfully"
                        response = None
                        self.blanks.create_text(
                            text=self.title_text,
                            x=self.blanks.get_center_x(500),
                            y=100,
                            font_size=FONT_SIZE_MEDIUM,
                            color=BLACK
                        )

            self.elapsed_time = 0

    def render(self, surface):
        surface.blit(self.background_image, (0, 0))

        self.blanks.render_text(surface)
        self.blanks.render_input(surface, self.username)

    def post_form(self):
        self.response = requests.post(FASTAPI_URL_LOGIN, json={
            "username": self.username
        })
        self.title_text = self.response.json().get("message")
        
        if self.title_text:
            self.blanks.create_text(
                text=self.title_text,
                x=self.blanks.get_center_x(500),
                y=100,
                font_size=FONT_SIZE_MEDIUM,
                color=BLACK
            )

    def create_elements(self):
        self.blanks.create_const_text(
            text=self.title_text,
            x=self.blanks.get_center_x(500),
            y=50,
            font_size=FONT_SIZE_BIG,
            color=BLACK

        )

        self.blanks.create_text(
            text=self.subtitle_text,
            x=self.blanks.get_center_x(500),
            y=100,
            font_size=FONT_SIZE_SMALL,
            color=BLACK
        )

        self.blanks.create_input(
            x=self.blanks.get_center_x(400),
            y=self.blanks.get_center_y(50) + 100,
            width=400,
            height=50
        )
