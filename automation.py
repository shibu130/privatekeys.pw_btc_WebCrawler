#shibu thomas 
#this code was created on 18-5-2020
#this works for windows
#the path where u have installed chrome and where u have downloaded the chromedriver for selenium
#may be different
#change the path accordingly

from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys

#file
file=open("pages_with_balance.txt","w")
# print(randint(1,2573157538607026564968244111304175730063056983979442319613448069811514699875))
def setup_driver():
    options=Options()

    #change binary location to the location where chrome/brave/chromium is installed
    options.binary_location=r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
    #change the path of the chromedriver to where u have saved it on your computer
    driver=webdriver.Chrome(executable_path=r"G:\selenium\chromedriver.exe",chrome_options=options)
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
        btcBalanceInThePage=WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,"/html/body/main/div[@class='container-fluid']/h3[@class='text-center']/span[@class='js-balances-bitcoin']/span[@class='badge badge-light']")))
        balance_on_the_page=int(btcBalanceInThePage.text)
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
            balance,page=random_page()
            if(balance>0):
                print("go to bitcoin directory page  number {} on privatekeys.pw".format(page))
                # exit(0)
                file.writelines(page+"\n")
            elif balance==0:
                #timout or execption
                balance,page=random_page(page)

                if(balance>0):
                    print("go to bitcoin directory page  number {} on privatekeys.pw".format(page))
                    # condition=False
                    file.writelines(page+"\n")
    except KeyboardInterrupt:
        file.close()
        print("crtl+d pressed")
        sys.exit()

        

                








