import pandas as pd

# Nome do arquivo CSV 
nome_arquivo = "tabela_contratos.csv"

# Carregando arquivo
try:
    df = pd.read_csv(nome_arquivo)

    # Verifica se a coluna "fk_empresa_contratada" está presente antes de tentar removê-la
    if "fk_empresa_contratada" in df.columns:
        # Remova a coluna "fk_empresa_contratada"
        df = df.drop(columns=["fk_empresa_contratada"])

        # nome saida arquivo
        nome_arquivo_saida = "tabelas_contratos_sem_empresa.csv"

        try:
            # salvando
            df.to_csv(nome_arquivo_saida, index=False)

            print(f"Coluna 'fk_empresa_contratada' removida e DataFrame salvo como '{nome_arquivo_saida}'")

        except Exception as e:
            print(f"Ocorreu um erro ao salvar o arquivo: {str(e)}")

    else:
        print("A coluna 'fk_empresa_contratada' não foi encontrada no DataFrame.")

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
