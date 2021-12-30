from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.exceptions import [NoSuchElementException()]
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

    elmap = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div')))
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
    driver.implicitly_wait(5)


def collectInformations():
    # treeLossPct informations
    try:
        elinformations = wait.until(
            EC.presence_of_all_elements_located((By.XPATH,'//*[@id="treeLossPct"]')))
        if(elinformations):
            print("PCTtext" + elinformations.text)
        
    except:
        print("pct tree loss não existe")
    finally:
        pass
    # tree Loss informations
    try:
        elinformations2 = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]')))
        elinformations2_texto = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]')))
        # elinformations2_grafico = wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//[@id="treeLoss"]/div[2]/div[2]')))
        if(elinformations2):
            # print("title LOSS: " + elinformations2.text) # uncomment if you want to see the text 
            print(elinformations2.is_displayed())
            
        if(elinformations2):
            # print("text LOSS: " + elinformations2_texto.text) # uncomment if you want to see the text 
            print(elinformations2_texto.is_displayed())
    except:
        print("tree informations não existe.")

    finally:
        pass


# configs
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(
    executable_path=r'D:\downloads\geckodriver-v0.30.0-win64\geckodriver.exe')

# driver = webdriver.Firefox()
driver.get("https://www.globalforestwatch.org/map/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 30)
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
collectInformations()
