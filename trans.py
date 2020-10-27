import os, sys
from pprint import pprint
import argparse

from split_paragraphs import split_paragraphs
from tqdm import tqdm

from pdfminer.high_level import extract_text

from googletrans import Translator


def translate(text, src='en', dest='ja'):

    translator = Translator()
    trans = translator.translate(text, src=src, dest=dest)

    return trans.text


def text_file_translate(text_file):
    
    name, ext = os.path.splitext(text_file)

    with open(f"{name}.txt", "r") as f:

        lines = f.read()

    lines = lines.splitlines()

    paragraphs = split_paragraphs(lines)

    out = ''
    for paragraph in tqdm(paragraphs, desc="translate"):

        if len(paragraph) == 0:
            continue

        out += '\n\n'

        if paragraph[0] == "#":
            out += paragraph + '\n'

        else:
            out += translate(paragraph) + '\n'

    with open(f"{name}_trans.txt", "w") as f:

        f.write(out)
    

if __name__ == "__main__":
    
    # args = sys.argv
    # file_name = args[1]
    text_file_translate("pixelCNN_test.txt") 
