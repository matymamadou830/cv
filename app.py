import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Ndeye Maty Ndiaye - Géomatique", layout="wide")

# --- CSS PERSONNALISÉ (Marron et Saumon) ---
st.markdown("""
    <style>
    /* Arrière-plan général marron */
    .stApp {
        background-color: #5D4037;
        color: white;
    }
    
    /* Colonne de gauche (Profil) plus foncée */
    .sidebar-custom {
        background-color: #3E2723;
        padding: 30px;
        border-radius: 15px;
        height: 100%;
        border: 1px solid #FA8072;
    }

    /* Ligne de séparation couleur Saumon */
    .salmon-line {
        border: 0;
        height: 3px;
        background: #FA8072;
        margin: 20px 0;
        border-radius: 5px;
    }

    /* Style du contenu de droite */
    .right-content {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 15px;
    }
    
    h1, h2, h3 {
        color: #FA8072 !important; /* Couleur Saumon pour les titres */
    }
    </style>
    """, unsafe_allow_html=True)

# --- STRUCTURE DU CV (30% / 70%) ---
col1, col2 = st.columns([3, 7])

# --- COLONNE DE GAUCHE (30% - Profil & Contacts) ---
with col1:
    st.markdown('<div class="sidebar-custom">', unsafe_allow_html=True)
    st.title("👤 Profil")
    st.write("### *Ndeye Maty Ndiaye*")
    st.write("Étudiante en 2ème année de Géomatique (G15)")
    
    st.markdown('<div class="salmon-line"></div>', unsafe_allow_html=True)
    
    st.subheader("📍 Contact")
    st.write("📧 Matymamadou830@gmail.com")
    st.write("📞 772067109")
    st.write("🏠 Dakar, Sénégal")
    
    st.markdown('<div class="salmon-line"></div>', unsafe_allow_html=True)
    
    st.subheader("🌍 Langues")
    st.write("- *Français* : Courant")
    st.write("- *Wolof* : Maternel")
    st.write("- *Anglais* : Technique")
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLONNE DE DROITE (70% - Parcours & Compétences) ---
with col2:
    st.markdown('<div class="right-content">', unsafe_allow_html=True)
    st.header("📄 CURRICULUM VITAE")
    
    # Section Formation
    st.subheader("🎓 Formation")
    st.write("*2024 - Présent* : Licence 2 en Géomatique - CEDT G15")
    st.write("*Baccalauréat* : Obtenu au Lycée de [Academia Limamoulaye]")
    st.write("*BFEM* : Obtenu au Collège de [Academia Limamoulaye]")
    
    st.markdown('<div class="salmon-line"></div>', unsafe_allow_html=True)

    # Section Compétences (Les points clés demandés)
    st.subheader("💻 Compétences Techniques")
    st.write("✅ *Maîtrise de la cartographie SIG* (QGIS, ArcGIS)")
    st.write("✅ *Collecte de données* (KoboCollect, GPS)")
    st.write("✅ *Modélisation 3D* et Analyse spatiale")
    st.write("✅ *Programmation Python* intégrée à Streamlit")
    
    st.markdown('<div class="salmon-line"></div>', unsafe_allow_html=True)

    # Section Qualités
    st.subheader("🤝 Qualités")
    st.write("- Rigueur et organisation")
    st.write("- Esprit d'analyse technique")
    st.write("- Capacité à proposer des solutions innovantes")

    st.markdown('</div>', unsafe_allow_html=True)

# --- PIED DE PAGE INTERACTIF ---
st.write("")
if st.button("Soumettre mon profil"):
    st.balloons()
    st.success("Candidature de Ndeye Maty Ndiaye envoyée avec succès !")
