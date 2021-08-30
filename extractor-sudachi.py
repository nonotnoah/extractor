from sudachipy import dictionary 
from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary().create()

mode = tokenizer.Tokenizer.SplitMode.C

def parse_dictionary_form(text):
    m = tokenizer_obj.tokenize(text, mode)[0]
    return m.dictionary_form()

def parse(text):
    return [m.surface() for m in tokenizer_obj.tokenize(text, mode)]

digitsAndSpecial = "1234567890\'\",.?;:[]\{\}-=_+!@#$%^&*()<>/|"

def get(wordType):
    full_text = parse(text)
    type_words = []
    for word in full_text:
        type = [m.part_of_speech() for m in tokenizer_obj.tokenize(word, mode)]
        if wordType == '動詞' == type[0][0]:
            type_words.append(parse_dictionary_form(word))
        elif type[0][0] == wordType:
            type_words.append(word)
        
    words = [word for word in type_words if word not in filterlist and word not in digitsAndSpecial]

    return words

with open('analyze.txt', 'r', encoding='utf-8') as analyze:
    text = analyze.read()
    result = parse(text)
    print('Parsing: ', ''.join(result[:10]), '...', sep='') # print mecab results

with open('blank.txt', 'r', encoding='utf-8') as filterfile:  # utf-8 is important!
    ff_lines = filterfile.read()
    filterlist = ff_lines.split("\n")

nouns = get("名詞")
print("名詞", len(nouns), nouns)

adjectives = get("形容詞")
print("形容詞", len(adjectives), adjectives)

verbs = get("動詞")
print("動詞", len(verbs), verbs)

totalWords = len(nouns) + len(adjectives) + len(verbs)
print("合計:", totalWords)
