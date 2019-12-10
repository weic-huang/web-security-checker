from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import sys

url = sys.argv[1]
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

browser.save_screenshot(url)
print ('done')
sys.stdout.flush()
