print("Hello world")
f = open("./words_alpha.txt", "r")
print(f)
line = f.readline()
while len(line) != 0:
    # if len(line) == 6:
    #     print(line.rstrip())
    line = f.readline()
f.close()

f = open('./count_1w.txt')
print(f)
line = f.readline()
while len(line) != 0:
    words = line.split()
    if len(words[0]) == 5 and int(words[1]) > 150000:
        print(words[0], words[1])
    line = f.readline()
f.close()
