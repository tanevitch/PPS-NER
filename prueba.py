import re
import spacy


nlp= spacy.load("output-merge/model-best")

text = "Venta de lote en Flores, Capital Federal. GRAN PROYECTO INMOBILIARIO POSIBLE. Frente 8.66 x fondo 38.1 m2 en Flores CABA. USAA (C3II). Sobre Avenida Directorio esquina Avenida San Pedrito. Gran flujo vehicular y peatonal"

ents= nlp(text).ents
print(set([ent.text for ent in ents]))
ents
a = nlp("calle 13 C e/ 471").similarity(nlp("calle 13 C e/ 471 y 472")) 
a