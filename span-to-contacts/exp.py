import pywhatkit as kit
import pandas as pd
import time  # Adiciona a função sleep para controlar o tempo de espera

def carregar_contatos(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv, header=None)
        return df[0].tolist()  # Supondo que o telefone esteja na primeira coluna
    except Exception as e:
        print(f"Erro ao carregar contatos: {e}")
        return []

def formatar_numero(numero):
    # Remove todos os caracteres que não sejam dígitos
    numero_limpo = ''.join(filter(str.isdigit, numero))
    
    # Verifica se o número tem 11 dígitos (DDD + número) e adiciona o código do Brasil
    if len(numero_limpo) == 11:  # Exemplo: 11973750137
        return f"+55{numero_limpo}"
    elif len(numero_limpo) == 13:  # Exemplo: já contém o código do país: 5511973750137
        return f"+{numero_limpo}"
    else:
        print(f"Formato de número inválido: {numero}")
        return None

mensagem = """oiii
"""

imagem = r"///"  # Certifique-se de que o caminho está correto

contatos = carregar_contatos(".csv") # carregue os contatos com seu arquivo csv

for contato in contatos:
    try:
        contato_formatado = formatar_numero(contato)

        if contato_formatado:
            print(f"Enviando para: {contato_formatado}")

            # Envia a mensagem e espera 30 segundos após o envio
            kit.sendwhats_image(contato_formatado, imagem, mensagem, 20)  # Atraso de 20 segundos para carregar o WhatsApp Web
            time.sleep(20)  # Pausa de 30 segundos entre os envios para garantir que a mensagem foi enviada
            print(f"Imagem e mensagem enviadas para {contato_formatado}")
        else:
            print(f"Não foi possível enviar para {contato}, número inválido.")

    except Exception as e:
        print(f"Erro ao enviar para {contato_formatado}: {e}")
