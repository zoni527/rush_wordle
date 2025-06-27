# Wordle Rush: initial plan

## Strategies

- Guess common words
- Random guesses
    - Naive approach, guess completely randomly, check which
    words are still valid, guess again
- Use words with large letter coverage to filter out a lot of other words
    - How to narrow down most effectively
        - Words with the largest coverage
            - 5 different letters
        - Combinations of words with large combined coverage
            - Consonant-vowel balance
    - Check common letters or uncommon letters?
        - If an uncommon letter would hit it would narrow down the list very effectively

If the word has uncommon letters it narrows down the list of words faster

- Word pairs with 10 different letters
- Three words that cover the largest part of the alphabet
- Four or five words that cover the largest part of the alphabet
    - max 25 letters

## Possible program logic

1. suggest possible words
    - different orders
        - frequency
        - alphabetical
        - type
        - coverage
2. select a five letter word to be used ass a guess
3. if guess isn't correct: narrow down next guess
    - remove words with letters that aren't in the word
    - remove words that don't have letters in the required positions
4. if n_guesses < 6 -> repeat from 1, else you have lost

## Questions

- Are names ok words?
    - At least one online version suggests so
- Plurals ok?
    - Again, seems so
- Any way to remove words from the list that are not part of the game?
    - Can I automatically test the words as inputs to the game and then validate/invalidate them?

## Tasks

- Create most extensive list of 5 letter words, ordered alphabetically, all lower caps
- Create function to filter out words that don't contain a letter/many letters
- Create function to filter out words that don't contain a letter at the right spot
- Mine more words
