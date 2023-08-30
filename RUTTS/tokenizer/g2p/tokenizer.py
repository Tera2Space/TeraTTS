import re
from .g2p import *
import json
import os

class Tokenizer():
    def __init__(self, data_path: str) -> None:
        self.dic = {}
        for line in open(os.path.join(data_path, "dictionary.txt")):
           items = line.split()
           self.dic[items[0]] = " ".join(items[1:])

        self.config = json.load(open(os.path.join(data_path, "config.json")))
    
    def g2p(self, text):
        text = re.sub("—", "-", text)
        text = re.sub("([!'(),-.:;?])", r' \1 ', text)

        phonemes = []
        for word in text.split():
            if re.match("[!'(),-.:;?]", word):
                phonemes.append(word)
                continue

            word = word.lower()
            if len(phonemes) > 0: phonemes.append(' ')

            if word in self.dic:
                phonemes.extend(self.dic[word].split())
            else:
                phonemes.extend(convert(word).split())

        phoneme_id_map = self.config["phoneme_id_map"]
        phoneme_ids = []
        phoneme_ids.extend(phoneme_id_map["^"])
        phoneme_ids.extend(phoneme_id_map["_"])
        for p in phonemes:
            if p in phoneme_id_map:
                phoneme_ids.extend(phoneme_id_map[p])
                phoneme_ids.extend(phoneme_id_map["_"])
        phoneme_ids.extend(phoneme_id_map["$"])

        return phoneme_ids, phonemes
    
    def _get_seq(self, text: str) -> list[int]:
        seq = self.g2p(text)[0]
        return seq