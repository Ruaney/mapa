from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
import unittest

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'D:\downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")

        assert "Python" in driver.title

        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source
        sleep(2)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
  