# start-up screen with button class

import pygame
import sys
import tools

class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE // 2)

    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    

def draw_back_button(surface):
    return Button(tools.WIDTH - 200, tools.HEIGHT - 80, tools.B_WIDTH, tools.B_HEIGHT, "Main Menu", tools.WHITE, tools.GRAY)

def draw_menu(surface, clock):
    font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE)

    # Create buttons
    button_3x3 = Button(200, 200, tools.B_WIDTH, tools.B_HEIGHT, "3x3 Cube", tools.WHITE, tools.D_GRAY)
    button_2x2 = Button(200, 300, tools.B_WIDTH, tools.B_HEIGHT, "2x2 Cube", tools.WHITE, tools.D_GRAY)
    button_quit = Button(200, 400, tools.B_WIDTH, tools.B_HEIGHT, "Quit", tools.WHITE, tools.D_GRAY)

    while True:
        clock.tick(30)
        surface.fill(tools.BLACK)

        # Render title
        title_text = font.render("Select Cube Type", True, tools.WHITE)
        surface.blit(title_text, (tools.WIDTH // 2 - title_text.get_width() // 2, 100))

        # Draw buttons
        button_3x3.draw(surface)
        button_2x2.draw(surface)
        button_quit.draw(surface)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_3x3.is_clicked(event.pos):
                    return "round1"     # starting stage for 3x3
                elif button_2x2.is_clicked(event.pos):
                    return "first"      # starting stage for 2x2
                elif button_quit.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()