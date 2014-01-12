#/usr/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader
import sys
from collections import OrderedDict
from letters import Letter

# TODO: argparse (file name, language?, etc.)


def get_PDF_content(path):
    content = ""
    # Load PDF into pyPDF
    pdf = PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content


def display_format(value):
    return str(format(value, '.2f'))


def display_thresholds(dictionnary):
    cpt = 0
    for key, letter in dictionnary.iteritems():
        cpt += letter.cpt
    print str(cpt) + " notes analysees"

    for key, letter in dictionnary.iteritems():
        print key + " (" + str(letter.cpt) + "):" ,
        if letter.cpt > 1:
            print "[" + display_format(letter.min) + " , " + display_format(letter.max) + "]"
        elif letter.cpt == 1:
            print "[" + display_format(letter.min)+"]"
        else:
            print "-"


def main(argv):
    file_name = argv[1]
    if file_name.split(".")[-1] == "txt":
        with open(file_name, 'r') as content_file:
            file_content = content_file.read()
    elif file_name.split(".")[-1] == "pdf":
        file_content = get_PDF_content(file_name).encode("utf8", "ignore")

    dict_letters = OrderedDict()
    for letter_value in ['A*', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']:
        dict_letters.update({letter_value: Letter(letter_value)})

    for i in range(len(file_content)):
        for key, letter in dict_letters.iteritems():
            search_string = " " + letter.letter_value + " "

            if file_content[i:i+len(search_string)] == search_string:
                while file_content[i] != "|":
                    i += 1
                i += 1

                grade_str = ""
                while file_content[i] != "|":
                    grade_str += file_content[i]
                    i += 1

                letter.check_extrema(float(grade_str))

                letter.cpt += 1

    display_thresholds(dict_letters)

if __name__ == "__main__":
        main(sys.argv)