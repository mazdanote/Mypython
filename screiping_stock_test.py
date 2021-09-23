import time
import os
import pandas as pd
import openpyxl
from selenium import webdriver


driver = webdriver.Chrome() # WebDriverのインスタンスを作成
driver.get('https://financials.morningstar.com/ratios/r.html?t=0P000000GY') # URLを指定してブラウザを開く
time.sleep(5) # 5秒待機

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen2.png")
driver.save_screenshot(FILENAME)

# print(driver.page_source)
f = open('screen.html','w')
f.write(driver.page_source)
f.close()

crypto_data = pd.read_html(driver.page_source)
print(crypto_data[0])
time.sleep(10) # 10秒待機

book = openpyxl.Workbook()
crypto_data[0].to_excel('testtest.xlsx')
ws=book.worksheet[0]
book.save('testtest.xlsx')

#==========ここから追加作業

driver.quit() # ブラウザを閉じる

#==========ここから別作業
