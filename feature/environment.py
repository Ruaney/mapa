from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


def before_all(context):
    firefoxOptions = Options()
    firefoxOptions.add_argument("--headless")
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefoxOptions)
    context.actions = ActionChains(context.driver)
    context.wait = WebDriverWait(context.driver,15)
    #context.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    
def before_scenario(context,scenario):
    context.driver.maximize_window()
    