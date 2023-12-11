import spacy
from spacy.tokens import DocBin
import json
from sklearn.model_selection import train_test_split
from spacy.util import filter_spans

def cargar_archivos():
    my_json = { "classes": [
            "FOT",
            "DIR_CALLE_ALTURA",
            "DIR_INTERSECCION",
            "DIR_ENTRE",
            "DIR_OTROS",
            "DIMENSIONES",
            "NOMBRE_BARRIO",
            "CANT_FRENTES",
            "IRREGULAR",
            "DIR_LOTE"
        ], "annotations": []}
    files = ['anotaciones1y2.json', 'anotaciones3.json', 'anotaciones4.json', 'anotaciones5.json', 'anotaciones_entre.json']
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            my_json["annotations"] += json.load(f)["annotations"]
    
    with open("anotaciones.json", 'w', encoding='utf-8') as f:
        json.dump(my_json,f, ensure_ascii=False)
    return my_json


def entrenar(data, filename: str):
    nlp = spacy.blank("es")

    db = DocBin()

    for text, annotations in data:
        doc = nlp(text)
        ents = []
        for start, end, label in annotations["entities"]:
            
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                print(msg)
            else:
                ents.append(span)

        filtered_ents = filter_spans(ents)
        doc.ents = filtered_ents
        db.add(doc)
    db.to_disk("./"+filename+".spacy")


def particionar(data):
    # entrenar(data["annotations"], "train_data")
    train, test = train_test_split(data["annotations"], test_size=0.2)
    entrenar(train, "train_data")
    entrenar(test, "test_data")

cargar_archivos()
train_data= json.load(open("anotaciones.json", 'r', encoding='utf-8'))
particionar(train_data)



