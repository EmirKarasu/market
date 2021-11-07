from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\path\to\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")
driver.quit()