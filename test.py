import spacy


nlp= spacy.load("output/model-last")


ner = nlp.get_pipe("ner")
print(ner.labels)


text= "Casa de 4 ambientes en Lomas del Mirador.  Ubicada en Melo 836, Lomas del Mirador.  Lote de 8,66 x 23 Vivienda con 100 años de antigüedad aprox. (ideal modernizar o demoler) de 90 m2 Cubiertos  o Cocina. o Comedor. o Baño. o 3 Dormitorios. o Patio. o Terraza. o Galpón.  ZONIFICACION Zona: U2B FOS 0,6 FOT 2.25 Densidad 700 Altura Máxima 13 mts  Consultanos para coordinar una visita LUCERO Propiedades  - KP255930 - KPD110810 - -   Publicado vía KiteProp CRM Inmobiliario"
doc=nlp(text)
for ent in doc.ents:
   print(ent.text,ent.label_)


text= """Amplio PH de tres ambientes. Se encuentra ubicado en 5 entre 528 bis y 529.
"""
doc=nlp(text)
for ent in doc.ents:
   print(ent.text,ent.label_)


   
text= "637 entre 137 y 143. Lote de 27m x 150m, haciendo un total de 4050 m2. Barrio cerrado ya conformado compuesto por 9 lotes de diversas medidas. Su destino es para vivienda familiar. Cuenta con los servicios de luz y agua."
doc=nlp(text)
for ent in doc.ents:
   print(ent.text,ent.label_)
