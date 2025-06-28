# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    wordle_assistant.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jvarila <jvarila@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/28 12:10:28 by jvarila           #+#    #+#              #
#    Updated: 2025/06/28 18:17:41 by jvarila          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import readline

guesses         = []
invalid_chars   = set()
yellow_chars  = set()
green_chars     = list('_____')
output_columns  = 12

# ---------------------------------------------------------------------------- #
def main():

    f = open('./all_mined_words_alphabetical_order.txt')
    all_text = f.read()
    words = all_text.split()

    while True:

        valid_words = filtered_list(words, invalid_chars, yellow_chars, green_chars)
        if len(valid_words) == 0:
            print("There are no more valid words, you'll have to be creative!")
            print("Bye!")
            exit(0)
        print("Currently there are {0} valid words".format(len(valid_words)))
        user_input = str(input("Do you want to print them? (y/n) > ")).lower()
        if user_input[0] == 'y':
            print_words(valid_words)
        elif user_wants_to_exit(user_input):
            exit(0)

        guess = str(input("Enter a guess > ")).lower()
        while True:
            if user_wants_to_exit(guess):
                exit(0)
            if len(guess) != 5:
                print("Error: length of input is {0}, needs to be 5".format(len(guess)))
                guess = str(input("Enter a guess > ")).lower()
                continue
            elif contains_non_lowercase_char(guess):
                print("Error: word contains invalid character")
                guess = str(input("Enter a guess > ")).lower()
                continue
            break
        guesses.append(guess)

        user_input = str(input("Was the guess correct? (y/n) > ")).lower()
        if user_input[0] == 'y':
            print("Congratulations! Goodbye!")
            break
        elif user_wants_to_exit(user_input):
            exit(0)

        print("Mark green characters with g and yellow characters with y")
        print("    " + guess)
        user_input = str(input("    _____\r  > ")).lower()
        if user_wants_to_exit(guess):
            exit(0)
        if len(user_input) < 5:
            user_input += "_____"
        for i in range(5):
            if user_input[i] == 'y':
                yellow_chars.add(guess[i])
            elif user_input[i] == 'g':
                green_chars[i] = guess[i]

        for c in guess:
            if c not in yellow_chars and c not in green_chars:
                invalid_chars.add(c)

        print("Guesses: {0}".format(guesses))
        print("Yellow characters: {0}".format(yellow_chars))
        print("Invalid characters: {0}".format(invalid_chars))
        print("Green characters: {0}".format(green_chars))

    f.close()

# ---------------------------------------------------------------------------- #

def filtered_list(words, banned, required, filter):
    new_list = []
    for word in words:
        if still_valid(word):
            new_list.append(word)
    return new_list

def still_valid(word):
    if contains_character_from_charset(word, invalid_chars):
        return False
    elif not contains_all_characters_from_charset(word, yellow_chars):
        return False
    elif not matches_filter(word, green_chars):
        return False
    for g in guesses:
        if not contains_character_from_charset(g, yellow_chars):
            continue
        for i in range(5):
            if (g[i] in yellow_chars
                    and green_chars[i] != g[i]
                    and word[i] == g[i]):
                return False
    return True

def contains_character_from_charset(word, charset):
    if len(charset) == 0:
        return False
    if any((c in charset) for c in word):
        return True
    else:
        return False

def contains_all_characters_from_charset(word, charset):
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

def user_wants_to_exit(user_input):
    match user_input:
        case "exit" | "stop" | "quit" | "q":
            return True
    return False

main()
