import random
import os

BASE_DIR = os.path.dirname(__file__)

def generate_funny_name(adjectives=[], nouns=[]):
    if adjectives and nouns:
        pass

    adjective_path = os.path.join(BASE_DIR, 'words', 'adjectives.txt')
    nouns_path = os.path.join(BASE_DIR, 'words', 'nouns.txt')

    with open(adjective_path) as adjective_f, open(nouns_path) as nouns_f:

        adjectives = [adjective.strip('\n') for adjective in adjective_f]
        nouns = [noun.strip('\n') for noun in nouns_f]

    funny_name = "{adjective} {noun}".format(adjective=random.choice(adjectives), noun=random.choice(nouns))

    return funny_name
