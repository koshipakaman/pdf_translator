import os, sys
from pprint import pprint
import argparse

from split_paragraphs import split_paragraphs, labeling, save_paragraphs
from tqdm import tqdm

from pdfminer.high_level import extract_text

from trans import translate, text_file_translate

args = sys.argv
file_name = args[1]

pdf_path = os.path.expanduser("~/Dropbox/research/trans/main")

# parser = argparse.ArgumentParser()
# args = parser.parse_arg()

name, ext = os.path.splitext(file_name)

if ext == ".pdf":

    text = extract_text(f"{pdf_path}/{file_name}")

    # preprocess
    lines = text.splitlines()
    lines = labeling(lines)
    paragraphs = split_paragraphs(lines)
    save_paragraphs(paragraphs, f"{pdf_path}/{name}.txt")
    print(f"Saved {pdf_path}/{name}.txt")

    print("Do you want to continue translating? [y/n] > ")

    while True:

        yn = input()

        if yn == "y": 
            text_file_translate(f"{pdf_path}/{name}.txt")
            break

        elif yn == "n":
            exit("Done.")
            break

        else:
            print("require [y/n].")

elif ext == ".txt":
    text_file_translate(f"{pdf_path}/{file_name}")

else:
    raise Exception(f"{ext} file is not required.")
