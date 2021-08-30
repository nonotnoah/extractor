from sudachipy import dictionary 
from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary().create()

mode = tokenizer.Tokenizer.SplitMode.C

def parse(word):
    m = tokenizer_obj.tokenize(word, mode)

parse("国家公務員")