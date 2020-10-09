import random
import math
from string import (Template, ascii_lowercase)


def letter_list():
    return [i for i in ascii_lowercase] + ["-"]


def haiku_template():
    return Template("""
    $l1s1$l1s2$l1s3$l1s4$l1s5
    $l2s1$l2s2$l2s3$l2s4$l2s5$l2s6$l2s7
    $l3s1$l3s2$l3s3$l3s4$l3s5
    """)


def random_word_length(line):
    if line != 2 and line in range(1, 4):
        return random.randint(1, 15)
    elif line == 2:
        return random.randint(1, 20)
    else:
        raise ValueError("line must be between 1 and 3")


def random_word_from_length(length):
    word = []
    for i in range(1, length+1):
        word.append(
            random.choice(
                letter_list()
            )
        )
    return "".join(word)


if __name__ == '__main__':
    print("HaikuGenerator v0.0.1")
    print(
        random_word_from_length(
            random_word_length(1)
        )
    )
