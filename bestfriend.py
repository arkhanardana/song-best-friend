import sys
from time import sleep

def print_lyrics():
    lines = [
        ("And that's because I wanna be your favorite boy", 0.10),
        ("I wanna be the one that makes your day", 0.08),
        ("The one you think about as you lie awake", 0.08),
        ("I can't wait to be your number one", 0.11),
        ("I'll be your biggest fan and you'll be mine", 0.07),
        ("But I still wanna break your heart and make you cry", 0.07),
    ]

    delay = [1.2, 0.9, 1.1, 1.4, 0.1, 0.9]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delay[i])
        print("")

print_lyrics()
