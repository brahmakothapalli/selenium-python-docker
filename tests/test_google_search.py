''' this module contains tests to sequentially'''
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_my_blog_search():
    '''Executing the test_google_search'''
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://www.google.com")
    driver.find_element(By.NAME , "q").send_keys("brahmakothapalli.hashnode.com", Keys.ENTER)
    print(driver.title)
    print("Execution completed :: test_google_search")
    driver.quit()

def test_my_channel_youtube_search():
    '''Executing the test_google_search'''
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://www.google.com")
    # driver.find_element(By.ID , "search-input").click()
    driver.find_element(By.NAME , "q").send_keys("@brahmakothapalli youtube", Keys.ENTER)
    print(driver.title)
    print("Execution completed :: test_youtube_search")
    sleep(5)
    driver.quit()