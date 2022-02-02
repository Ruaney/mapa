from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
from webdriver_manager.firefox import GeckoDriverManager

from time import sleep

@given('Entro no site')
def step_impl(context):    
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #context.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
   
    context.actions = ActionChains(context.driver)
    context.wait = WebDriverWait(context.driver,30)
    context.driver.get("https://www.globalforestwatch.org/map/")    
    context.driver.maximize_window()

@when('defino as variaveis locais')
def step_impl(context):
    driver = context.driver
    driver.execute_script(
        "window.localStorage.setItem('agreeCookies','true');")
    driver.execute_script(
        "window.localStorage.setItem('welcomeModalHidden','true');")


@when('recarrego a pagina')
def step_impl(context):
    context.driver.refresh()
    sleep(5)
    
    
  
@when('configuro RADD')
def step_impl(context):
    
    wait = context.wait
    menu_forest_change = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/ul[1]/li[1]/button')))
    menu_forest_change.send_keys(Keys.ENTER)
    # configure RADD
    menu_RADD = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[4]/button')))
    menu_RADD.send_keys(Keys.ENTER)  
    sleep(5)
@when('clico "botao de analise"')
def step_impl(context):
    
    wait = context.wait
    # elements analisis
    menu_analisis_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]/button')))
    menu_analisis_button.send_keys(Keys.ENTER)
    # actions.click(menu_analisis_button).perform()

    drawn_option = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
    ))
    drawn_option.send_keys(Keys.ENTER)


@when('clico "botao de começar a desenhar"')
def step_impl(context):
    wait = context.wait
    sleep(5)
    
    try:
        start_drawn_option = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/button')
        ))
    finally:
        # confirmando que realmente precisa clicar
        if(start_drawn_option.text == "FAÇA O DESENHO" or "START DRAWING"):
            start_drawn_option.send_keys(Keys.ENTER)
            #context.actions.click(start_drawn_option).perform()
        else:
            pass


@when('verifico se o site deu erro')
def step_impl(context):
    
    if(context.driver.title == "An error occurred"):
        context.driver.refresh()


@when('em mostrar mapa somente')
def step_impl(context):
    wait = context.wait
    
    test = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')))
    test.send_keys(Keys.ENTER)    

@when('desenho no mapa')
def step_impl(context):
    wait = context.wait
    driver = context.driver
    actions = context.actions
    elmap = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div')))
    # first click
    actions.move_to_element_with_offset(elmap, 200, 150).click().perform()

    # second click
    actions.move_to_element_with_offset(elmap, 200, 50).click().perform()
    
    # third click
    actions.move_to_element_with_offset(elmap, 300, 50).click().perform()
    sleep(3)
    # final click
    actions.double_click().perform()

    
@when('clico "mostrar mapa somente"')
def step_impl(context):
    
    test = context.driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div/div[1]/div[3]/button')
    test.send_keys(Keys.ENTER)
    
@then('verifica se as informações estão presentes')
def step_impl(context):
    sleep(20)
    
    wait = context.wait
    # treeLossGain informations
    treeLossGain = wait.until(
        EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))
    
    for inf in treeLossGain:
        assert inf.is_displayed()
    
    # tree Loss informations
    treeLoss = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]')))
    assert treeLoss.is_displayed()
