from gruut import sentences
import os
import re

class Tokenizer():
    def __init__(self, path) -> None:
        with open(os.path.join(path, "vocab.txt"), "r", encoding="utf-8") as vocab_file:
            self.symbols = vocab_file.read().split("\n")
            self.symbols = list(map(chr, list(map(int, self.symbols))))
            
        self.symbol_to_id = {s: i for i, s in enumerate(self.symbols)}
        
    def _ru_phonems(self, text: str) -> str:
        text = text.lower()
        phonemes = ""
        for sent in sentences(text, lang="ru"):
            for word in sent:
                if word.phonemes:
                    phonemes += "".join(word.phonemes)
        phonemes = re.sub(re.compile(r'\s+'), ' ', phonemes).lstrip().rstrip()
        return phonemes
    
    
    def _text_to_sequence(self, text: str) -> list[int]:
        '''convert text to seq'''
        sequence = []
        clean_text = self._ru_phonems(text)
        for symbol in clean_text:
            symbol_id = self.symbol_to_id[symbol]
            sequence += [symbol_id]
        return sequence
    
    
    def _get_seq(self, text: str) -> list[int]:
        seq = self._text_to_sequence(text)
        return seq