'''this module contains tests to execute sequentially on the selenium-hun in docker containers'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search():
    '''Executing the test_google_search'''
    chrome_options = webdriver.ChromeOptions()
    driver=webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=chrome_options)
    driver.maximize_window()
    driver.get("http://www.google.com")
    driver.find_element(By.NAME , "q").send_keys("brahma-coder.hashnode.com", Keys.ENTER)
    print(driver.title)
    print("Execution completed :: test_google_search")
    driver.quit()

def test_amazon_launch():
    '''Executing the test_amazon_launch'''
    firfox_options = webdriver.FirefoxOptions()
    driver=webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=firfox_options)
    driver.maximize_window()
    driver.get("http://www.amazon.in")
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("mouse pads", Keys.ENTER)
    print(driver.title)
    print("Execution completed :: test_amazon_launch")
    driver.quit()
