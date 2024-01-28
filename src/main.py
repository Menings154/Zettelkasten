import reader
import datastructure


def load_Zettel():
    Zettelkasten = reader.Zettelreader()
    all_Zettel = [datastructure.Zettel(id=value,
                                       name=Zettelkasten.all_names[count],
                                       summary=Zettelkasten.get_summary(id=value),
                                       text=Zettelkasten.get_text(id=value))
                                        for count, value in enumerate(Zettelkasten.all_ids)]
    print("finished")

load_Zettel()