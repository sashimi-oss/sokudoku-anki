from janome.tokenizer import Tokenizer

t = Tokenizer()

s = "Pythonの基礎を学びたい方"

wakati = []

for token in t.tokenize(s):
  print(token)
  wakati.append(token.surface)

print(wakati)


# from janome.tokenizer import Tokenizer

# t = Tokenizer()

# token = t.tokenize('走れ').__next__()

# print(type(token))
# # <class 'janome.tokenizer.Token'>

# print(token.surface)

# x = []

# x.append(token.surface)
# print(x)
