#!/usr/bin/env python3

import zipfile

class ZipCracker(object):

    def __init__(self, zip_file, word_list):
        self.zip_file = self.process_zip(zip_file)
        self.word_list = self.process_word_list(word_list)

    def crack_zip(self, zip_file, wordlist):
        pass

    def process_zip(self, zip_file):
        if zipfile.is_zipfile(zip_file):
            return(True, zip_file)
        else:
            return(False, '{} is not a valid zip file!'.format(zip_file))

    def process_word_list(self, word_list):
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
