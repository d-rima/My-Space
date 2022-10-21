from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdm07BKViWFvya-XGTFD3nrSt0CFv2wQBE0LTxOu__Wq5weHg/viewform?usp=sf_link"
zillow_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
chrome_driver_path = r"C:\Users\dalli\Downloads\Coding\chromedriver_win32\chromedriver.exe"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}

class rental_finder:
    def __init__(self):
        self.costs = []
        self.homes = []
        self.links = []
        self.driver = webdriver.Chrome(executable_path = chrome_driver_path)

    def scrape_info(self):
        response = requests.get(zillow_URL, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        info = soup.find_all(class_="property-card-data")
        
        for item in info:
            money = item.find("span")
            address = item.find("address")
            link = item.find("a", href=True)
            self.costs.append(money.get_text()[0:6])
            self.homes.append(address.get_text())
            self.links.append(link["href"])

    def fill_out_form(self):
        self.driver.get(form_URL)
        self.original_handle = self.driver.current_window_handle
        time.sleep(5)

        for i in range(len(self.links)):
            address_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            rent_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

            address_input.send_keys(self.homes[i])
            rent_input.send_keys(self.costs[i])
            link_input.send_keys(self.links[i])

            submit_button.click()

            another_response = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()

rentalFinder = rental_finder()
rentalFinder.scrape_info()
rentalFinder.fill_out_form()
