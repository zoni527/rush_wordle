# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    wordle_bot_basic.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jvarila <jvarila@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/28 12:10:28 by jvarila           #+#    #+#              #
#    Updated: 2025/06/29 11:29:50 by jvarila          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import readline
import random

guesses         = []
invalid_chars   = set()
yellow_chars    = set()
green_chars     = list('_____')
output_columns  = 12

class C:
    # Bold high intensity
    B_HI_BL     = "\033[1;90m\001"
    B_HI_R      = "\033[1;91m\001"
    B_HI_G      = "\033[1;92m\001"
    B_HI_Y      = "\033[1;93m\001"
    B_HI_B      = "\033[1;94m\001"
    B_HI_P      = "\033[1;95m\001"
    B_HI_C      = "\033[1;96m\001"
    B_HI_W      = "\033[1;97m\001"
    # Reset
    RST         = "\033[0m\002"

# ---------------------------------------------------------------------------- #

def main():

    f           = open('word_lists/sgb-words.txt')
    all_text    = f.read()
    f.close()
    words       = all_text.split()
    words.sort()

    valid_words = words
    guess_count = 0
    solution    = random.choice(words)

    while guess_count < 6:

        valid_words = filtered_list(valid_words, invalid_chars, yellow_chars, green_chars)
        if len(valid_words) == 0:
            exit(1)

        guess = random.choice(valid_words)
        guess_count += 1

        if guess == solution:
            print("The program guessed the word {0}, which is correct!".format(guess))
            print(C.B_HI_G + "\nCongratulations!" + C.RST)
            print("Bye!")
            exit(0)

        guesses.append(guess)

        for i in range(5):
            if guess[i] == solution[i]:
                green_chars[i] = guess[i]
            elif guess[i] in solution:
                yellow_chars.add(guess[i])
            else:
                invalid_chars.add(guess[i])

    print("Out of guesses, " + C.B_HI_R + "you are dead" + C.RST)
    print("Bye!")
    exit(1)

# ---------------------------------------------------------------------------- #

def filtered_list(words, banned, required, filter):
    new_list = []
    for word in words:
        if still_valid(word):
            new_list.append(word)
    return new_list

def still_valid(word):
    if contains_character_in_set(word, invalid_chars):
        return False
    elif not contains_all_characters_in_set(word, yellow_chars):
        return False
    elif not matches_filter(word, green_chars):
        return False
    for g in guesses:
        if not contains_character_in_set(g, yellow_chars):
            continue
        for i in range(5):
            if (g[i] in yellow_chars
                    and green_chars[i] != g[i]
                    and word[i] == g[i]):
                return False
    return True

def contains_character_in_set(word, charset):
    if len(charset) == 0:
        return False
    if any((c in charset) for c in word):
        return True
    else:
        return False

def contains_all_characters_in_set(word, charset):
    for c in charset:
        if c not in word:
            return False
    return True

def matches_filter(word, filter):
    for i in range(5):
        if filter[i].islower():
            if word[i] != filter[i]:
                return False
    return True

def print_words(words):
    i = 1
    for word in words:
        print(word, end='   ')
        if i % output_columns == 0:
            print()
        i += 1
    if (i - 1) % output_columns != 0:
        print()
    print()

def contains_non_lowercase_char(word):
    if any((not c.islower()) for c in word):
        return True
    else:
        return False

main()
