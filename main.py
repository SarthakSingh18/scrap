from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pymysql

def click():
    driver.find_element_by_id("widgetField").click()
    driver.find_element_by_id("startDate").clear()
    inputElement = driver.find_element_by_id("startDate")
    inputElement.send_keys("04/01/2016")
    driver.find_element_by_id("applyBtn").click()
    return

def dataBase():
    connection=pymysql.connect(host="localhost",user="temp",password="temp",db="temp",port=3306)
    mycursor=connection.cursor()
    table = soup.find("table", {"id": "curr_table"})
    rows = table.find_all('tr')
    for row in rows[1:]:
        data = row.find_all('td')
        dateTime=data[0].text
        cost=data[1].text
        print(dateTime)
        query="INSERT INTO data(date,price) values (%s,%s)"
        arguments=(dateTime,cost)
        mycursor.execute(query,arguments)
        connection.commit()
    return

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.investing.com/equities/tata-consultancy-services-historical-data")
click()
time.sleep(5)
soup=BeautifulSoup(driver.page_source,features="html.parser")
dataBase()