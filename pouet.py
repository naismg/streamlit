import streamlit as st
import pandas as pd
import os
import requests
import json
from supabase import create_client, Client

st.set_page_config(layout="wide")

# CSS to inject a black banner with light blue text
st.markdown("""
    <style>
    .header {
        background-color: black;
        color: #00BFFF;
        padding: 10px;
        text-align: center;
    }
    </style>
    <div class="header">
        <h2>Windturbine production</h2>
    </div>
    """, unsafe_allow_html=True)

# session state
def change_is_logged_session():
    st.session_state["is_logged"] = not st.session_state["is_logged"]

# Créer le client Supabase
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

if "is_logged" not in st.session_state:
    st.session_state["is_logged"] = False

if st.session_state["is_logged"] == False:

    placeholder = st.empty()

    with placeholder.form("login"):
        st.markdown("#### Bonjour, veuillez renseigner vos identifiants")
        user_email = st.text_input(label="Email", placeholder="votremail@exemple.com")
        user_password = st.text_input(label="Mot de passe", placeholder="Enter votre mot de passe", type="password")
        login_button = st.form_submit_button("Login")

        if ((login_button) and (user_email == st.secrets['EMAIL']) and (user_password == st.secrets['PASSWORD'])):
            change_is_logged_session()
            placeholder.empty()
        elif ((login_button) and ((user_email != st.secrets['EMAIL']) or (user_password != st.secrets['PASSWORD']))):
            st.error('Identifiants incorrects, veuillez réessayer', icon="⚠️")

# submit sample form if logged
if st.session_state["is_logged"] == True:
    st.button("Déconnexion", on_click=change_is_logged_session)

    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)
    col6, col7, col8 = st.columns(3)

    col1.empty()
    col2.empty()
    col3.empty()
    col5.empty()
    col6.empty()
    col8.empty()

    user_input = col4.text_input("Entrez les données de prédiction", "")

    if st.button("Predict"):
        # Simuler une prédiction pour la démonstration
        prediction = "123.45545 MW"

        # # Insérer la prédiction dans la base de données
        # data, count = supabase.table('predWindturbine').insert({"id":1,"value":user_input,"pred": prediction}).execute()
        st.markdown("#### Prédiction envoyée à la base de données")

        # if count > 0:
        #     st.success("La prédiction a été envoyée avec succès à la base de données!")
        # else:
        #     st.error("Il y a eu une erreur lors de l'envoi de la prédiction à la base de données.")

        col7.write(f'La prédiction pour "{user_input}" est: {prediction}')
