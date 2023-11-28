import spacy
from spacy.tokens import DocBin
import json
from sklearn.model_selection import train_test_split

def cargar_archivos():
    json_array = []
    files = ['anotaciones/archivo_1.json', 'anotaciones/archivo_11.json', 'anotaciones/archivo_21.json', 'anotaciones/archivo_31.json', 'anotaciones/archivo_41.json']
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            json_array.append(data)

    merged_dict = {}
    for json_dict in json_array:
        merged_dict.update(json_dict)
    json.dump(json_array, open("anotaciones.json", "w") )
    return merged_dict


def entrenar(data, filename: str):
    nlp = spacy.blank("es")

    db = DocBin()
    try:
        for text, annotations in data:
            doc = nlp(text)
            ents = []
            for start, end, label in annotations["entities"]:
                span = doc.char_span(start, end, label=label)
                ents.append(span)
            doc.ents = ents
            db.add(doc)
    except: 
        pass
    db.to_disk("./"+filename+".spacy")


def particionar(data):
    train, test = train_test_split(data["annotations"], test_size=0.2)
    entrenar(train, "train_data")
    entrenar(test, "test_data")


train_data= json.load(open("textos_1.json", 'r', encoding='utf-8'))
particionar(train_data)


