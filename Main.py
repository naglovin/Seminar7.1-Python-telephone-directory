from os.path import exists
from CSV_creating import creating_file
from File_writing import writing_scv
from File_writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating_file()

writing_scv()
writing_txt()