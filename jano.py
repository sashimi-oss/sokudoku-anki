# import sys

# args = sys.argv

from janome.tokenizer import Tokenizer

def keisotai_kaiseki (kotoba):


    t = Tokenizer()

    s = kotoba

    wakati = []

    for token in t.tokenize(s):
        print(token)
        wakati.append(token.surface)

    print(wakati)
    return wakati