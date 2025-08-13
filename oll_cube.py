# OLL cube logic and drawing
import pygame
import tools
from algs import OLL

# 3x3 for these cases
CUBE_SIZE = 3

def draw_label_above(surface, text, font, center_x, top_y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, top_y))  # this ensures it stays centered over cube
    surface.blit(text_surface, text_rect)

class ollDraw:
    def draw_line(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE    # declare size but make it so we can adjust it
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.LINE), True, tools.WHITE)   # text for algorithm
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE

        # text for case label
        draw_label_above(surface, "Line", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if row == 1:
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

        

    def draw_lshape(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.L_SHAPE), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE

        draw_label_above(surface, "L-shape", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 1 and col == 1) or (row == 1 and col == 2) or (row == 2 and col == 1):
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

        

    def draw_dot(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.DOT), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE

        draw_label_above(surface, "Dot", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 1 and col == 1):
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

        

    def draw_sune(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.SUNE), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        # determine sizes for small yellow lines
        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "Sune", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 0) or (row == 0 and col == 2) or (row == 2 and col == 2):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line) 
        

    def draw_antisune(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE)
        ht = tools.LINE_HEIGHT

        if alg_flag:
            text_surface = font.render(" ".join(OLL.ANTISUNE), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        # determine sizes for small yellow lines
        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "Antisune", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 0) or (row == 0 and col == 2) or (row == 2 and col == 0):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)
        

    def draw_h(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.H), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "H", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 0) or (row == 0 and col == 2) or (row == 2 and col == 0) or (row == 2 and col == 2):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
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
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)
        

    def draw_pi(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.PI), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "Pi", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 0) or (row == 0 and col == 2) or (row == 2 and col == 0) or (row == 2 and col == 2):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # top right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y - top_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left side line
        line = pygame.Rect(
            START_X - 2 * ht, 
            START_Y + 2 * sz, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)
        

    def draw_l(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.L), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "L", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 2) or (row == 2 and col == 0):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # top right side line
        line = pygame.Rect(
            START_X + 3 * sz + ht, 
            START_Y, 
            ht, sz
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)
        

    def draw_t(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.T), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "T", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 0 and col == 0) or (row == 2 and col == 0):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
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
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)
        

    def draw_u(surface, START_X, START_Y, ALG_X, alg_flag):
        sz = tools.TILE_SIZE
        ht = tools.LINE_HEIGHT
        font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE) 

        if alg_flag:
            text_surface = font.render(" ".join(OLL.U), True, tools.WHITE)
            surface.blit(text_surface, (ALG_X, tools.ALG_TEXT_Y))
        else:
            sz = tools.SMALL_TILE
            ht = tools.SMALL_LINE

        r_side = 2 * sz
        bott_side = ht + 3 * sz
        top_side = 2 * ht

        draw_label_above(surface, "U", font, START_X + sz*3 // 2, START_Y - 20, tools.WHITE)

        for row in range(CUBE_SIZE):
            for col in range(CUBE_SIZE):
                if (row == 2 and col == 0) or (row == 2 and col == 2):
                    color = tools.GRAY
                else:
                    color = tools.YELLOW
                rect = pygame.Rect(
                    START_X + col * sz,
                    START_Y + row * sz,
                    sz, sz
                )
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, tools.BLACK, rect, 2)  # black border

        # bottom left line
        line = pygame.Rect(
            START_X, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)

        # bottom right line
        line = pygame.Rect(
            START_X + r_side, 
            START_Y + bott_side, 
            sz, ht
        )

        pygame.draw.rect(surface, tools.YELLOW, line)        