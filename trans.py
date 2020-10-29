import os, sys
from pprint import pprint
import requests
# import time

from split_paragraphs import split_paragraphs
from tqdm import tqdm

from pdfminer.high_level import extract_text

from googletrans import Translator


translator = Translator()

def translate(text, src='en', dest='ja'):

    trans = translator.translate(text, src=src, dest=dest)

    return trans.text


def text_file_translate(text_file):

    name, ext = os.path.splitext(text_file)

    with open(f"{name}.txt", "r", encoding="utf-8") as f:

        lines = f.read()

    lines = lines.splitlines()

    paragraphs = split_paragraphs(lines)

    out = ''
    error_count = 0
    for paragraph in tqdm(paragraphs, desc="translate"):

        if len(paragraph) == 0:
            continue

        out += '\n\n'

        if paragraph[0] == "#":
            out += paragraph + '\n'

        else:

            try:
                out += translate(paragraph) + '\n'

            except:
                error_count += 1

                out += ":TranslatorExcept\n"
                out += paragraph + '\n'


    with open(f"{name}_trans.txt", "w", encoding="utf-8") as f:

        f.write(out)

    print(f"Done. (Raise {error_count} exceptions.)")
