from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class Browser:
    def ChromeBrowser(site):
        # Configurando as opções do navegador Chrome
        chrome_options = webdriver.ChromeOptions() 
        chrome_options.add_argument("--start-maximized") 
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.binary_location = ("./chrome-win64/chrome.exe") 
        chrome_driver_path = ("./chromedriver-win64/chromedriver.exe") 
        
        # Configurando o serviço do Chrome
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path) 

        # Inicializando o driver do Chrome
        driver = webdriver.Chrome(options=chrome_options,service=service_options)  
        
        # Abrindo o site
        driver.get(site)
        
        return (driver)
    
class PageObjects:
    def login(driver, usuario, senha):
        """
            Esta função é responsável por realizar o login em uma página web usando o Selenium WebDriver.

            Parâmetros:
                driver: O driver do Selenium WebDriver que está sendo usado para interagir com a página da web.
                usuario: O nome de usuário que será usado para fazer login.
                senha: A senha que será usada para fazer login.
        """
         
        try:
            input_usuario = driver.find_element(By.XPATH, '//input[@name="username"]')
            input_senha = driver.find_element(By.XPATH, '//input[@name="password"]')
            btn_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
            
            print("Preenchendo usuario...")
            input_usuario.send_keys(usuario)

            print("Preenchendo senha...")
            input_senha.send_keys(senha)

            print('Fazendo login...')
            btn_submit.click()

            return True
        except Exception as e:
            print('Erro no login')
            print(e)


    def inserir_dados(driver, dados):
        """
            Esta função é responsável por inserir dados em um formulário web usando o Selenium WebDriver.
            
            Parâmetros:
                driver: O driver do Selenium WebDriver que está sendo usado para interagir com a página da web.
                dados: Um dicionário contendo os dados que serão inseridos no formulário. 
        """
        try:
            for i, row in dados.iterrows():
                # Botão New Job Posting (Novo anúncio de emprego)
                btn_new_job = Waits.clickable(driver, By.XPATH, '//button[@id="newJobPosting"]')
                btn_new_job.click()
                print(f"Etapa {i} iniciando...")

                # Job ID (ID de trabalho)
                input_id = Waits.visible(driver, By.XPATH, '//input[@aria-label="jobId"]')
                driver.execute_script('arguments[0].removeAttribute("disabled");', input_id)
                input_id.clear()
                input_id.send_keys(int(row['#']))

                # Job Title (Cargo)
                input_job_title = Waits.visible(driver, By.XPATH, '//input[@id="jobTitle"]')
                input_job_title.click()
                input_job_title.clear()
                input_job_title.send_keys(row['jobTitle'])

                # Job Description (Descrição do trabalho)
                input_job_description = Waits.visible(driver, By.XPATH, '//textarea[@id="jobDescription"]')
                input_job_description.click()
                input_job_description.clear()
                input_job_description.send_keys(row['jobDescription'])

                # Hiring Department (Departamento de Contratação)
                select_job_departament = Select(driver.find_element(By.XPATH, '//select[@id="hiringDepartment"]'))
                select_job_departament.select_by_visible_text(row['hiringDepartment'])

                # Education Level (Nível de educação)
                select_job_education = Select(driver.find_element(By.XPATH, '//select[@id="educationLevel"]'))
                select_job_education.select_by_visible_text(row['educationLevel'])

                # Posting Start Date (Data de início da postagem)
                input_job_star_date = driver.find_element(By.XPATH, '//input[@id="postingStartDate"]')
                input_job_star_date.clear()
                input_job_star_date.send_keys(row['postingStartDate'])
            
                # Posting End Date (Data de término da postagem)
                input_job_end_date = driver.find_element(By.XPATH, '//input[@id="postingEndDate"]')
                input_job_end_date.clear()
                input_job_end_date.send_keys(row['postingEndDate'])
            
                # Remote (Trabalho remoto)
                if row['remote'] == 'Yes':
                    radio_job_yes = driver.find_element(By.XPATH, '//*[@id="remote"]/label[1]/span[1]/span[1]/input')
                    radio_job_yes.click()
                else:
                    radio_job_no = driver.find_element(By.XPATH, '//*[@id="remote"]/label[2]/span[1]/span[1]/input')
                    radio_job_no.click()

                # Job type (Tipo de emprego)
                if 'FULL' in row['jobType'].upper():
                    checked_job_full_time = driver.find_element(By.XPATH, '//input[@id="jobTypeFullTime"]')
                    checked_job_full_time.click()
                if 'PART' in row['jobType'].upper():
                    checked_job_part_time = driver.find_element(By.XPATH, '//input[@id="jobTypePartTime"]')
                    checked_job_part_time.click()
                if 'TEMP' in row['jobType'].upper():
                    checked_job_temp = driver.find_element(By.XPATH, '//input[@id="jobTypeTemp"]')
                    checked_job_temp.click()
                if 'PERMANENT' in row['jobType'].upper():
                    checked_job_permanent = driver.find_element(By.XPATH, '//input[@id="jobTypePermanent"]')
                    checked_job_permanent.click()
                # Botão de enviar
                btn_job_submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
                btn_job_submit.click()
            return True
        except Exception as e:
            print('Erro ao inserir os dados')
            print(e)

class Waits:
    def clickable(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, selector)))
    
    def visible(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by_type, selector))) 