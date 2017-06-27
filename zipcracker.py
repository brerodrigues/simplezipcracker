#!/usr/bin/env python3

import zipfile

class ZipCracker(object):

    def __init__(self, zip_file, word_list):
        #self.zip_file = self.open_zip_file(zip_file)
        self.zip_file = zip_file
        self.word_list = self.open_word_list(word_list)

    def crack_zip(self, zip_file, wordlist):
        pass

    def open_zip(self, zip_file):
        pass

    def open_word_list(self, word_list):
        try:
            wordlist_file = open(word_list, 'r')
        except FileNotFoundError:
            return(False, 'File {} not found!'.format(word_list))
        except PermissionError:
            return(False, 'You don\'t have permission to read the file {}'.format(word_list))
        #Letting other expections happen for test purposes
        #except:
        #    return(False, 'Unknow error when opening the {} file'.format(word_list))
        else:
            wordlist = wordlist_file.read().split('\n')
            return (True, wordlist)
