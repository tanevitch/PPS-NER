import spacy


text= "Casa de 4 ambientes en Lomas del Mirador.  Ubicada en Melo 836, Lomas del Mirador.  Lote de 8,66 x 23 Vivienda con 100 años de antigüedad aprox. (ideal modernizar o demoler) de 90 m2 Cubiertos  o Cocina. o Comedor. o Baño. o 3 Dormitorios. o Patio. o Terraza. o Galpón.  ZONIFICACION Zona: U2B FOS 0,6 FOT 2.25 Densidad 700 Altura Máxima 13 mts  Consultanos para coordinar una visita LUCERO Propiedades  - KP255930 - KPD110810 - -   Publicado vía KiteProp CRM Inmobiliario"

nlp= spacy.load("output/model-last")
doc=nlp(text)

ner = nlp.get_pipe("ner")

# List the labels used by the NER model
ner_labels = ner.labels

for ent in doc.ents:
   print(ent.text,ent.label_)


# EN
# Lindisimo Departamento PERSON
# Venta sobre la PERSON
# Sargento Cabral PERSON
# Cancilleria GPE
# la Plaza FAC
# 183 CARDINAL
# Tres dormitorios GPE
# tres baños PERSON
# Cocina GPE
# buen comedor diario PERSON
# Lavadero Independiente WORK_OF_ART
# Dependencia de Servicio ORG
# En Impecable ORG
# reciclado ORG
# muy buen gusto PERSON
# Buenos Placards ORG
# Servicios Centrales ORG
# Baulera PERSON
# Horario porteria con vivienda PERSON
# el edificio + camaras de Seguridad. ORG
# Super Tranquila ORG
# el medio de la Ciudad PERSON
# Expensas ORG
# 6.254 MONEY
# 2016 DATE
# 1.929 MONEY
# verlo GPE


# ES
# Venta LOC
# Sargento Cabral PER
# Vecino LOC
# Cancilleria LOC
# Plaza San Martin LOC
# Son 183 Mts PER
# Piso PER
# Palier Privado PER
# Hall LOC
# Living MISC
# Escritorio PER
# Tres ORG
# Cocina MISC
# Lavadero Independiente PER
# Dependencia de Servicio ORG
# En Impecable estado MISC
# Buenos Placards LOC
# Luminoso MISC
# Servicios Centrales LOC
# Baulera LOC
# Horario PER
# Seguridad MISC
# Super Tranquila MISC
# Ciudad! LOC
# Vale LOC

