from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def clickAnalisisButton():
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


def clickMapOnly():

    try:
        test = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/button')))
        actions.click(test).perform()
    except:
        test = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div/div[1]/div[3]/button')
        actions.click(test).perform()


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


def collectInformations():
    # treeLossPct e treeLoss id
    elinformations = wait.until(
        EC.presence_of_element_located((By.ID, "#treeLossPct")))

    print("display: " + elinformations.is_displayed())
    print("enable: " + elinformations.is_enabled())
    print("text: " + elinformations.text)
    print("parent: " + elinformations.parent)


# configs
# driver = webdriver.Firefox(
#     executable_path=r'D:\downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
driver = webdriver.Firefox()
driver.get("https://www.globalforestwatch.org/map/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)
# define variables in localStorage
driver.execute_script(
    "window.localStorage.setItem('agreeCookies','true');")
driver.execute_script(
    "window.localStorage.setItem('welcomeModalHidden','true');")
# driver.execute_script(
#     "window.localStorage.setItem('txlive:selectedlang','pt_BR');")
driver.refresh()

# try:
menu_forest_change = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/ul[1]/li[1]/button')))
menu_forest_change.send_keys(Keys.ENTER)
# configure RADD
menu_RADD = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[4]/button')))
menu_RADD.send_keys(Keys.ENTER)

# finally:
clickAnalisisButton()
buttonStartDrawn()
sleep(2)
if(driver.title == "An error occurred"):
    driver.refresh()
    # buttonStartDrawn()
clickMapOnly()
drawnInMap()

clickMapOnly()
# collectInformations()
# pageSource = driver.page_source
# fileTowrite = open("page_source.html","w");
# fileTowrite.write(pageSource)
# fileTowrite.close()
# drawn_option = driver.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
