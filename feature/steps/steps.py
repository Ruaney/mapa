
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
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
import pdb
logging.basicConfig(filename='mensagens_log.log',
                    filemode='w', encoding='utf-8', level=logging.INFO)
logging.info("init arquivo")


def entrarSite(context, interface):
    firefoxOptions = Options()

    if(not (interface)):
        firefoxOptions.add_argument("--headless")

    context.driver = context.webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=firefoxOptions)
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

    except TimeoutException:
        logging.exception(
            "tempo expirou, um provavel erro aconteceu no site. ")
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
        logging.exception("Botão não localizado.")
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
        logging.exception('Não foi possivel localizar o mapa para desenhar.')


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
        logging.exception("Um Erro aconteceu, tempo expirou {}".format(e))

@then('Verifica se ganho/perda de cobertura arborea estão presentes')
def step_impl(context):
    start = time.time()
    wait = context.wait

    try:
        menu_show_map = context.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div/div[1]/div[3]/button')
        menu_show_map.send_keys(Keys.ENTER)
    except NoSuchElementException:
        logging.exception("elemento de mostrar somente o mapa não localizado.")

    try:
        tree_loss_gain = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))

        if(hasattr(tree_loss_gain, '__iter__')):
            for inf in tree_loss_gain:
                logging.info(
                    "Apenas para checar. {}".format(inf.text))
                assert inf.is_displayed()
        elif(tree_loss_gain):
            logging.info(
                "Apenas para checar.  {}".format(tree_loss_gain.text))
            assert tree_loss_gain.is_displayed()

    except TimeoutException:
        logging.exception(
            'Não foi possivel verificar o ganho de cobertura arborea')

    try:
        tree_loss = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]')))

        assert tree_loss.is_displayed()
        if(tree_loss):
            logging.info(
                "Informações Perda de cobertura: {}".format(tree_loss.text))
            
        end = time.time()
        tot = end - start

        logging.info("demorou %d segundos para verificar o ganho/perda de cobertura. ", tot)
    except TimeoutException:
        logging.exception(
            'Não foi possivel verificar a perda de cobertura arborea')
    
    context.driver.quit()

@then('Verifica se ganho/perda de cobertura arborea estão presentes com base em um shape')
def step_impl(context):
    wait = context.wait
    driver = context.driver
    actions = context.actions
    time.sleep(15)

    # try:
    #     tree_loss_gain = wait.until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))

    #     if(hasattr(tree_loss_gain, '__iter__')):
    #         for inf in tree_loss_gain:
    #             logging.info(
    #                 "Apenas para checar. {}".format(inf.text))
    #             assert inf.is_displayed()
    #     elif(tree_loss_gain):
    #         logging.info(
    #             "Apenas para checar.  {}".format(tree_loss_gain.text))
    #         assert tree_loss_gain.is_displayed()

    # except TimeoutException:
    #     logging.exception(
    #         'Não foi possivel verificar o ganho de cobertura arborea')

    try:
        tree_loss = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="treeLoss"]/div[2]/div[1]')))

        assert tree_loss.is_displayed() == True
        
        if(tree_loss):
            logging.info(
                "Informações Perda de cobertura: {}".format(tree_loss.text))
            list_temp = []
            locale_string = tree_loss.text.find('2')
            string_year = tree_loss.text[(locale_string-1):(locale_string+11)]
            list_year = string_year.split(' ')
            year_begin = int(list_year[0])
            year_end = int(list_year[2])
            tot_moves = year_end - year_begin # quantas vezes vou ter que mover o mouse para pegar informaçoes de perda de cobertura no gráfico.
            
            try:
                graphic_loss = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeLoss"]/div[2]/div[2]/div/div/div[1]/svg/g[2]/g/g[1]')))
                
                #para pegar a primeira informação do grafico de perda de cobertura
                temp_value_ini = 10
                for x in range(1,tot_moves):
                    actions.move_to_element_with_offset(graphic_loss,(temp_value_ini*x),1) # move o mouse para direita de acordo com o valor de x
                    year_loss = driver.find_element(By.XPATH,'//*[@id="treeLoss"]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div') #ano do grafico
                    if(year_loss == year_passed):
                        continue
                    list_temp.append(year_loss.text)
                    loss_roof_hect = driver.find_element(By.XPATH, '//*[@id="treeLoss"]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]') #hectares perdidos
                    list_temp.append(loss_roof_hect.text)
                    year_passed = year_loss.text
                pdb.set_trace()
                    
            except TimeoutException:
                logging.exception('não foi possivel localizar o gráfico de perda de cobertura arborea.')
                

        #vou ter que pegar aqui o ano de inicio e fim no texto que vai ta dentro de
        #treeLoss, dai vou ter inicio e fim para poder saber quantas vezes vou ter que mover o mouse em cima do grafico
        #para pegar as informações de perda de cobertura dos anos e pegar o grafico
        #pelo XPATH e mover o mouse para ir aparecendo as informaçoes e ao mesmo tempo
        # atualizar uma variavel para armazenar valores temporariamente. 
        #Posso mover o mouse com actions.move_to_element_with_offset(variavel,10,1) -- começo em 10,1 
        #depois vou movendo de 10 em 10
        # do 150 para 160 o ano nao se alterou, vou ter que verificar se o ano se altera em 1 para continuar se nao jogar um erro
        
    except TimeoutException:
        logging.exception(
            'Não foi possivel verificar a perda de cobertura arborea')

    context.driver.quit()

