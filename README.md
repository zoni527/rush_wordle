# Wordle Rush Project
## Description
The task was to program an assistant program to help someone play
[Wordle](https://www.nytimes.com/games/wordle/index.html), a bot
that plays the game by itself, and a version of the game, if time
permitted, during two working days. I coded all three using Python.
## Prerequisites
- Python3
- Curses (not available on Windows by default)
## Installation & running
To run the projects all that is required is to clone this repository,
give the scripts execution privileges, and then run the desired script.
The scripts run the correct python source code from the source folder,
it would also be possible to feed the source directly to the python3
executable.

Example to run the game:
```bash
git clone https://github.com/zoni527/rush_wordle.git && cd rush_wordle
chmod +x wordle_game.sh
./wordle_game.sh
```
or alternatively using the source code:
```bash
python3 ./src/wordle_game.py
```
