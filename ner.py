import spacy


text= "LOTE No 26 DE 5.010 M2 - LO INVITAMOS A VISITARLO!! Lindisimo Departamento en Venta sobre la calle Sargento Cabral entre Cancilleria y Plaza San Martin. Son 183 Mts. Piso. Palier Privado. Hall de entrada. Living, comedor y Escritorio a balcon corrido. Tres dormitorios con tres baños completos. Cocina con buen comedor diario. Lavadero Independiente. Dependencia de Servicio. En Impecable estado, reciclado con muy buen gusto. Buenos Placards. Luminoso. Servicios Centrales. Baulera. Horario porteria con vivienda en el edificio + camaras de Seguridad. Es una cuadra Super Tranquila con poco transito en el medio de la Ciudad! FOT 3. Expensas $6.254 ABL 2016 $1.929 Vale la pena verlo!"

nlp= spacy.load("output/model-best")
doc=nlp(text)

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

