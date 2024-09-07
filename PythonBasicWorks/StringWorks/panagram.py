# write a program to print the given sentance is panagram or not
# panagram meas sentance contain all the english alphabets

word="the quick brown fox jumps over a lazy dog"

alphabet="abcdefghijklmnopqrstuvwxyz"

is_panagram=True

for char in alphabet:

    if word.count(char)==0:

        is_panagram=False

        break

print(is_panagram)
