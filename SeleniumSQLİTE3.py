from seleniumwire import webdriver
import time
from selenium.webdriver.common.by import By
import sqlite3
from selenium.webdriver.support.ui import WebDriverWait


sql = sqlite3.connect('seleniumcountryinfo.db')
c = sql.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS countryinfo(name,capital,population,area)''')

def interceptor(request):
   request.headers['New-Header'] = 'My user agent is Python 3.10.1 + Selenium 4.1.0 +Selenium Wire 4.5.6+ Windows10'

driver= webdriver.Firefox()
driver.request_interceptor = interceptor
url= "https://www.scrapethissite.com/pages/simple/"
driver.get(url)
time.sleep(5)
data= driver.find_elements(By.CLASS_NAME, "country")

insert_sql= "INSERT INTO countryinfo(name,capital,population,area) VALUES(?,?,?,?);"

for country in data:
 name= country.find_element(By.CLASS_NAME, "country-name").text.strip()
 capital= country.find_element(By.CLASS_NAME, "country-capital").text.strip()
 population= country.find_element(By.CLASS_NAME, "country-population").text.strip()
 area= country.find_element(By.CLASS_NAME, "country-area").text.strip()
 c.execute(insert_sql, (name,capital,population,area))


sql.commit()
sql.close()
