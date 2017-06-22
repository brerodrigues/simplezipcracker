#!/usr/bin/env python3

class ZipCracker(object):

    def __init__(self, zip_file, word_list=None):
        #self.zip_file = self.open_zip_file(zip_file)
        self.zip_file = zip_file
        self.word_list = self.open_word_list(word_list)

    def crack_zip(self, zip_file, wordlist):
        pass

    def open_word_list(self, word_list):
        wordlist_file = open(word_list, 'r')
        wordlist = wordlist_file.read().split('\n')
        return wordlist
