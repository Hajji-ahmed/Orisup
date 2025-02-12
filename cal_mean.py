import streamlit as st
# Configuration de la page
st.set_page_config(
    page_title="Assistant d'Orientation - Chatbot",
    page_icon="logo_Orisup.jpg",
    layout="centered",
)
# Ajouter le logo en haut de la page
st.image("logo_Orisup.jpg", width=150, caption="Orisup")

# Fonction pour calculer la moyenne générale
def calculer_moyenne(notes, coefficients):
    total_notes = sum([note * coef for note, coef in zip(notes, coefficients)])
    total_coefficients = sum(coefficients)
    if total_coefficients != 0:
        moyenne = total_notes / total_coefficients
    else:
        moyenne = 0
    return moyenne

css = """
    body {
        background-color: #f0f8ff; /* Couleur de fond bleu clair */
        color: #333333; /* Couleur du texte */
    }
    .stButton button {
        background-color: #ff7f50; /* Orange pour le bouton */
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
    .stTitle {
        color: #1e3a8a; /* Bleu pour le titre */
        font-size: 36px;
        font-weight: bold;
    }
    .stTextInput, .stNumberInput {
        border: 2px solid #1e3a8a; /* Bordure bleue pour les champs de saisie */
        border-radius: 5px;
    }
    .stTextInput input, .stNumberInput input {
        color: #1e3a8a; /* Couleur du texte dans les champs */
    }
    .stMarkdown {
        color: #ff7f50; /* Orange pour les textes affichés */
    }
"""
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.title("Calcul de la Moyenne Générale")


matieres = ["Mathématiques", "Physique", "Chimie", "Français", "Informatique"]


notes = []
coefficients = []

# Entrée des notes et des coefficients
for matiere in matieres:
    note = st.number_input(f"Note pour {matiere}", min_value=0.0, max_value=20.0, step=0.5)
    coefficient = st.number_input(f"Coefficient pour {matiere}", min_value=1, step=1)
    
    notes.append(note)
    coefficients.append(coefficient)

# Calcul de la moyenne générale
if st.button("Calculer la Moyenne"):
    moyenne = calculer_moyenne(notes, coefficients)
    st.write(f"La moyenne générale est : {moyenne:.2f}")
