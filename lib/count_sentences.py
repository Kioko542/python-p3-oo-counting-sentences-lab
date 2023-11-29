#!/usr/bin/env python3



import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        replaced_value = re.sub(r'[!?]', '.', self.value)
        sentences = [sentence for sentence in replaced_value.split('.') if sentence]
        return len(sentences)
