from konlpy.tag import Okt
from typing import OrderedDict

okt = Okt()

dotdotdot = '...'
digitsAndSpecialStr = "\'\",.?;:[]\{\}-=_+!@#$%^&*()<>/|… "
digitsAndSpecial = [item for item in digitsAndSpecialStr]

def get(wordType, text):
    full_text = okt.pos(text)
    type_words = []
    for word in full_text:
        if word[0] not in digitsAndSpecial and dotdotdot:
            try: # remove numbers
                int(word)
                # print('bad character', word)
                continue
            except:
                try:
                    type = word[1]
                    if type == wordType:
                        type_words.append(word[0])
                except:
                    # print('no good, coach')
                    continue
        
    all_words = [word for word in type_words if word not in filterlist]
    words = list(OrderedDict.fromkeys(all_words))

    return words

with open('utils/text/blank.txt', 'r', encoding='utf-8') as filterfile:  # utf-8 is important!
    ff_lines = filterfile.read()
    filterlist = ff_lines.split("\n")
    
