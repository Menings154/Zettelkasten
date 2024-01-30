import re

import reader
import datastructure


def load_Zettel():
    Zettelkasten = reader.Zettelreader()
    all_Zettel = [datastructure.Zettel(id=value,
                                       name=Zettelkasten.all_names[count],
                                       summary=Zettelkasten.get_summary(id=value),
                                       text=Zettelkasten.get_text(id=value))
                                        for count, value in enumerate(Zettelkasten.all_ids)]
    return Zettelkasten, all_Zettel

def go_through_outline(path, function):
    new_text = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_text.append(line)
            matches = re.findall(r'\d{12}', line)
            for match in matches:  # besser hier die tabs einfügen
                new_text.append(function(id=match))
    
    new_path = path[:-4]+function.__name__[3:]+'.txt'
    tab = 0
    with open(new_path, "w") as new_file:
        for line in new_text:
            if type(line) == str:  # will ich ds machen oder will ich lieber 2 Funktionen draus machen?
                try:
                    new_file.write(tab*"\t"+line)
                except TypeError:
                    new_file.write(tab*"\t"+"NO "+function.__name__[4:].upper()+"\n")  
                    tab=0
                    continue
            elif type(line) == list:
                for item in line:
                    matches = re.findall(r'\d{12}', item)
                    for match in matches:
                        temp = function(id=match)
                        if temp!=None:
                            item = item.replace(match, '['+' '.join(temp)+']')
                        new_file.write(tab*"\t"+item)
            
            try:
                tab = len(re.findall(pattern=r'\t', string=line))
                if tab>0:
                    tab+=1
            except TypeError:
                pass
    
    print("New file with the name: ", new_path)

Zettelkasten, all_Zettel = load_Zettel()
#go_through_outline(path=r"C:\Users\Benja\Dropbox\Zettelkasten\03 - Buffer\Lernen.txt", 
#                   function=Zettelkasten.get_summary)
go_through_outline(path=r"C:\Users\Benja\Dropbox\Zettelkasten\03 - Buffer\test\Lernen_summary.txt", 
                   function=Zettelkasten.get_text)