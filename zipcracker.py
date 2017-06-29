#!/usr/bin/env python3

import zipfile

class ZipCracker(object):

    def __init__(self, zip_file, word_list):
        self.zip_file = self.process_zip(zip_file)
        self.word_list = self.process_word_list(word_list)

    def crack_zip(self):
        # Checking if is everything ok with wordlist and zip
        if self.word_list[0] and self.zip_file[0] is True:
            word_list = self.word_list[1]
            zip_file = self.zip_file[1]
            for word in word_list:
                try:
                    zip_file.extractall(pwd=word.encode('utf-8'))
                # extractall() will raise a 'RuntimeError' exception if pwd
                # is incorrect, so i'm checking if 'Bad password' is found on
                # the exception to controll the flow
                except RuntimeError as e:
                    if 'Bad password' in str(e):
                        print('Tried the passowrd \'{}\' and failed'.format(word))
                # Ignoring others exceptions
                except:
                    pass
                else:
                    print('Tried the password \'{}\' and succeed!'.format(word))
                    return(True, word)
            # for ended, all words tested
            return(False, 'Password not found')
        else:
            return(False, 'Something is wrong with the zip or wordlist')

    def process_zip(self, zip_file_name):
        # Checks if is a valid zip using magic number and if is acessible
        if zipfile.is_zipfile(zip_file_name):
            # Creating object zipfile to make checks
            zip_file = zipfile.ZipFile(zip_file_name)
            # Trying to read the files
            try:
                # If testzip() returns something, the zip is damaged
                if zip_file.testzip() is not None:
                    return(False, '{} is damaged'.format(zip_file_name))
            # If testzip() raises a exception, check if 'encrypted' can
            # be found on the description
            except RuntimeError as e:
                if 'encrypted' in str(e):
                    return(True, zip_file)
                else:
                    return(False, '{} is not enctrypted'.format(zip_file_name))
        else:
            return(False, '{} is not a valid zip file or is not acessible'.format(zip_file_name))

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
