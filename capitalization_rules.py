import nltk
import re

nnp_pattern = '[A-Z][a-zA-Z]+'
capital_pattern = '[A-Z][a-z]+'

def capitalize_rules(text):
    
    max_len = 4
    text = text.lower()
    morph = nltk.word_tokenize(text)

    # part of speech (hinshi)
    # [('Hi', 'NNP'), ..., ]
    pos = nltk.pos_tag(morph) 

    words = [ word.capitalize() for word in morph ]

    lower_pos_tag = [ 'IN', 'TO', 'DT', 'WDT']

    capitalized = []
    for i, (word, pos_tag) in enumerate(pos):
        if pos_tag in lower_pos_tag and len(word) <= max_len:
            capitalized.append(words[i].lower())

        else:
            capitalized.append(words[i])

    return " ".join(capitalized)
