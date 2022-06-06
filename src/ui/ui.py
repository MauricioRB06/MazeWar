
import pygame


class TextUI:

    def __init__(self, text, position, font_color):

        self.text = text
        self.fontColor = font_color
        self.position = position

        self.font = 'freesansbold.ttf'
        self.anchor = 'center'
        self.fontSize = 20

    def render(self, screen):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.fontColor)
        text_rect = text.get_rect()
        setattr(text_rect, self.anchor, self.position)
        screen.blit(text, text_rect)
