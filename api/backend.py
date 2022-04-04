######################### Importation des librairies #########################

from flask import Flask, request, jsonify 
import joblib
import pandas as pd 
import json
import sklearn as sk

# Chargements des données
clf = joblib.load('xgb_60k.joblib')
df = pd.read_csv('df_to_modelisation_short.csv')


######################### Lancement de l'application #########################

app = Flask(__name__)

@app.route("/", methods=["GET"])
def loaded():
    return "API, modeles et données en cours de chargement..."

# Fonction pour predire la classe du client
@app.route('/predict', methods =['GET'])
def predict():
    ser = df.sample(1).drop(['TARGET'],inplace=False, axis=1)
    pred = clf.predict(ser)
    return str(pred)    

# Fonction pour extraire la liste de tous les id 
@app.route('/predict/sk_ids', methods =['GET'])
def sk_ids():
    # Extraire la liste de tous les identifiants 'SK_ID_CURR' dans le df.
    sk_ids = pd.Series(list(df.index.sort_values()))
    # Convertir pd.Series en JSON
    sk_ids_json = json.loads(sk_ids.to_json())
    # Retourner les données 
    return jsonify({'status': 'ok',
    		        'df': sk_ids_json})


######################### Execution de l'application #########################
    
if __name__ == '__main__':
    app.run()