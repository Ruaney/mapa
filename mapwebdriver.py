from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def clickAnalisisButton():
    # elements analisis
    menu_analisis_button = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]/button')
    menu_analisis_button.send_keys(Keys.ENTER)
    # actions.click(menu_analisis_button).perform()

    drawn_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
    ))
    drawn_option.send_keys(Keys.ENTER)

   
def buttonStartDrawn():
    try:
        start_drawn_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
            '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/button')
        ))
    finally:
        start_drawn_option.send_keys(Keys.ENTER)
    
        
driver = webdriver.Firefox(
    executable_path=r'D:\downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
driver.get("https://www.globalforestwatch.org/map/")
driver.maximize_window()
actions = ActionChains(driver)

# define variables in localStorage
driver.execute_script(
    "window.localStorage.setItem('agreeCookies','true');")
driver.execute_script(
    "window.localStorage.setItem('welcomeModalHidden','true');")
driver.refresh()

try:
    menu_forest_change = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/ul[1]/li[1]/button')))
    menu_forest_change.send_keys(Keys.ENTER)
    # configure RADD
    menu_RADD = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[4]/button')))
    menu_RADD.send_keys(Keys.ENTER)

finally:
    clickAnalisisButton()
    buttonStartDrawn()
    sleep(2)
    if(driver.title == "An error occurred"):
        driver.refresh()
    # pageSource = driver.page_source
    # fileTowrite = open("page_source.html","w");
    # fileTowrite.write(pageSource)
    # fileTowrite.close()
# drawn_option = driver.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/button[2]')
