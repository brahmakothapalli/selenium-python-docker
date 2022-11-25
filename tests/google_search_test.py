from selenium import webdriver
import time

ff_options = webdriver.FirefoxOptions()
# pointing the selenium tests to selenium grid url
# driver = webdriver.Remote(command_executor="http://172.17.0.2:4444/wd/hub", options=ff_options)

# local driver initalization
driver = webdriver.Firefox()

driver.get("http://www.google.com")
time.sleep(5)
driver.maximize_window()
print("Title of the application :: "+driver.title)
driver.quit()
print("Executed the test successfully")