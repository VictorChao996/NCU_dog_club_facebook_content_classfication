from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import getpass
import bs4
import os

import utils.files as files
import utils.manipulate as manipulate

load_dotenv()
# 所有要建立的file 名稱 list
fileList = ['noon.txt', 'afternoon.txt', 'night.txt', 'person_leave.txt', 'other.txt', 'medical_treatment.txt']
openUrl = os.environ.get("URL")
# renew txt record file 
files.deleteCollection(fileList)
files.createCollection(fileList)

# 關閉notification 直接進入網頁
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# 跳過notification，讓selenium可以繼續執行下面的階段
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get(openUrl)
sleep(2)
driver.maximize_window()

# 輸入臉書帳號 & 密碼
email =  driver.find_element(By.NAME, 'email')
password =  driver.find_element(By.NAME, 'pass')
email.send_keys(os.environ.get('USER'))
password.send_keys(os.environ.get('PASSWORD'))
password.submit()

sleep(1)

#模擬滑鼠滾輪滾動(為了動態加載臉書社團頁面)
manipulate.scrollCollection(3, driver);

sleep(2)
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
#嘗試從比較大的層級去抓取人名 & 相對應的貼文內容
paragraph_titles = soup.findAll("div", class_ = "x1cy8zhl x78zum5 x1q0g3np xod5an3 x1pi30zi x1swvt13 xz9dl7a")
# print(paras_computer)
authors = []
for para in paragraph_titles:
    # 紀錄當前 para 要印出的所有訊息
    tempString = ""
    name = para.find("strong")
    if name is not None:
        author_name_span = name.find("span")
        if author_name_span is not None:
            # If <span> tag exists within <strong> tag, extract its text content
            author_name = author_name_span.text
            # print("發文者:", author_name)
            tempString += "發文者: " + author_name + "\n"
            authors.append(tempString)
paragraph_content = soup.findAll("div", class_="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a")

# 擷取文章作者 & 內容
tempString = ""
for i in range(0, min(len(paragraph_content), len(authors))):
    tempString += authors[i]
    tempString += paragraph_content[i].text
    # 根據當前文章的關鍵字做分類
    files.classifyRecords(tempString)
    tempString = ""
sleep(10)