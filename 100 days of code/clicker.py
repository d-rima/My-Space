from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\dalli\Downloads\Coding\chromedriver_win32\chromedriver.exe")
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# dates = driver.find_elements_by_css_selector(".event-widget time")

# events = driver.find_elements_by_css_selector(".event-widget a")

# times = []
# things = []
# for time in dates:
#     times.append(time.text)
# for event in events:
#     things.append(event.text)

# dict = {}

# for i in range(5):
#     dict[f"{i}"] = times[i], things[i+1]

# print(dict)

# driver.quit()

# first_name = driver.find_element_by_name('fName')
# last_name = driver.find_element_by_name("lName")
# email = driver.find_element_by_name("email")
# button = driver.find_element_by_tag_name("button")
# first_name.send_keys("Dallin")
# last_name.send_keys("Rima")
# email.send_keys("broncos54321@gmail.com")
# button.click()

cookie = driver.find_element_by_id("cookie")

price_dict = {
    "cursor": 15,
    "grandma": 100,
    "factory": 500,
    "mine": 2000,
    "shipment": 7000,
    "alchemy lab": 50000,
    "portal": 1000000,
    "time machine": 123456789
}

def upgrade(my_cookies):
    if price_dict["time machine"] <= my_cookies:
        time_machine = driver.find_element_by_id("buyTime machine")
        time_machine.click()
        return
    if price_dict["portal"] <= my_cookies:
        portal = driver.find_element_by_id("buyPortal")
        portal.click()
        return
    if price_dict["alchemy lab"] <= my_cookies:
        alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
        alchemy_lab.click()
        return
    if price_dict["shipment"] <= my_cookies:
        shipment = driver.find_element_by_id("buyShipment")
        shipment.click()
        return
    if price_dict["mine"] <= my_cookies:
        mine = driver.find_element_by_id("buyMine")
        mine.click()
        return
    if price_dict["factory"] <= my_cookies:
        factory = driver.find_element_by_id("buyFactory")
        factory.click()
        return
    if price_dict["grandma"] <= my_cookies:
        grandma = driver.find_element_by_id("buyGrandma")
        grandma.click()
        return
    if price_dict["cursor"] <= my_cookies:
        cursor = driver.find_element_by_id("buyCursor")
        cursor.click()
        return
    
timeout = time.time() + 5
end_time = time.time() + 300

while time.time() < end_time:
    cookie.click()

    if time.time() > timeout:
        my_cookies = driver.find_element_by_id("money").text
        if ',' in my_cookies:
            my_cookies = my_cookies.replace(',', '')
        my_cookies = int(my_cookies)
        upgrade(my_cookies)
        timeout = time.time() + 5

cookies_per_second = driver.find_element_by_id("cps")
print(cookies_per_second.text)
driver.quit()