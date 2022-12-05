import os
import logging
from flask import Flask, jsonify
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

## logger init
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(name)s %(pathname)s %(lineno)d %(funcName)s %(levelname)s %(message)s')
sh.setFormatter(formatter)

logger.addHandler(sh)


@app.route("/")
def route():
    return "Hello World"


@app.route("/run")
def run():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    wait = WebDriverWait(driver, 10)  # Timeout 10s

    url = 'https://google.com'
    driver.get(url)
    wait.until(EC.title_contains("Google"))

    logger.info(driver.title)

    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    logger.info(driver.title)

    driver.quit()
    logger.info("quit driver")

    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))