from selenium import webdriver
import os
import time

def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/headless-chromium"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome("/opt/chromedriver",
                              options=options)
 # Login to Miner
    driver.get("https://www.monero.crypto-webminer.com/")
    time.sleep(20)

# click Wallet Box
    driver.find_element(By.XPATH, "/html/body/div[3]/input").click
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

    