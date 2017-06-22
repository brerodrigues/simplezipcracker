#!/usr/bin/env python3

import string
import random

class ZipCracker(object):

    def __init__(self, zip_file, word_list=None):
        #self.zip_file = self.open_zip_file(zip_file)
        self.zip_file = zip_file
        self.word_list = self.open_word_list(word_list)

    def crack_zip(self, zip_file, wordlist):
        pass

    def create_word_list(file_name, min_lenght, max_lenght, max_words):
        pass

    def open_word_list(self, wordlist):
        pass
