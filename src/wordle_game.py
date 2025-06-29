# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    wordle_game.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jvarila <jvarila@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/29 17:02:01 by jvarila           #+#    #+#              #
#    Updated: 2025/06/29 18:05:28 by jvarila          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import curses

game_grid = """\
┌───┬───┬───┬───┬───┐
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
└───┴───┴───┴───┴───┘"""

grid_lines = game_grid.splitlines()
grid_h = len(grid_lines)
grid_w = len(grid_lines[0])

def center_line(window, line):

    height, width = window.getmaxyx()
    y = height // 2 - height % 2
    x = (width // 2) - len(line) // 2 - len(line) % 2
    return y, x

def draw_game_grid(window):

    y, x = get_grid_drawing_start_cursor_position(window)
    for line in grid_lines:
        window.addstr(y, x, line)
        y += 1
    window.refresh()

def get_grid_drawing_start_cursor_position(window):

    height, width = window.getmaxyx()
    grid_yo = (height // 2) - grid_h // 2 - grid_h % 2
    grid_xo = (width // 2) - grid_w // 2 - grid_w % 2
    if (grid_yo < 0):
        grid_yo = 0
    if (grid_xo < 0):
        grid_xo = 0
    return grid_yo, grid_xo

def draw_full_screen_message(window, text):

    height, width = window.getmaxyx()
    window.erase()
    window.border()
    text_y, text_x = center_line(window, text)
    window.addstr(text_y, text_x, text)
    window.refresh()

def draw_exit_message(window):

    exit_msg = "Press (capital) Q to exit"
    exit_msg_y, exit_msg_x = center_line(window, exit_msg)
    exit_msg_y = 1
    window.addstr(exit_msg_y, exit_msg_x, exit_msg)
    window.refresh()

def main(stdscr):

    f           = open('word_lists/sgb-words.txt')
    all_text    = f.read()
    f.close()
    words       = all_text.split()
    words.sort()
    solution    = random.choice(words)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()

    height, width = stdscr.getmaxyx()
    if (grid_h > height or grid_w > width):
        exit(1)

    # Start screen
    curses.curs_set(0)
    draw_full_screen_message(stdscr, "Wordle by jvarila")
    stdscr.move(0, 0)
    stdscr.getkey()

    # Draw game grid on screen
    draw_game_grid(stdscr)

    # First square position
    grid_yo, grid_xo = get_grid_drawing_start_cursor_position(stdscr)
    cursor_y = grid_yo + 1
    cursor_x = grid_xo + 2

    draw_exit_message(stdscr)

    # Game loop
    guess_count = 0
    while guess_count < 6: #{

        # Small guard in case of window resize, but not very effective,
        # shit might still blow up
        height, width = stdscr.getmaxyx()

        # Collect user input
        guess = ""
        cursor_x = grid_xo + 2
        while guess not in words: #{
            guess = ""
            stdscr.move(cursor_y, cursor_x)
            curses.curs_set(1)
            i = 0
            while i < 5:
                c = chr(stdscr.getch())
                if c == 'Q':
                    exit(0)
                # Make sure character is ok (implement backspace later, maybe enter)
                while not c.islower() or not c.isascii():
                    c = chr(stdscr.getch())
                guess += c
                stdscr.addch(c)
                stdscr.refresh()
                cursor_x += 4
                stdscr.move(cursor_y, cursor_x)
                i += 1
            curses.curs_set(0)
            stdscr.addstr(1, 2, " " * (width - 5))
            stdscr.addstr(1, 2, "Guess: {0}".format(guess))
            draw_exit_message(stdscr)

            stdscr.addstr(height - 2, 2, " " * (width - 5))
            if guess not in words:
                stdscr.addstr(height - 2, 2, "Guess {0} not in word list".format(guess))
                # Jump back and clear squares
                while i > 0:
                    cursor_x -= 4
                    stdscr.move(cursor_y, cursor_x)
                    stdscr.addch(' ')
                    i -= 1
        #}
        guess_count += 1
        stdscr.refresh()

        # Detect win
        if guess == solution:
            draw_full_screen_message(stdscr, "You won! Press any key to exit")
            stdscr.getkey()
            exit(0)

        # Color the letters
        for i in range(5):
            cursor_x = grid_xo + 2 + i * 4
            stdscr.move(cursor_y, cursor_x)
            if guess[i] == solution[i]:
                stdscr.addch(guess[i], curses.color_pair(1))
            elif guess[i] in solution:
                stdscr.addch(guess[i], curses.color_pair(2))
            else:
                stdscr.addch(guess[i], curses.color_pair(3))

        # Move to the next row
        cursor_y += 2
    #}

    # Lost the game
    draw_full_screen_message(stdscr, "You ran out of guesses, you are dead" +
                             " (the right answer was {0} btw)".format(solution))
    curses.curs_set(0)
    stdscr.getkey()
    exit(0)

curses.wrapper(main)
