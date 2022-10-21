import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}

# Returns all the data from the website
page = requests.get(URL, headers = headers)


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title").get_text()
    company_element = job_element.find("h3", class_="company").get_text()
    location_element = job_element.find("p", class_="location").get_text()
    print(title_element.strip())
    print(company_element.strip())
    print(location_element.strip())
    print()

