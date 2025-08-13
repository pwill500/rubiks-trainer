# PLL cube logic and drawing
import pygame
import tools
from algs import PLL

# 3x3 for these cases
CUBE_SIZE = 3

def draw_label_above(surface, text, font, center_x, top_y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, top_y - 10))  # this ensures it stays centered over cube
    surface.blit(text_surface, text_rect)

def draw_rotation_arrow(surface, center_x, top_y, direction="cw"):
    size = 20  # arrow size
    height = 15  # vertical height from tip to base

    if direction == "cw":
        # Pointing right
        point = (center_x + size, top_y)
        left = (center_x - size, top_y - height)
        right = (center_x - size, top_y + height)
    else:
        # Pointing left
        point = (center_x - size, top_y)
        left = (center_x + size, top_y - height)
        right = (center_x + size, top_y + height)

    pygame.draw.polygon(surface, tools.WHITE, [point, left, right])


class pllDraw:
    def draw_diagonal(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.DIAGONAL), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE

        # text for case label
        draw_label_above(surface, "Diagonal", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

    def draw_headlights(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.HEADLIGHTS), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "Headlights", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.RED, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y + 2 * sz, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.RED, line) 

    def draw_ccw(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.CCW), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "CCW", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # full top line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            sz*3, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        if not alg_flag:
            draw_rotation_arrow(surface, START_X + sz*3 // 2, START_Y + sz, "ccw")

    def draw_cw(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.CW), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "CW", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # full top line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            sz*3, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        if not alg_flag:
            draw_rotation_arrow(surface, START_X + sz*3 // 2, START_Y + sz, "cw")

    def draw_opposite(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.OPPOSITE), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "Opposite", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)

        # top middle line
        line = pygame.Rect(
            START_X + sz + ht, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side + ht, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # bottom middle line
        line = pygame.Rect(
            START_X + sz + ht, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side + ht, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

    def draw_adjacent(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(PLL.ADJACENT), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "Adjacent", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.YELLOW, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        # top middle line
        line = pygame.Rect(
            START_X + sz + ht, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side + ht, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        # top left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y, 
            ht, sz - ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # middle left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y + sz, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.RED, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y + 2 * sz, 
            ht, sz - ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)