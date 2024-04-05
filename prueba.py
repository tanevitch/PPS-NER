import re
import spacy


nlp= spacy.load("output-merge/model-best")

text = "Lote con mejoras (casa a refaccionar) 8.77 x 26.23 + martillo, sup. total 226 mts2. Todos los servicios. FOS 0.6. FOT 1.6. Zonificación RTMA. Escritura a cargo del comprador."

ents= nlp(text).ents
print(set([ent.text for ent in ents]))
ents
a = nlp("calle 13 C e/ 471").similarity(nlp("calle 13 C e/ 471 y 472")) 
a