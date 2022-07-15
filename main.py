import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os



###
from flask import Flask

app = Flask(__name__)


@app.route("/")

def home_view():
        #return "<h1>Welcome to Geeks for Geeks</h1>"
        return hello_world()




def hello_world():
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
   # chrome_prefs = {}
    #chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
   # chrome_prefs["profile.default_content_settings"] = {"images": 2}

    driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), options=chrome_options)
    
# Login to Miner
    driver.get("https://www.monero.crypto-webminer.com/")
    time.sleep(20)

# click Wallet Box
    driver.find_element(By.ID, "wallett").click
    time.sleep(2)


# enter wallet address
    driver.find_element(By.XPATH, "/html/body/div[3]/input").send_keys("49KVg3wibjaMEwoUa7jaRZRs87Bi4Q3avLFeidLmq5WgKm7khYi48b37DxvQzdCTPyLfwwaS1zrCPQaTHSCgENSbEx3M61M")
    print("Wallet Address Entered!")
    time.sleep(2)


# press enter

    #driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/table/tbody/tr/td[3]/div[2]/input").send_keys(Keys.RETURN)
    #print("Login done!")
    #time.sleep(9)

# Keyboard Controls

    element = driver.find_element(By.XPATH, "/html/body/button")
    driver.execute_script("arguments[0].click();", element)

    print("Script running...")


    time.sleep(840)



    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)





    time.sleep(840)

    







#if __name__ == "__main__":
    #hello_world()
 #   app.debug = True
  #  app.run()