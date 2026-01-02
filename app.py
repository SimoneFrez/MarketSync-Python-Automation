import streamlit as st
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv('DB_NAME', 'database_profissional.db')

st.set_page_config(page_title="MarketSync Dashboard", layout="wide")

st.title("MarketSync - Monitor de Automação")
st.markdown("Interface de monitoramento para integridade de inventário e sincronização de dados.")

def carregar_dados():
    """Realiza o fetch dos dados persistidos no banco de dados local."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM produtos", conn)
    conn.close()
    return df

try:
    df = carregar_dados()

    # Indicadores Principais (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("SKUs Processados", len(df))
    col2.metric("Volume em Estoque", df['estoque'].sum())
    col3.metric("Ticket Médio (Sincronizado)", f"R$ {df['preco'].mean():.2f}")

    st.subheader("Distribuição de Inventário")
    st.bar_chart(df.set_index('nome')['estoque'])

    st.subheader("Detalhamento dos Registros")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.warning("Pipeline de dados não detectado. Certifique-se de que a automação (main.py) foi executada com sucesso.")