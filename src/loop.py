from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from notify import notification
from server import server
from tabulate import tabulate
from dictionnary import server_list
import time

class loop:
    def boucle(Xpath):
        PATH = '.\chromedriver.exe'
        driver = webdriver.Chrome(PATH)
        driver.get('https://vente.tryandjudge.com/dofuskamas.php')
        
        
        while True:
            try:
                sell = driver.find_element_by_xpath(Xpath)        
                sell.click()
                notification('Jri jri rah t7aal',title="bi3 Kama")
                    
            except:
                print("Not yet")
                time.sleep(5)
                driver.refresh()
