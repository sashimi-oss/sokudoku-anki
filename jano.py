# import sys

# args = sys.argv


def keisotai_kaiseki (kotoba):

    from janome.tokenizer import Tokenizer

    t = Tokenizer()

    s = kotoba

    wakati = []

    for token in t.tokenize(s):
        print(token)
        wakati.append(token.surface)

    print(wakati)
    return wakati