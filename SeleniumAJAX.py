from seleniumwire import webdriver
import time
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from bson.json_util import loads, dumps

def interceptor(request):
	request.headers['New-Header'] = 'My user agent is Python 3.10.1 + Selenium 4.1.0 +Selenium Wire 4.5.6+ Windows10'
	driver.request_interceptor = interceptor
driver = webdriver.Firefox()
url = "https://www.scrapethissite.com/pages/ajax-javascript/"
driver.get(url)
time.sleep(10)
filmten = driver.find_elements(By.CLASS_NAME, "year-link")
for years in filmten:
	time.sleep(5)
	yearclick=years.click()
	time.sleep(5)
	driver.implicitly_wait(5)
	data = driver.find_elements(By.CLASS_NAME, "film")
	for datas in data:
		datas = {'film_title': datas.find_element(By.CLASS_NAME, "film-title").text.strip(),
				'film_nominations': datas.find_element(By.CLASS_NAME,"film-nominations").text.strip(),
				'film_awards': datas.find_element(By.CLASS_NAME, "film-awards").text.strip(),
				'film_best_picture': datas.find_element(By.CLASS_NAME,"film-best-picture").text.strip()
				}
		client = MongoClient('mongodb://localhost:*****/')
		myMDBD = client["Testfilm"]
		collection = myMDBD['test-film']
		result = dumps(datas)
		finalresult = loads(result)
		execute = myMDBD.collection.insert_one(finalresult)
		driver.implicitly_wait(5)
		time.sleep(5)
