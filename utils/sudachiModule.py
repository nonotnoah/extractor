from typing import OrderedDict
from sudachipy import dictionary 
from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary().create()

mode = tokenizer.Tokenizer.SplitMode.C

def parse_dictionary_form(text):
    m = tokenizer_obj.tokenize(text, mode)[0]
    return m.dictionary_form()

def parse(text):
    return [m.surface() for m in tokenizer_obj.tokenize(text, mode)]

dotdotdot = '...'
digitsAndSpecialStr = "\'\",.?;:[]\{\}-=_+!@#$%^&*()<>/|… "
digitsAndSpecial = [item for item in digitsAndSpecialStr]

def get(wordType, text):
    full_text = parse(text)
    type_words = []
    for word in full_text:
        if word not in digitsAndSpecial and dotdotdot:
            try: # remove numbers
                int(word)
                # print('bad character', word)
                continue
            except:
                try:
                    type = [m.part_of_speech() for m in tokenizer_obj.tokenize(word, mode)]
                    if wordType == '動詞' == type[0][0]: # get dictionary form if word is verb
                        type_words.append(parse_dictionary_form(word))
                    elif type[0][0] == wordType:
                        type_words.append(word)
                except:
                    # print('no good, coach')
                    continue
        
    all_words = [word for word in type_words if word not in filterlist]
    words = list(OrderedDict.fromkeys(all_words))

    return words

with open('utils/text/blank.txt', 'r', encoding='utf-8') as filterfile:  # utf-8 is important!
    ff_lines = filterfile.read()
    filterlist = ff_lines.split("\n")
    