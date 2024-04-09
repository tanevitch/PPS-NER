import re
import pandas as pd
import spacy


nlp= spacy.load("output-merge/model-best")

input = pd.read_csv('ground_truth_100.csv', sep = '|')
input = input.fillna("")

def contiene_dos(texto):
    return ["dos","doble","2","segundo"] in texto

def contiene_tres(texto):
    return ["tres","triple","3","tercer"] in texto

def procesar_frentes(frentes_predichos):
    frentes_en_numeros= []
    for match in frentes_predichos:
        contiene_2= contiene_dos(match.lower())
        if contiene_2:
            frentes_en_numeros.append(2)
        else: 
            contiene_3= contiene_tres(match.lower())
            if contiene_3:
                frentes_en_numeros.append(3)
    else:
        frentes_en_numeros.append(1)

    return max(frentes_en_numeros)

def get_numeros(cadena: str):
    return re.findall(r'\b\d+(?:[.,]\d+)?\b', cadena)
     
def procesar_fot(predichos: list):
    predichos= list(set(predichos))
    numeros = get_numeros(" ".join(predichos))
    if len(get_numeros((" ".join(predichos)))) == 1:
        unidad = re.search(r'\b(m2|mts2|mt2)\b', " ".join(predichos))
        if unidad:
            return " ".join(set(numeros))+" "+unidad.group()
        
        return " ".join(set(numeros))
    else: 
        if len(predichos) == 2:
            result = predichos[0]+". "+predichos[1]
            result = result.replace("Res.", "residencial:")
            result = result.replace("Com.", "comercial:")
            result = result.replace("Fot", "FOT")
            result = result.replace("fot", "FOT")
            return result
        else:
            result= "".join(predichos).rstrip(".")
            result = result.replace("Fot", "FOT")
            result = result.replace("fot", "FOT")
            return result
    
def procesar_irregular(predichos):
    for predicho in predichos:
        if "irregular" in predicho.lower(): 
            return True
        patron = re.compile(r'\b(triangular|martillo|trapecio)\b', re.IGNORECASE)
        coincidencias = patron.findall(predicho)
        if bool(coincidencias):
            return True 
    else:
        return ""
    
def contar_numeros(cadena):
    numeros = re.findall(r'\b\d+(?:[.,]\d+)?\b', cadena)
    numeros_sin_duplicados = set(numeros)
    return len(numeros_sin_duplicados)


def procesar_medidas(predichos: list):
    mejor_match = max(predichos, key=len)
    if "martillo" in mejor_match:
        return mejor_match.replace(" mts", "")

    medidas = ""
    for numero in list(map(str, get_numeros(mejor_match))):
        medidas+= numero+" x "

    return medidas.rstrip(" x")

data = []
for index, row in input.iterrows():
   respuestas= {
       "DIRECCION": [],
       "FOT": [],
       "IRREGULAR": [],
       "DIMENSIONES": [],
       "ESQUINA": [],
       "NOMBRE_BARRIO": [],
       "CANT_FRENTES": [],
       "PILETA": []
   }
   doc=nlp(row['descripcion'])
   for ent in doc.ents:
        if ent.text not in respuestas[ent.label_]:
            respuestas[ent.label_].append(ent.text)


   respuestas["DIRECCION"]= max(respuestas["DIRECCION"], key=len) if respuestas["DIRECCION"] else ""
   respuestas["FOT"]= procesar_fot(respuestas["FOT"]) if respuestas["FOT"] else ""
   respuestas["DIMENSIONES"]= procesar_medidas(respuestas["DIMENSIONES"]) if respuestas["DIMENSIONES"] else ""
   respuestas["IRREGULAR"]= procesar_irregular(respuestas["IRREGULAR"]) if respuestas["IRREGULAR"] else ""
#    respuestas["IRREGULAR"]= True if contar_numeros(respuestas["DIMENSIONES"]) > 2 or "martillo" in respuestas["DIMENSIONES"] else ""
   respuestas["ESQUINA"]= True if respuestas["ESQUINA"] or "esquina" in respuestas["DIRECCION"] else ""
   respuestas["NOMBRE_BARRIO"]= max(respuestas["NOMBRE_BARRIO"], key=len) if respuestas["NOMBRE_BARRIO"] else ""
   respuestas["CANT_FRENTES"]=procesar_frentes(respuestas["CANT_FRENTES"]) if respuestas["CANT_FRENTES"] else ""
#    respuestas["CANT_FRENTES"]= 2 if respuestas["ESQUINA"] and not respuestas["CANT_FRENTES"] else ""
   respuestas["PILETA"]= True if respuestas["PILETA"] else ""

   data.append( {
       "descripcion": row['descripcion'],
       "direccion":  respuestas["DIRECCION"],
       "fot" : respuestas["FOT"],
       "irregular": respuestas["IRREGULAR"],
       "dimensiones": respuestas["DIMENSIONES"],
       "esquina": respuestas["ESQUINA"],
       "barrio": respuestas["NOMBRE_BARRIO"],
       "frentes": respuestas["CANT_FRENTES"],
       "pileta": respuestas["PILETA"]
   } )


df= pd.DataFrame(data, index=None) 
df.set_index('descripcion', inplace=True)
df.to_csv("respuestas_ner.csv", sep="|")   