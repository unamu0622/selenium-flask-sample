from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 10)  # Timeout 10s

driver.get('https://google.com')
wait.until(EC.title_contains("Google"))

logger.info(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
logger.info(driver.title)

driver.quit()
logger.info("quit driver")
