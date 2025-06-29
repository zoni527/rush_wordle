# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    word_list_analysis.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jvarila <jvarila@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/29 09:31:50 by jvarila           #+#    #+#              #
#    Updated: 2025/06/29 10:06:44 by jvarila          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import Counter

def main():

    total_char_freq = {}
    alphabet        = "abcdefghijklmnopqrstuvwxyz"

    f = open('word_lists/sgb-words.txt')
    all_text    = f.read()
    words       = all_text.split()
    words.sort()

    word_dict                   = {}
    words_with_n_unique_chars   = [0, 0, 0, 0, 0]
    words_without_letter         = {}

    for word in words:
        word_dict[word] = {}
        word_dict[word]["unique chars"] = len(set(word))
        word_dict[word]["char freq"] = {}

        for c in word:
            char_freq = word_dict[word]["char freq"]
            if c not in total_char_freq:
                total_char_freq[c] = 1
            else:
                total_char_freq[c] += 1
            if c not in char_freq:
                char_freq[c] = 1
            else:
                char_freq[c] += 1
        words_with_n_unique_chars[len(set(word)) - 1] += 1

        for c in alphabet:
            if c not in word:
                if c not in words_without_letter:
                    words_without_letter[c] = 1
                else:
                    words_without_letter[c] += 1


    print(word_dict)
    print(words_with_n_unique_chars)
    total_char_freq_sorted = dict(sorted(total_char_freq.items()))
    print(total_char_freq_sorted)
    words_without_letter_sorted = dict(sorted(words_without_letter.items()))
    print(words_without_letter_sorted)

main()
