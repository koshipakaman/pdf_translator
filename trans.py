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

            except AttributeError:
                error_count += 1
                
                out += ":AttributeError\n"
                out += paragraph + '\n'

    with open(f"{name}_trans.txt", "w", encoding="utf-8") as f:

        f.write(out)

    print(f"Done. (Raise {error_count} exceptions.)")
