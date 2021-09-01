#shibu thomas 
#this code was created on 18-5-2020
#this works for windows
#the path where u have installed chrome and where u have downloaded the chromedriver for selenium
#may be different
#change the path accordingly

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 9000  # Set Duration To 1000 ms == 1 second
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import selenium.common.exceptions

file = open('out.txt', 'a')


def setup_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument("disable-gpu")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    driver = webdriver.Chrome()
    return driver

def random_page(last_page=None):
    try:
        page_number=randint(1,2573157538607026564968244111304175730063056983979442319613448069811514699875)
        driver=setup_driver()
        #change line 38 with below for checking different type of address
        #driver_url=https://privatekeys.pw/bitcoin-segwit/keys/+str(page_number)
        #driver_urlhttps://privatekeys.pw/bitcoin-segwit-p2sh/keys/+str(page_number)  
        #driver_url="https://privatekeys.pw/bitcoin/keys/"+str(page_number)
        driver_url="https://privatekeys.pw/bitcoin/keys/"+str(page_number)
        driver.get(driver_url)
        btcBalanceInThePage=WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,"/html/body/main/div[@class='container-fluid']/h3[@class='text-center']/span[@class='js-balances-bitcoin']/span[contains(@class, 'badge badge-success') or contains(@class, 'badge badge-light')]")))
        balance_on_the_page=float(btcBalanceInThePage.text)
        driver.close()
    except Exception:
        balance_on_the_page=0
        # page_number=None
        print("timeout retrying......")
        driver.close()
    return (balance_on_the_page,page_number)


if __name__ == "__main__":
    condition=True
    try:
        while(condition):
             if balance > 0:
                with open('out.txt', 'a') as f:
                    print("go to bitcoin directory page number {} on privatekeys.pw".format(page), file=f)
                    winsound.Beep(frequency, duration)
                #u want to stop here once u find a page with actual balance ? uncomment line 60
                # exit(0)
                # file.writelines(page+"\n")
            # elif balance==0:
            #     #timout or execption
            #     balance,page=random_page(page)

            #     if(balance>0):
            #         print("go to bitcoin directory page  number {} on privatekeys.pw".format(page))
            #         # condition=False
            #         file.writelines(page+"\n")
    except KeyboardInterrupt:
        file.close()
        print("crtl+d pressed")
        sys.exit()

    except selenium.common.exceptions.NoSuchWindowException:
        file.close()
        print("browser window closed")
        sys.exit()

        

                








