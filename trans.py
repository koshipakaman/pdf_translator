# -*- coding: utf-8 -*-
import os
import sys
import traceback
import requests

from split_paragraphs import split_paragraphs
from tqdm import tqdm

from googletrans import Translator


class GoogleTranslator:

    def __init__(self, API_KEY=None, source='en', target='ja'):

        self.translator = Translator()
        self.source = source
        self.target = target

        # TODO: use API

    def __call__(self, text):

        trans = self.translator.translate(text, src=self.source, dest=self.target)
        return trans.text


class DeepLTranslator:

    def __init__(self, API_KEY=None, source='en', target='ja'):

        self.params = {
                'auth_key': API_KEY,
                'source_lang': source.upper(),
                'target_lang': target.upper(),
        }
        self.URL = "https://api.deepl.com/v2/translate"

    def __call__(self, text):

        self.params['text'] = text
        request = requests.post(self.URL, data=self.params)

        res = request.json()
        return res['translations'][0]['text']


engines = {
        'google': GoogleTranslator,
        'deepl': DeepLTranslator,
    }


def text_file_translate(text_file,
                        engine="google",
                        API_KEY=None,
                        source='en', target='ja'):

    name, ext = os.path.splitext(text_file)

    with open(f"{name}.txt", "r", encoding="utf-8") as f:

        lines = f.read()

    lines = lines.splitlines()

    paragraphs = split_paragraphs(lines)
    translate = engines[engine](API_KEY, source, target)

    out = ''
    error_count = 0

    for paragraph in tqdm(paragraphs, desc="translate"):

        if len(paragraph) == 0:
            continue

        elif paragraph[0] == "#":
            out += paragraph + '\n'

        else:

            try:
                out += translate(paragraph) + '\n'

            except Exception as e:

                traceback.print_exc()
                # print(paragraph)

                error_count += 1

                out += f"{type(e)}\n"
                out += paragraph + '\n'

            out += '\n\n'

    with open(f"{name}_trans.txt", "w", encoding="utf-8") as f:

        f.write(out)

    print(f"Done. (Raise {error_count} exceptions.)")


if __name__ == "__main__":

    translate = engines["google"]()
    print(translate("Published as a conference paper at ICLR 2019"))
