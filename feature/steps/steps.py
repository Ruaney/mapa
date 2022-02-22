
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
import time
import logging
import os

logging.basicConfig(filename='mensagens_log.log',
                    filemode='w', encoding='utf-8', level=logging.INFO)
logging.info("init arquivo")


def entrarSite(context, interface):
    firefoxOptions = Options()

    if(not (interface)):
        firefoxOptions.add_argument("--headless")

    context.driver = context.webdriver.Firefox(
        executable_path=GeckoDriverManager().install(), options=firefoxOptions)
    context.actions = ActionChains(context.driver)
    context.wait = WebDriverWait(context.driver, 15)
    context.driver.get("https://www.globalforestwatch.org/map")
    context.driver.maximize_window()


@given('Entro no site globalforest (com interface grafica)')
def step_impl(context):

    entrarSite(context, True)


@given('Entro no site globalforest (sem interface grafica)')
def step_impl(context):
    entrarSite(context, False)


@when('Configuro RADD no menu esquerdo opcao Forest Change')
def step_impl(context):
    driver = context.driver
    wait = context.wait
    driver.execute_script(
        "window.localStorage.setItem('agreeCookies','true');")
    driver.execute_script(
        "window.localStorage.setItem('welcomeModalHidden','true');")
    context.driver.refresh()
    time.sleep(5)
    menu_forest_change = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/ul[1]/li[1]/button')))
    menu_forest_change.send_keys(Keys.ENTER)
    # configure RADD
    menuRADD = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[4]/button')))
    menuRADD.send_keys(Keys.ENTER)
    time.sleep(5)


@when('Clico botao de analise presente ao lado do menu esquerdo')
def step_impl(context):

    wait = context.wait
    try:
        menu_analisis_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]/button')))
        menu_analisis_button.send_keys(Keys.ENTER)

        drawn_option = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
        ))
        drawn_option.send_keys(Keys.ENTER)

    except TimeoutException as e:
        logging.critical(
            "tempo expirou, um provavel erro aconteceu no site. %s", e)
        if(context.driver.title == " An error ocurred"):
            logging.critical("Um erro ocorreu no site")


@when('Clico botao de começar a desenhar ou fazer upload da forma')
def step_impl(context):
    time.sleep(5)
    wait = context.wait
    try:
        start_drawn_option = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/button')
        ))
        # confirmando que realmente precisa clicar
        if(start_drawn_option.text == "FAÇA O DESENHO" or "START DRAWING"):
            start_drawn_option.send_keys(Keys.ENTER)
            # context.actions.click(start_drawn_option).perform()
        buttonShowMap = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')))
        buttonShowMap.send_keys(Keys.ENTER)
    except (StaleElementReferenceException, TimeoutException):
        logging.info("Botão não localizado.")
        if(context.driver.title == "An error ocurred"):
            logging.critical("Um erro ocorreu no site")


@when('soluçao temporaria, para erro que acontece aqui')
def step_impl(context):
    context.driver.refresh()
    time.sleep(10)


@when('Desenho no mapa com base na long e lat')
def step_impl(context):
    wait = context.wait
    actions = context.actions
    try:
        elmap = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div')))
        # first click
        actions.move_to_element_with_offset(elmap, 200, 150).click().perform()

        # second click
        actions.move_to_element_with_offset(elmap, 200, 50).click().perform()

        # third click
        actions.move_to_element_with_offset(elmap, 300, 50).click().perform()
        time.sleep(3)
        # final click
        actions.double_click().perform()
    except TimeoutException:
        logging.info('Não foi possivel localizar o mapa para desenhar.')


@when('Coloco o arquivo com a forma')
def upload_archive_with_form(context):
    wait = context.wait
    localRelative = r"\shapes\fp_MS_atualizado_r2_idade_rev_clayton.zip"
    archive = os.getcwd()+localRelative
    logging.info("local do arquivo: %s", archive)
    try:
        uploadArchiveElement = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div[3]/input')))
        uploadArchiveElement.send_keys(archive)

    except TimeoutException as e:
        logging.warning("Um Erro aconteceu, tempo expirou {}".format(e))

@then('Verifica se ganho/perda de cobertura arborea estão presentes')
def step_impl(context):
    start = time.time()
    wait = context.wait

    try:
        menuShowMap = context.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div/div[1]/div[3]/button')
        menuShowMap.send_keys(Keys.ENTER)
    except NoSuchElementException:
        logging.info("elemento de mostrar somente o mapa não localizado.")

    try:
        treeLossGain = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))

        if(hasattr(treeLossGain, '__iter__')):
            for inf in treeLossGain:
                logging.info(
                    "Apenas para checar. {}".format(inf.text))
                assert inf.is_displayed()
        elif(treeLossGain):
            logging.info(
                "Apenas para checar.  {}".format(treeLossGain.text))
            assert treeLossGain.is_displayed()

    except TimeoutException:
        logging.info(
            'Não foi possivel verificar o ganho de cobertura arborea')

    try:
        treeLoss = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]')))

        assert treeLoss.is_displayed()
        if(treeLoss):
            logging.info(
                "Informações Perda de cobertura: {}".format(treeLoss.text))
        end = time.time()
        tot = end - start
        logging.info("demorou %d segundos para verificar o ganho/perda de cobertura. ", tot)
    except TimeoutException:
        logging.info(
            'Não foi possivel verificar a perda de cobertura arborea')

    context.driver.quit()

# @then('Verifico se ganho/perda de cobertura arborea estão presentes')
# def step_impl(context):
#     pass
