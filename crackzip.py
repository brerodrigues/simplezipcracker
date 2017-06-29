#!/usr/bin/env python3

import zipcracker
import sys

def main(argv):
    if len(argv) < 3:
        print('Usage: ./{} zip_file word_list'.format(str(argv[0])))
        return(False, 'Insufficient arguments')

    zip_file = argv[1]
    word_list = argv[2]

    zip_cracker = zipcracker.ZipCracker(zip_file, word_list)

    # checking if the objects attributes are ok
    if zip_cracker.zip_file[0] is False:
        print (zip_cracker.zip_file[1])
        return (False, zip_cracker.zip_file[1])

    if zip_cracker.word_list[0] is False:
        print (zip_cracker.word_list[1])
        return (False, zip_cracker.word_list[1])

    # Cracking the bad boy and storing the result
    cracking_result = zip_cracker.crack_zip()

    # Checking the results
    if cracking_result[0] is True:
        print ('Password is \'{}\''.format(cracking_result[1]))
        return (True, cracking_result[1])
    else:
        print ('Password not found')
        return (False, cracking_result[1])

if __name__ == '__main__':
    main(sys.argv)
