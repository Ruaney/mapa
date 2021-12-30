from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


def clickMapOnly():

    # test = driver.find_element(By.id, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')
    # actions.click(test).perform()
    # test.send_keys(Keys.ENTER)
    # actions.move_to_element(test).click().perform()
    try:
        test = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')))
        test.send_keys(Keys.ENTER)

    except:
        test2 = driver.find_element(By.XPATH, '')
        test2.send_keys(Keys.ENTER)


def drawnInMap():
    driver.implicitly_wait(2)

    elmap = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div')
    # first click
    actions.move_to_element_with_offset(elmap, 200, 150).click().perform()

    driver.implicitly_wait(1)
    # second click
    actions.move_to_element_with_offset(elmap, 200, 50).click().perform()
    driver.implicitly_wait(1)
    # third click
    actions.move_to_element_with_offset(elmap, 300, 50).click().perform()
    driver.implicitly_wait(1)
    # final click
    actions.double_click().click().perform()
    driver.implicitly_wait(1)

    # driver.implicitly_wait(10)


def clickAnalisisButton():
    # elements analisis
    # menu_analisis_button = driver.find_element(
    #     By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]/button')
    menu_analisis_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]/button')))
    menu_analisis_button.send_keys(Keys.ENTER)
    # actions.click(menu_analisis_button).perform()

    drawn_option = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
    ))
    drawn_option.send_keys(Keys.ENTER)


def buttonStartDrawn():

    try:
        start_drawn_option = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/button')
        ))
    finally:
        # confirmando que realmente precisa clicar
        if(start_drawn_option.text == "FAÇA O DESENHO" or "START DRAWING"):
            start_drawn_option.send_keys(Keys.ENTER)
        else:
            pass


# configs
driver = webdriver.Firefox()
driver.get("https://www.globalforestwatch.org/map/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)
# define variables in localStorage
driver.execute_script(
    "window.localStorage.setItem('agreeCookies','true');")
driver.execute_script(
    "window.localStorage.setItem('welcomeModalHidden','true');")
driver.refresh()
clickAnalisisButton()
buttonStartDrawn()
clickMapOnly()
drawnInMap()
