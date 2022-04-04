######################### Importation des librairies #########################

import sys
from streamlit import cli as stcli
import streamlit as st
import streamlit
from PIL import Image
import requests
import sklearn as sk
import pandas as pd


######################### Lancement de l'application #########################

@st.cache(allow_output_mutation=True, show_spinner=True, suppress_st_warning=True)
def main():
    st.write('')

if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
        


######################### Front-end ######################### 
  
# Page principale
st.title("Outil propriétaire de scoring de prêt")
st.header("Testez l'égibilité des clients aux prêts 0%")

st.info('''
- Notre entreprise propose désormais des crédits à la consommation auprès d'une clientèle ayant peu ou pas du tout d'historique de prêt.
- Pour vous permettre de travailler dans les meilleurs conditions, nos data scientists ont développé  un outil de “scoring crédit” qui calcule la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé.
- Les résultats sont affiché sous la forme d'un dashboard interactif auquel vous avez accès en tant que gestionnaires de la relation client.
- Ces données vont vous permettre d'interpréter les prédictions réalisées, et d’améliorer la connaissance de vos prospects et clients.  
- Vous pourrez également   
- Nos clients étant de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit, vous pourrez désormais leur expliquer de façon la plus transparente possible les décisions d’octroi de crédit grâce à cet outil
''')

# Barre latérale
logo = Image.open("logo.jpg")
st.sidebar.image(logo)

st.sidebar.subheader("Entrez l'identifiant")
#page_names = ["Accueil gestionnaire", "Prediction"]
#page = st.sidebar.radio("", page_names, index=0)

######################### Récupération des données et prediction #########################

# Prediction
@st.cache(allow_output_mutation=True, show_spinner=True, suppress_st_warning=True)
def request_prediction():
    response = requests.requests(
        method='GET', url='http://127.0.0.1:5000/')
    if response.status_code != 200:
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))
    return response.json()


id_custom = st.sidebar.selectbox("Selectionnez l'identifiant client", ['1' ,'2','3'])
if id_custom == '1':
    rec = requests.get('http://127.0.0.1:5000/')
    st.sidebar.write(rec.text)
