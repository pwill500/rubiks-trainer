# main logic and entry point

import pygame
import tools
import ui
import startup

# Pygame Setup
pygame.init()
WIN = pygame.display.set_mode((tools.WIDTH, tools.HEIGHT))
pygame.display.set_caption("2-Look OLL/PLL Trainer (Pygame)")

# Main loop

def main():
    clock = pygame.time.Clock()
    mode = startup.draw_menu(WIN, clock)

    current_stage = mode

    while True:
        if current_stage == "first" or current_stage == "yellow" or current_stage == "last":
            start_x = tools.WIDTH // 2 - tools.TILE_SIZE * 2 // 2
            start_y = tools.HEIGHT // 2 - tools.TILE_SIZE * 2 // 2
        else:
            start_x = tools.WIDTH // 2 - tools.TILE_SIZE * 3 // 2
            start_y = tools.HEIGHT // 2 - tools.TILE_SIZE * 3 // 2

        if current_stage == "round1" or current_stage == "round2":
            current_stage = ui.oll_select(WIN, start_x, start_y, clock, current_stage)
        elif current_stage == "corner" or current_stage == "edge":
            current_stage = ui.pll_select(WIN, start_x, start_y, clock, current_stage)
        elif current_stage == "first" or current_stage == "yellow" or current_stage == "last":
            current_stage = ui.two_select(WIN, start_x, start_y, clock, current_stage)
        elif current_stage == "menu":
            current_stage = startup.draw_menu(WIN, clock)
    

if __name__ == "__main__":
    main() 