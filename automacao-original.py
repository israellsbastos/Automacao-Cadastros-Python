import pandas as pd
import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 0.5
CHROME_PATH = "chrome"
URL = "http://www.sauer.pro.br/python/automacao/index.html"
LOGIN = "admin"
CSV_FILE = "dados-alunos.csv"

# Funções auxiliares
def abrir_chrome():
    pyautogui.press("win")
    pyautogui.write(CHROME_PATH)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.write(URL)
    pyautogui.press("enter")

def login_admin():
    time.sleep(4)
    pyautogui.click(x=1277, y=612)  # Ajuste conforme necessário
    pyautogui.write(LOGIN)
    pyautogui.press("tab")
    pyautogui.write(LOGIN)
    pyautogui.press("tab")
    pyautogui.press("enter")

def acessar_formulario():
    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.press("enter")

def preencher_formulario(nome, email, endereco, telefone):
    pyautogui.click(x=1272, y=674)  # Ajuste conforme necessário
    pyautogui.write(nome)
    pyautogui.press("tab")
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(endereco)
    pyautogui.press("tab")
    pyautogui.write(telefone)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.scroll(5000)  # Ajuste conforme necessário

# Execução da automação
try:
    abrir_chrome()
    login_admin()
    acessar_formulario()

    # Leitura da tabela de dados
    tabela = pd.read_csv(CSV_FILE)

    # Preenchimento dos dados
    for linha in tabela.index:
        nome = str(tabela.loc[linha, "Nome"])
        email = str(tabela.loc[linha, "Email"])
        endereco = str(tabela.loc[linha, "Endereco"])
        telefone = str(tabela.loc[linha, "Telefone"])
        preencher_formulario(nome, email, endereco, telefone)

except Exception as e:
    print(f"Ocorreu um erro: {e}")







