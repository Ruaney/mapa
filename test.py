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
       test2=driver.find_element(By.XPATH,'')
       test2.send_keys(Keys.ENTER)

#configs
driver = webdriver.Firefox(
    executable_path=r'D:\downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
driver.get("https://www.globalforestwatch.org/map/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver,20)
# define variables in localStorage
driver.execute_script(
    "window.localStorage.setItem('agreeCookies','true');")
driver.execute_script(
    "window.localStorage.setItem('welcomeModalHidden','true');")
driver.refresh()
clickMapOnly()
clickMapOnly()

