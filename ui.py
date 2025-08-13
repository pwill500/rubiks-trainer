# menu and UI components

import pygame
import sys
import tools
from oll_cube import ollDraw
from pll_cube import pllDraw
from two_cube import twoDraw
from startup import draw_back_button

def two_select(surface, START_X, START_Y, clock, stage):
    font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE)
    showing_case = None

    # draw positions, initialize dict to do so
    # we can store the function names inside the tuples for later use 
    if stage == "first":
        label_text = "Select first layer case"
        case_data = {
            "first":    (200, START_Y + tools.TEXT_BUF, 175, twoDraw.draw_first),     # x, y, alg_x, draw_fn
            "checker":  (400, START_Y + tools.TEXT_BUF, 225, twoDraw.draw_checker),
        }

    elif stage == "yellow":
        label_text = "Select yellow case"
        case_data = {
            "Y1":   (tools.TOP_GAPS, START_Y + tools.TEXT_BUF, 185, twoDraw.draw_Y1),   # x, y, alg_x, draw_fn
            "Y2":   (tools.TOP_GAPS * 2 + tools.TOTAL_SM, START_Y + tools.TEXT_BUF, 185, twoDraw.draw_Y2),
            "Y3":   (tools.TOP_GAPS * 3 + tools.TOTAL_SM * 2, START_Y + tools.TEXT_BUF, 200, twoDraw.draw_Y3),
            "Y4":   (tools.TOP_GAPS * 4 + tools.TOTAL_SM * 3, START_Y + tools.TEXT_BUF, 170, twoDraw.draw_Y4),
            "Y5":   (tools.TOP_GAPS * 2, START_Y + tools.BOTT_Y, 190, twoDraw.draw_Y5),
            "Y6":   (tools.TOP_GAPS * 3 + tools.TOTAL_SM, START_Y + tools.BOTT_Y, 180, twoDraw.draw_Y6),
            "Y7":   (tools.TOP_GAPS * 4 + tools.TOTAL_SM * 2, START_Y + tools.BOTT_Y, 175, twoDraw.draw_Y7),
        }

    elif stage == "last":
        label_text = "Select final layer case"
        case_data = {
            "last":    (200, START_Y + tools.TEXT_BUF, 165, twoDraw.draw_last),     # x, y, alg_x, draw_fn
            "mixed":  (400, START_Y + tools.TEXT_BUF, 165, twoDraw.draw_mixed),
        }

    else:
        raise ValueError("Invalid stage")
    
    # generate rectangles
    # we can use the name, as well as x and y coordinates from whichever case_data dict above
    # we don't care about the function name here as it isn't relevant when drawing the rectangles
    case_rects = {
        name: pygame.Rect(x, y, tools.TOTAL_SM, tools.TOTAL_SM)
        for name, (x, y, _, _) in case_data.items()
    }

    back_button = draw_back_button(surface)

    # main
    while True:
        clock.tick(30)
        surface.fill(tools.BLACK)

        back_button.draw(surface)

        if showing_case is None:
            text_surface = font.render(label_text, True, tools.WHITE)
            surface.blit(text_surface, (120, tools.LABEL_Y))

            for name, (x, y, _, draw_fn) in case_data.items():
                draw_fn(surface, x, y, 0, False)
        else:
            # show full-size selected case
            # where underscore means "don't care" and we can just grab the function
            _, _, alg_x, draw_fn = case_data[showing_case]
            draw_fn(surface, START_X, START_Y, alg_x, True)

        pygame.display.flip()

        # handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if we click inside the invisible rectangle, make sure we know which case is showing
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if showing_case is None:
                    for name, rect in case_rects.items():
                        if rect.collidepoint(event.pos):
                            showing_case = name
                            break
                if back_button.is_clicked(event.pos):   # "is_clicked" also comes from startup.py
                    return "menu"

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT:
                        if stage == "first":
                            return "yellow"
                        elif stage == "yellow":
                            return "last"  
                        elif stage == "last" and showing_case == "mixed":
                            return "last"
                        else:
                            return "menu"
                    case pygame.K_LEFT:
                        if stage == "yellow":
                            return "first"
                        elif stage == "last":
                            return "yellow"
                        else:
                            return "menu"
                    case pygame.K_ESCAPE:
                        showing_case = None

# ======== start 3x3 ========

def pll_select(surface, START_X, START_Y, clock, stage):
    font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE)
    showing_case = None

    # draw positions, initialize dict to do so
    # we can store the function names inside the tuples for later use 
    if stage == "corner":
        label_text = "Select corner PLL case"
        case_data = {
            "diagonal":    (200, START_Y + tools.TEXT_BUF, 50, pllDraw.draw_diagonal),     # x, y, alg_x, draw_fn
            "headlights":  (400, START_Y + tools.TEXT_BUF, 50, pllDraw.draw_headlights),
        }

    elif stage == "edge":
        label_text = "Select edge PLL case"
        case_data = {
            "ccw":     (tools.TOP_GAPS * 2, START_Y + tools.TEXT_BUF, 50, pllDraw.draw_ccw),   # x, y, alg_x, draw_fn
            "cw": (tools.TOP_GAPS * 2 + tools.TOTAL_SM * 3, START_Y + tools.TEXT_BUF, 50, pllDraw.draw_cw),
            "opposite":        (tools.TOP_GAPS * 2, START_Y + tools.BOTT_Y, 100, pllDraw.draw_opposite),
            "adjacent":       (tools.TOP_GAPS * 2 + tools.TOTAL_SM * 3, START_Y + tools.BOTT_Y, 100, pllDraw.draw_adjacent),
        }

    else:
        raise ValueError("Invalid stage")
    
    # generate rectangles
    # we can use the name, as well as x and y coordinates from whichever case_data dict above
    # we don't care about the function name here as it isn't relevant when drawing the rectangles
    case_rects = {
        name: pygame.Rect(x, y, tools.TOTAL_SM, tools.TOTAL_SM)
        for name, (x, y, _, _) in case_data.items()
    }

    back_button = draw_back_button(surface)

    # main section
    while True:
        clock.tick(30)
        surface.fill(tools.BLACK)

        back_button.draw(surface)

        if showing_case is None:
            text_surface = font.render(label_text, True, tools.WHITE)
            surface.blit(text_surface, (120, tools.LABEL_Y))

            for name, (x, y, _, draw_fn) in case_data.items():
                draw_fn(surface, x, y, 0, False)
        else:
            # show full-size selected case
            # where underscore means "don't care" and we can just grab the function
            _, _, alg_x, draw_fn = case_data[showing_case]
            draw_fn(surface, START_X, START_Y, alg_x, True)

        pygame.display.flip()

        # handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if showing_case is None:
                    for name, rect in case_rects.items():
                        if rect.collidepoint(event.pos):
                            showing_case = name
                            break
                if back_button.is_clicked(event.pos):   # "is_clicked" also comes from startup.py
                    return "menu"

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT:
                        return "edge" if stage == "corner" else "menu"
                    case pygame.K_LEFT:
                        return "corner" if stage == "edge" else "menu"
                    case pygame.K_ESCAPE:
                        showing_case = None

def oll_select(surface, START_X, START_Y, clock, stage):
    font = pygame.font.SysFont(tools.FONT_NAME, tools.FONT_SIZE)
    showing_case = None

    # draw positions, initialize dict to do so
    # we can store the function names inside the tuples for later use 
    if stage == "round1":
        label_text = "Select initial OLL case"
        case_data = {
            "line":    (150, START_Y + tools.TEXT_BUF, 200, ollDraw.draw_line),
            "lshape":  (300, START_Y + tools.TEXT_BUF, 200, ollDraw.draw_lshape),
            "dot":     (450, START_Y + tools.TEXT_BUF, 100, ollDraw.draw_dot),
        }

    elif stage == "round2":
        label_text = "Select round 2 OLL case"
        case_data = {
            "sune":     (tools.TOP_GAPS, START_Y + tools.TEXT_BUF, 200, ollDraw.draw_sune),
            "antisune": (tools.TOP_GAPS * 2 + tools.TOTAL_SM, START_Y + tools.TEXT_BUF, 200, ollDraw.draw_antisune),
            "h":        (tools.TOP_GAPS * 3 + tools.TOTAL_SM * 2, START_Y + tools.TEXT_BUF, 50, ollDraw.draw_h),
            "pi":       (tools.TOP_GAPS * 4 + tools.TOTAL_SM * 3, START_Y + tools.TEXT_BUF, 75, ollDraw.draw_pi),
            "l":        (tools.TOP_GAPS * 2, START_Y + tools.BOTT_Y, 120, ollDraw.draw_l),
            "t":        (tools.TOP_GAPS * 2 + tools.TOTAL_SM * 2, START_Y + tools.BOTT_Y, 120, ollDraw.draw_t),
            "u":        (tools.TOP_GAPS * 2 + tools.TOTAL_SM * 4, START_Y + tools.BOTT_Y, 100, ollDraw.draw_u),
        }

    else:
        raise ValueError("Invalid stage")
    
    # generate rectangles
    # we can use the name, as well as x and y coordinates from whichever case_data dict above
    # we don't care about the function name here as it isn't relevant when drawing the rectangles
    case_rects = {
        name: pygame.Rect(x, y, tools.TOTAL_SM, tools.TOTAL_SM)
        for name, (x, y, _, _) in case_data.items()
    }

    # generate back button
    back_button = draw_back_button(surface)

    # main
    while True:
        clock.tick(30)
        surface.fill(tools.BLACK)

        # actually draw button, this is coming from the button class in startup.py
        back_button.draw(surface)

        if showing_case is None:
            text_surface = font.render(label_text, True, tools.WHITE)
            surface.blit(text_surface, (120, tools.LABEL_Y))

            for name, (x, y, _, draw_fn) in case_data.items():
                draw_fn(surface, x, y, 0, False)
        else:
            # show full-size selected case
            # where underscore means "don't care" and we can just grab the function
            _, _, alg_x, draw_fn = case_data[showing_case]
            draw_fn(surface, START_X, START_Y, alg_x, True)

        pygame.display.flip()

        # handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if showing_case is None:
                    for name, rect in case_rects.items():
                        if rect.collidepoint(event.pos):
                            showing_case = name
                            break
                if back_button.is_clicked(event.pos):   # "is_clicked" also comes from startup.py
                    return "menu"

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT:
                        return "round2" if stage == "round1" else "corner"
                    case pygame.K_LEFT:
                        return "round1" if stage == "round2" else "menu"
                    case pygame.K_ESCAPE:
                        showing_case = None