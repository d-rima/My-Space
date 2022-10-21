from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path=r"C:\Users\dalli\Downloads\Coding\chromedriver_win32\chromedriver.exe")
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3261868548&distance=25&f_AL=true&f_E=1%2C2%2C3&geoId=103250458&keywords=python%20developer&location=Salt%20Lake%20City%2C%20Utah%2C%20United%20States&refresh=true&sortBy=R')

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

username = driver.find_element_by_id("username")
username.send_keys("dallinrima@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Cougars0414!")

enter_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
enter_button.click()

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("3852169145")

        now_button = driver.find_element_by_css_selector("footer button")
        if now_button.text == "Next":
            exit_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            exit_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex application, skipped.")
        else:
            now_button.click()

        time.sleep(3)
        exit_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        exit_button.click()
        
    except NoSuchElementException:
        print("No apply button, skipped")
        continue
        
time.sleep(5)
driver.quit()
                                                                                    