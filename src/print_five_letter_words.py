import sys

n = len(sys.argv)
if n != 2:
    print("Use: python3 ./print_five_letter_words.py <input_file>")
    exit(1)

f = open(sys.argv[1])
line = f.readline()
while line:
    words = line.split()
    if len(words[0]) == 5:
        print(words[0])
    line = f.readline()
