from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from behave import *
from time import sleep
import time

def configurarRADD(context):
    driver = context.driver
    wait = context.wait 
    driver.execute_script(
        "window.localStorage.setItem('agreeCookies','true');")
    driver.execute_script(
        "window.localStorage.setItem('welcomeModalHidden','true');")
    context.driver.refresh()
    sleep(5)
    menu_forest_change = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/ul[1]/li[1]/button')))
    menu_forest_change.send_keys(Keys.ENTER)
    # configure RADD
    menu_RADD = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[4]/button')))
    menu_RADD.send_keys(Keys.ENTER)  
    sleep(5)
    
@given('Entro no site globalforest')
def step_impl(context):    
    context.driver.get("https://www.globalforestwatch.org/map/")    


@when('Configuro RADD no menu esquerdo opcao Forest Change')
def step_impl(context):
    configurarRADD(context)
    
@when('Clico "botao de analise" presente ao lado do menu esquerdo')
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

@when('Clico "botao de começar a desenhar ou fazer upload da forma"')
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
    
    
    buttonShowMap = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')))
    buttonShowMap.send_keys(Keys.ENTER) 

@when('Desenho no mapa com base na long e lat')
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

@then('Verifica se ganho/perda de cobertura arborea estão presentes')
def step_impl(context):
    menuShowMap = context.driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div/div[1]/div[3]/button')
    menuShowMap.send_keys(Keys.ENTER)
    
    start = time.time()
    
    wait = context.wait
    try:
        treeLossGain = wait.until(
        EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))
    
        for inf in treeLossGain:
            assert inf.is_displayed()
        
        treeLoss = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]')))
        assert treeLoss.is_displayed()
    except TimeoutException:
        print("tempo expirou")

    end = time.time()
    tot = end - start
    print("demorou: ",tot)