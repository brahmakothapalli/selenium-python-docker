''' this module contains tests to sequentially'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    '''Executing the test_google_search'''
    # chrome_options = webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://www.google.com")
    driver.find_element(By.NAME , "q").send_keys("brahmakothapalli.hashnode.com", Keys.ENTER)
    print(driver.title)
    print("Execution completed :: test_google_search")
    driver.quit()