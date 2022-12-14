from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('headless')
options.add_argument('no-sandbox')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
