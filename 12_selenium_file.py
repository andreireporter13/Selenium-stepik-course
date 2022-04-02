# Try to make a new Selenium script;
from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By

# import needed libraries for selenium; 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# import another important libraries 
import math 
import time


# Firefox important options; 
options = webdriver.FirefoxOptions()
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0')
options.add_argument('--disable-blink-features=AutomationControlled')
firefox_service = Service(executable_path='/home/andy/Documents/selenium-course-exercises/geckodriver')


# Make a first important function; 
def gather_data(link):

    try: 
        browser = webdriver.Firefox(service=firefox_service, options=options)
        browser.get(link)

        by_now = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
        button.click()

        
        x_element = browser.find_element(By.ID, 'input_value').text
        x = int(x_element)
       
        result = math.log(abs(12*math.sin(x)))

        input_label = browser.find_element(By.ID, 'answer')
        input_label.send_keys(result)

        button_submit = browser.find_element(By.ID, 'solve').click()

        
    except Exception as ex: 
        print(ex)

    finally: 
        # set time and quit for web driver; 
        time.sleep(20)
        browser.quit()
        

# main function; 
def main():
    gather_data('http://suninjuly.github.io/explicit_wait2.html')


# important things - name == __main__ 
if __name__ == '__main__':
    main()
