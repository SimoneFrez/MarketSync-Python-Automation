import pandas as pd
import sqlite3
import time
import logging
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv('DB_NAME', 'database_profissional.db')

logging.basicConfig(
    filename='automacao.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def setup_db():
    """Inicializa a conexão com o banco de dados e cria o schema se necessário."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos 
                      (id INTEGER PRIMARY KEY, nome TEXT, preco REAL, estoque INTEGER)''')
    conn.commit()
    return conn

def processar_automacao():
    """Executa o pipeline de sincronização de inventário."""
    logging.info("Iniciando processamento de sincronização.")
    
    sucessos = 0
    erros = 0
    conn = setup_db()
    
    # Dataset para processamento
    dados = {
        'nome': ['Camisa Polo', 'Calça Jeans', 'Tênis Esportivo', 'SKU_INVALIDO_1', 'SKU_INVALIDO_2'],
        'preco': [89.90, 150.00, 299.00, -5.00, 100.00],
        'estoque': [50, 20, 10, 5, -1]
    }
    df = pd.DataFrame(dados)

    for index, row in df.iterrows():
        try:
            # Validação de regras de negócio: Preço e Estoque positivos
            if row['preco'] > 0 and row['estoque'] >= 0:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
                               (row['nome'], row['preco'], row['estoque']))
                conn.commit()
                sucessos += 1
                logging.info(f"Sucesso: {row['nome']}")
            else:
                erros += 1
                logging.warning(f"Falha de Validação: {row['nome']} | Dados: P:{row['preco']} E:{row['estoque']}")
            
            time.sleep(0.1)
            
        except Exception as e:
            erros += 1
            logging.error(f"Erro na transação {row['nome']}: {e}")

    conn.close()
    
    # Output de monitoramento
    total = sucessos + erros
    taxa_sucesso = (sucessos / total) * 100 if total > 0 else 0
    
    print("-" * 30)
    print("RESUMO DA OPERAÇÃO")
    print(f"Sincronizados: {sucessos}")
    print(f"Falhas: {erros}")
    print(f"Eficiência: {taxa_sucesso:.1f}%")
    print("-" * 30)
    
    logging.info(f"Processamento finalizado. Sucessos: {sucessos}, Erros: {erros}")

if __name__ == "__main__":
    processar_automacao()