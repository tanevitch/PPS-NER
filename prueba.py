import re
import spacy

numeros = re.findall(r'\b\d+(?:[.,]\d+)?\b', "LOTE CON MEJORAS (CASA A REFACCIONAR) 8,77 X 26,23 X 8,77 X 26,07")
numeros_sin_duplicados = set(numeros)
len(numeros_sin_duplicados)

nlp= spacy.load("output-merge/model-best")

text = "Casa de 4 ambientes en Lomas del Mirador.  Ubicada en Melo 836, Lomas del Mirador.  Lote de 8,66 x 23 Vivienda con 100 años de antigüedad aprox. (ideal modernizar o demoler) de 90 m2 Cubiertos  o Cocina. o Comedor. o Baño. o 3 Dormitorios. o Patio. o Terraza. o Galpón.  ZONIFICACION Zona: U2B FOS 0,6 FOT 2.25 Densidad 700 Altura Máxima 13 mts"

ents= nlp(text).ents
print(set([ent.text for ent in ents]))
ents
a = nlp("calle 13 C e/ 471").similarity(nlp("calle 13 C e/ 471 y 472")) 
a