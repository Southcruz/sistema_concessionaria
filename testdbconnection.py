import psycopg2
import os
import sys
import traceback # Importar traceback para detalhes completos

print("--- Iniciando teste de conexão ao banco de dados ---")
print(f"Tentando usar DB: {os.getenv('POSTGRES_DB')}")
print(f"Tentando usar User: {os.getenv('POSTGRES_USER')}")
# Não vamos printar a senha por segurança, mas vamos usá-la.
print(f"Tentando usar Host: db")
print(f"Tentando usar Porta: 5432")
print("----------------------------------------------------")

try:
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host='db',  # Nome do serviço do banco no docker-compose.yml
        port='5432'
    )
    print("*************************************")
    print("*** CONEXÃO BEM SUCEDIDA! ***")
    print("*************************************")
    conn.close()
except psycopg2.Error as e_psql: # Captura erros específicos do psycopg2
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!! ERRO DE CONEXÃO (psycopg2.Error):")
    print(f"Tipo de erro: {type(e_psql).__name__}")
    print(f"Mensagem: {e_psql}")
    print(f"Código de diagnóstico (se houver): {e_psql.pgcode}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\nDetalhes completos do erro (traceback):")
    traceback.print_exc() # Imprime o traceback completo
except Exception as e_gen: # Captura outros erros inesperados
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!! ERRO GERAL INESPERADO DURANTE A CONEXÃO:")
    print(f"Tipo de erro: {type(e_gen).__name__}")
    print(f"Mensagem: {e_gen}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\nDetalhes completos do erro (traceback):")
    traceback.print_exc() # Imprime o traceback completo
finally:
    print("--- Teste de conexão finalizado ---")