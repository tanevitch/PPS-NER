import spacy


nlp= spacy.load("output/model-last")


ner = nlp.get_pipe("ner")
print(ner.labels)

text="Parque Industrial Cañuelas - Lote 9300 m2 (son 2 de 4650 m2 c/u) - Apto industrias categoría I, II y III.  El Parque cuenta con 200 hectáreas desarrolladas en dos etapas, la primera -de 100 hectáreas- totalmente finalizada, con escrituración inmediata.   - Retiros: frente 10 m, fondo 10 m (lotes perimetrales 5 m), laterales 5 m - FOS 0.6 y FOT 1.2 - Calles internas pavimentadas, aptas para tránsito pesado - Energía eléctrica de media tensión, tendido con columnas - Servicios de telecomunicaciones por fibra óptica (telefonía, banda ancha, etc) - Desagues: cuneta para pluviales con colección e industriales por conductos subterráneos - Balanza para camiones de hasta 80 toneladas - Helipuerto - Seguridad privada, control de accesos - Cerco perimetral de 2m de altura y forestación de banda perimetral de 15m de ancho - Gas natural con un tendido de 4 y una presión de 45kg/cm2 de entrada al parque, con distribución en media presión de 4Kg/cm2 en la red interna - Alumbrado general - Oficinas de recepción y administración - Estacionamiento - Estacionamiento para camiones en tránsito - Servicios del Banco de la Provincia de Buenos Aires con ejecutivo de cuenta y cajeros automáticos."
doc=nlp(text)
for token in doc:
   print(token.text, token.start, token.end)

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
