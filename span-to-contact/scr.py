from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Defina o número do contato manualmente (com o código do país incluído)
contato = "5513999999999"  # Exemplo: +55 para Brasil, 13 é DDD e o restante é o número
mensagem = "oiii"  # Mensagem que deseja enviar
num_mensagens = 5  # Quantidade de vezes que deseja enviar a mensagem

# Caminho para o perfil do Chrome
caminho_perfil = r"C:\Users\****\AppData\Local\Google\Chrome\User Data\Default"  # Altere conforme necessário

# Configuração do WebDriver
options = Options()
options.add_argument(f"user-data-dir={caminho_perfil}")

service = Service(r'C:\Users\****\Desktop\py\span-to-contact\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Acesse o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda um tempo para a página carregar totalmente
time.sleep(10)

# Abre a URL de conversa diretamente com o contato
url_conversa = f"https://web.whatsapp.com/send?phone={contato}"
driver.get(url_conversa)

# Aguarda um tempo para a página carregar totalmente
time.sleep(10)

# Localiza a caixa de texto para enviar mensagens
caixa_mensagem = driver.find_element("xpath", '//*[@id="main"]/footer//div[contains(@class,"copyable-text selectable-text")]')

# Envia a mensagem múltiplas vezes
for i in range(num_mensagens):
    caixa_mensagem.send_keys(mensagem)  # Digita a mensagem
    caixa_mensagem.send_keys(Keys.ENTER)  # Simula a tecla Enter para enviar a mensagem
    print(f"Mensagem {i + 1} enviada para {contato}")
    time.sleep(2)  # Pausa de 2 segundos entre os envios

# Fecha o navegador após enviar as mensagens
driver.quit()
