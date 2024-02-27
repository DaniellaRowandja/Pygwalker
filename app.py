""" import pandas as pd
import streamlit as st
import pygwalker as pyg

df = pd.read_csv("/Users/rowandjadaniella/Downloads/apple_quality.csv")
gwalker = pyg.walk(df) 
 """

from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st
 
# Ajuster la largeur de la page Streamlit
st.set_page_config(
    page_title="Utiliser Pygwalker dans Streamlit",
    layout="wide"
)
 
# Établir la communication entre pygwalker et streamlit
init_streamlit_comm()
 
# Ajouter un titre
st.title("Utiliser Pygwalker dans Streamlit")
 
# Obtenir une instance du rendu de pygwalker. Vous devez mettre en cache cette instance pour empêcher efficacement la croissance de la mémoire en cours de processus.
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
    # Lorsque vous avez besoin de publier votre application au public, vous devriez définir le paramètre debug sur False pour empêcher les autres utilisateurs d'écrire dans votre fichier de configuration de graphique.
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)
 
renderer = get_pyg_renderer()
 
# Rendre votre interface d'exploration de données. Les développeurs peuvent l'utiliser pour construire des graphiques par glisser-déposer.
renderer.render_explore()