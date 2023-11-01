from navigation import Browser, PageObjects
import pandas as pd

def ini():
    site = 'https://rpaexercise.aisingapore.org/login'
    usuario = 'jane007'
    senha = 'TheBestHR123'

    arquivo = './assets/datatable.csv'

    dados = pd.read_csv(arquivo, sep=',')

    driver = Browser.ChromeBrowser(site)
    if(PageObjects.login(driver, usuario, senha)):
        PageObjects.inserir_dados(driver, dados)

    print('Finalizado!')
    driver.close()
    driver.quit()

    return True

