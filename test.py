import re
import pandas as pd
import spacy


nlp= spacy.load("output-merge/model-best")


metricas = {
    "DIRECCION": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "FOT": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "IRREGULAR": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "DIMENSIONES": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "ESQUINA": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "NOMBRE_BARRIO": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "CANT_FRENTES": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    },
    "PILETA": {
        "tp": 0,
        "fp": 0,
        "fn": 0,
        "tn": 0,
        "p": 0.0,
        "r": 0.0,
        "f1": 0.0,
        "error": [
            
        ]
    }
}

input = pd.read_csv('ground_truth_100.csv', sep = '|')
input = input.fillna("")

def contiene_dos(texto):
    patron = re.compile(r'\b(dos|doble|2|segundo)\b', re.IGNORECASE)
    coincidencias = patron.findall(texto)
    return bool(coincidencias)

def contiene_tres(texto):
    patron = re.compile(r'\b(tres|triple|3|tercer)\b', re.IGNORECASE)
    coincidencias = patron.findall(texto)
    return bool(coincidencias)

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
    numeros = get_numeros(" ".join(predichos))
    if contar_numeros(" ".join(predichos)) == 1:
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
   respuestas["IRREGULAR"]= True if contar_numeros(respuestas["DIMENSIONES"]) > 2 else ""
   respuestas["ESQUINA"]= True if respuestas["ESQUINA"] else ""
   respuestas["NOMBRE_BARRIO"]= max(respuestas["NOMBRE_BARRIO"], key=len) if respuestas["NOMBRE_BARRIO"] else ""
   respuestas["CANT_FRENTES"]=procesar_frentes(respuestas["CANT_FRENTES"]) if respuestas["CANT_FRENTES"] else ""
   respuestas["CANT_FRENTES"]= 2 if respuestas["ESQUINA"] and not respuestas["CANT_FRENTES"] else ""
   respuestas["PILETA"]= True if respuestas["PILETA"] else ""

   for respuesta, esperada, key_metrica in zip(respuestas.values(), list(row[1:]), metricas):
        if respuesta == "" and esperada == "":
            metricas[key_metrica]["tn"]+=1
        else:
            if key_metrica in ["DIMENSIONES", "DIRECCION", "FOT", "NOMBRE_BARRIO"]:
                correcta= nlp(respuesta.strip()).similarity(nlp(esperada.strip())) == 1
            elif key_metrica == "CANT_FRENTES":
                if esperada:
                    correcta = respuesta == int(esperada) 
                else: 
                    correcta = respuesta == esperada

            elif key_metrica in [ "ESQUINA", "IRREGULAR", "PILETA"]:
                correcta= True if esperada==respuestas[key_metrica] else False


            if correcta:
                metricas[key_metrica]["tp"]+=1
            else:
                metricas[key_metrica]["error"].append({
                    "contexto": row["descripcion"],
                    "respuesta_predicha": respuesta,
                    "respuesta_esperada": esperada
                })
                if respuesta == "" and esperada != "":
                    metricas[key_metrica]["fn"]+=1
                elif (esperada == "" and respuesta != "") or (esperada!=respuesta):
                    metricas[key_metrica]["fp"]+=1

for metrica, valores in metricas.items():
    tp = valores["tp"]
    fp = valores["fp"]
    fn = valores["fn"]

    if (tp + fp) > 0:
        precision = tp / (tp + fp)
    else:
        precision = 0.0

    if (tp + fn) > 0:
        recall = tp / (tp + fn)
    else:
        recall = 0.0

    if (precision + recall) > 0:
        f1_score = 2 * ((precision * recall) / (precision + recall))
    else:
        f1_score = 0.0

    metricas[metrica]["p"] = precision
    metricas[metrica]["r"] = recall
    metricas[metrica]["f1"] = f1_score

import json
with open('resultados.json', 'w', encoding="utf8") as fp:
    json.dump(metricas, fp, ensure_ascii=False)