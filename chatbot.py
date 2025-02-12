import requests
import json
import os
from dotenv import load_dotenv
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Assistant d'Orientation - Chatbot",
    page_icon="logo_Orisup.jpg",
    layout="centered",
)
# Ajouter le logo en haut de la page
st.image("logo_Orisup.jpg", width=150, caption="Orisup")


# Chargement de la clé API depuis un fichier .env
load_dotenv()
api_key = os.getenv("API_KEY")

# URL de l'API
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

# Lecture des données des universités
with open("data_university.txt", "r") as file:
    university_data = file.read()

# Ajouter un style personnalisé pour l'arrière-plan
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, orange, blue);
        color: white;
        font-family: Arial, sans-serif;
    }
    div.stButton > button {
        background-color: #00008B;
        color: white;
        border-radius: 5px;
    }
    div.stTextInput > div > input {
        border: 2px solid #0056b3;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titre de l'application
st.title("💬 Chatbot - Assistant d'Orientation Universitaire")

# Conteneur de discussion
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Bienvenue ! Posez-moi votre question ou demandez des conseils d'orientation universitaire 😊."}
    ]

# Fonction pour afficher les messages
def afficher_messages():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div style='text-align: right; color: white; background-color: #0056b3; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; color: white; background-color: #ff6600; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>{message['content']}</div>", unsafe_allow_html=True)

# Affichage des messages existants
afficher_messages()

# Entrée utilisateur
user_input = st.text_input("Votre message :", key="user_input")

# Si l'utilisateur envoie un message
if st.button("Envoyer"):
    if user_input.strip():
        # Ajouter le message utilisateur à la discussion
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Construire le prompt pour l'API
        prompt = [
            {
                "text": """message system: Tu es un chatbot assistant spécialisé en orientation universitaire pour le réseau des universités marocaines. 
                Utilise les données disponibles et propose des suggestions précises et adaptées, avec un ton chaleureux et engageant."""
            },
            {
                "text": f"prompt: {user_input}\nDonnées sur les universités: {university_data}"
            }
        ]

        # Préparer la requête pour l'API
        payload = json.dumps({
            "contents": [{"parts": prompt}],
            "generation_config": {"temperature": 0.5}
        })
        headers = {"Content-Type": "application/json"}

        # Envoyer la requête à l'API
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            result = response.json()
            response_text = result["candidates"][0]["content"]["parts"][0]["text"]

            # Ajouter la réponse du chatbot à la discussion
            st.session_state.messages.append({"role": "bot", "content": response_text})
        else:
            st.session_state.messages.append(
                {"role": "bot", "content": "Désolé, je ne peux pas répondre pour le moment. Veuillez réessayer plus tard."}
            )

     

