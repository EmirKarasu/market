from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

print("sample test case started")

#chrome_options = Options()
#chrome_options.add_argument("--disable-infobars")
#driver1 = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome(r"C:\Users\Dell\PycharmProjects\pythonProject\Browsers\chromedriver.exe")

#for i in range(0,11):
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=yNAhL7ND6gU&t=42s")
time.sleep(2)
driver.find_element_by_name("").send_keys(Keys.SPACE)
time.sleep(3)
driver.close()




