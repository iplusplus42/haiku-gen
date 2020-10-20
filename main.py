import random
import os

DEBUG = False


class Utils:
    @staticmethod
    def is_palindrome(string):
        return string == string[::-1]

    @staticmethod
    def get_adjectives(syllable=1):
        adjectives = set()
        path = os.path.join(os.getcwd(), "words/adjectives")

        if syllable in range(1, 5):
            fd = open(os.path.join(path, f"{syllable}syllableadjectives.txt"))
            words = [i for i in fd.read().split("\n") if i != ""]
            adjectives.update({i for i in words})
        else:
            for i in os.listdir(path):
                fd = open(os.path.join(path, i), "r")
                words = [i for i in fd.read().split("\n") if i != ""]
                adjectives.update({i for i in words})
                fd.close()
        return adjectives

    @staticmethod
    def get_adverbs(syllable=1):
        adverbs = set()
        path = os.path.join(os.getcwd(), "words/adverbs")

        if syllable in range(1, 5):
            fd = open(os.path.join(path, f"{syllable}syllableadverbs.txt"))
            words = [i for i in fd.read().split("\n") if i != ""]
            adverbs.update({i for i in words})
        else:
            for i in os.listdir(path):
                fd = open(os.path.join(path, i), "r")
                words = [i for i in fd.read().split("\n") if i != ""]
                adverbs.update({i for i in words})
                fd.close()
        return adverbs

    @staticmethod
    def get_nouns(syllable=1):
        nouns = set()
        path = os.path.join(os.getcwd(), "words/nouns")

        if syllable in range(1, 5):
            fd = open(os.path.join(path, f"{syllable}syllablenouns.txt"))
            words = [i for i in fd.read().split("\n") if i != ""]
            nouns.update({i for i in words})
        else:
            for i in os.listdir(path):
                fd = open(os.path.join(path, i), "r")
                words = [i for i in fd.read().split("\n") if i != ""]
                nouns.update({i for i in words})
                fd.close()
        return nouns

    @staticmethod
    def get_verbs(syllable=1):
        verbs = set()
        path = os.path.join(os.getcwd(), "words/verbs")

        if syllable in range(1, 5):
            fd = open(os.path.join(path, f"{syllable}syllableverbs.txt"))
            words = [i for i in fd.read().split("\n") if i != ""]
            verbs.update({i for i in words})
        else:
            for i in os.listdir(path):
                fd = open(os.path.join(path, i), "r")
                words = [i for i in fd.read().split("\n") if i != ""]
                verbs.update({i for i in words})
                fd.close()
        return verbs

    @staticmethod
    def get_words(syllable=1):
        return random.choice([Utils.get_verbs, Utils.get_nouns, Utils.get_adverbs, Utils.get_adjectives])(syllable)

    @staticmethod
    def get_word(syllable=1):
        return random.choice(
            [i for i in random.choice(
                [Utils.get_verbs, Utils.get_nouns, Utils.get_adverbs, Utils.get_adjectives]
            )(syllable)]
        )


def debug(content):
    if DEBUG:
        print(content)


def haiku():
    line_1_syllables = 5
    line_2_syllables = 7
    line_3_syllables = 5
    temp = {"line1": "", "line2": "", "line3": ""}

    debug("Line 1")
    while line_1_syllables > 0:
        syllable = random.randint(1, 4 if line_1_syllables > 4 else line_1_syllables)
        debug(f"Remaining syllables: {line_1_syllables}")
        debug(f"Syllable: {syllable}")
        if syllable > line_1_syllables:
            continue
        word = Utils.get_word(syllable)
        debug(f"Word: {word}")
        temp["line1"] += f"{word} "
        line_1_syllables -= syllable

    debug("Line 2")
    while line_2_syllables > 0:
        syllable = random.randint(1, 4 if line_2_syllables > 4 else line_2_syllables)
        debug(f"Remaining syllables: {line_2_syllables}")
        debug(f"Syllable: {syllable}")
        if syllable > line_2_syllables:
            continue
        word = Utils.get_word(syllable)
        debug(f"Word: {word}")
        temp["line2"] += f"{word} "
        line_2_syllables -= syllable

    debug("Line 3")
    while line_3_syllables > 0:
        syllable = random.randint(1, 4 if line_3_syllables > 4 else line_3_syllables)
        debug(f"Remaining syllables: {line_3_syllables}")
        debug(f"Syllable: {syllable}")
        if syllable > line_3_syllables:
            continue
        word = Utils.get_word(syllable)
        debug(f"Word: {word}")
        temp["line3"] += f"{word} "
        line_3_syllables -= syllable

    return f"{temp['line1']}\n{temp['line2']}\n{temp['line3']}"


if __name__ == '__main__':
    print("HaikuGenerator v0.1.0")
    print(haiku())
