import os
import re

class Zettelreader:
    def __init__(self, path=r"C:\Users\Benja\Dropbox\Zettelkasten\02 - Archiv"):
        self.pattern = r'\[\^.*?\d{4}\]'
        self.path = path
        self.all_files = self.get_all_files()
        self.all_ids = self.get_all_ids()
        self.all_names = self.get_all_names()

    def get_all_files(self):
        return os.listdir(r"C:\Users\Benja\Dropbox\Zettelkasten\02 - Archiv")
    
    def get_all_ids(self):
        return [file[:12] for file in self.all_files]

    def get_all_names(self):
        return [file[13:-4] for file in self.all_files]

    def get_summary(self, id):
        for count, value in enumerate(self.all_ids):
            if value == id:
                break
        with open(self.path+"\\"+self.all_files[count], 'r') as file:
            data = file.readlines()
        for line in data:
            if line[0:3] == '###':
                return line[3:]

    def get_text(self, id):
        for count, value in enumerate(self.all_ids):
            if value == id:
                break
        with open(self.path+"\\"+self.all_files[count], 'r') as file:
            data = file.readlines()
        for count, line in enumerate(data):
            if line[0:3] == '###':
                start = count+2
            if re.search(self.pattern, line) != None:
                end = count
                return data[start:end]


# nein das nicht als klasse
class Outlinereader:
    def __init__(self, path):
        self.path=path
    
    def add_summrizes(self):
        text = []
        with open(self.path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            text.append(line)
            matches = re.findall(r"d{12}", line)
            if matches != None:
                for match in matches:
                    text.append()