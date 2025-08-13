# 2x2 cube logic and drawing
import pygame
import tools
from algs import TWO

# 3x3 for these cases
CUBE_SIZE = 2

def draw_label_above(surface, text, font, center_x, top_y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, top_y - 10))  # this ensures it stays centered over cube
    surface.blit(text_surface, text_rect)

class twoDraw:
    def draw_first(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.FIRST), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "First Layer", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.WHITE, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

    def draw_checker(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.CHECKER), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Checker", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.WHITE, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)
    
    def draw_Y1(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y1), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y1", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if row == 0 and col == 1:
                    color = tools.YELLOW
                else:
                    color = tools.GRAY
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - ht, 
            START_Y + sz, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

    def draw_Y2(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y2), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y2", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if row == 0 and col == 0:
                    color = tools.YELLOW
                else:
                    color = tools.GRAY
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right side line
        line = pygame.Rect(
            START_X + r_side*2, 
            START_Y + sz, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

    def draw_Y3(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y3), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y3", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.GRAY, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line) 

    def draw_Y4(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y4), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y4", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, tools.GRAY, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border


        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # top left side line
        line = pygame.Rect(
            START_X - ht, 
            START_Y, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - ht, 
            START_Y + sz, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line) 

    def draw_Y5(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y5), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y5", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if col == 1:
                    color = tools.YELLOW
                else:
                    color = tools.GRAY
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left side line
        line = pygame.Rect(
            START_X - ht, 
            START_Y, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - ht, 
            START_Y + sz, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

    def draw_Y6(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y6), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y6", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if col == 1:
                    color = tools.YELLOW
                else:
                    color = tools.GRAY
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left line
        line = pygame.Rect(
            START_X, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

    def draw_Y7(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.Y7), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Y7", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if col == row:
                    color = tools.YELLOW
                else:
                    color = tools.GRAY
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top right side line
        line = pygame.Rect(
            START_X + 2 * sz + ht, 
            START_Y, 
            ht, ln
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

    def draw_last(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.LAST), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        # text for case label
        draw_label_above(surface, "Last Layer", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

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
            ln, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.RED, line)

    def draw_mixed(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        ht = tools.LINE_HEIGHT
        ln = sz - 3
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE - 6) 

        if alg_flag:
            text_surface = font.render(" ".join(TWO.LAST), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE
            ln = tools.SM_LEN

        r_side = sz
        bott_side = ht + 2 * sz
        top_side = ht

        # text for case label
        draw_label_above(surface, "Mixed", font, START_X + sz*2 // 2, START_Y - 20, tools.WHITE)

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
            ln, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.GREEN, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            ln, ht
        )

        pygame.draw.rect(surface, tools.BLUE, line)