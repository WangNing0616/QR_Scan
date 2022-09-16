#!/usr/bin/env python
# encoding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests

url1='https://qrtracing.wdc.com/api/sdss/entrance'
data1={'EntranceId':'SDSS-B2 Entrance','EmpId':'1000300382','Temperature':'36.0','GUID':'41ba7bc3-8b4e-4d34-b758-efcfe6578ea5','PageServerId':'Gui-2','TestedCovid':'0','Travel':'0','CloseContact':'0','Fever':'0','Chills':'0','Cough':'0','SoreThroat':'0','LoseSmellTaste':'0','ShortnessBreath':'0'}
headers1={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
   'Referer':'https://qrtracingpage.wdc.com/'
   }
sourse1=requests.post(url1,data=data1,headers=headers1).text
print(sourse1)

url2='https://qrtracing.wdc.com/api/sdss/room'
data2={'RoomId':'SDSS 2F Office','TableId':'295','SeatId':'1','EmpId':'1000300382','GUID':'1d9b3af4-8fa5-4e50-ab54-8a25fae51dd0','PageServerId':'Gui-3'}
headers2={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
   'Referer':'https://qrtracingpage.wdc.com/'
   }
sourse2=requests.post(url2,data=data2,headers=headers2).text
print(sourse2)

browser = webdriver.Chrome()
browser.get("http://cvppasip02/SPAS/")
browser.maximize_window()

# webpage1
# browser.switch_to.frame(r'formleft')
# browser.find_element_by_id(r'txtBadgeID').clear()
# browser.find_element_by_id(r'txtBadgeID').send_keys(username)
# browser.find_element_by_id(r'txtPassword').clear()
# browser.find_element_by_id(r'txtPassword').send_keys(password)
# browser.find_element_by_xpath(r'//*[@id="cmdLogin"]').click()  # Login
# time.sleep(1)
browser.switch_to.parent_frame()
browser.switch_to.frame(r'main')
#browser.find_element_by_xpath(r'//*[@id="Form1"]/font/table/tbody/tr[2]/td/a[1]').click() 
browser.find_element_by_xpath(r'//*[@id="linkMeal"]').click()
time.sleep(1)
#time.sleep(1) 
#browser.find_element_by_xpath(r".//*[@id='cmdMealCode']/option[2]").click()
Select(browser.find_element_by_name("cmbMealCode")).select_by_value('M2:晚餐')
time.sleep(1)
#Select(browser.find_element_by_name("cmbMealCode")).select_by_value('M3:半夜餐')
#Select(browser.find_element_by_name("cmbMealCode")).select_by_value('M4:次日早餐')
Select(browser.find_element_by_name("cmbMealName")).select_by_value('F1:米饭')
time.sleep(1)
browser.find_element_by_xpath(r".//*[@id='cmdSubmit']").click()
time.sleep(5)
browser.quit()

# try:
#     time.sleep(1)
#     browser.find_element_by_id(r'lnkNextDown').click()
# except:
#     time.sleep(1)
#     browser.find_element_by_id(r'lnkNextDown').click()

# try:
#     time.sleep(1)
#     browser.find_element_by_id(r'btnSave').click()
# except:
#     time.sleep(1)
#     browser.find_element_by_id(r'btnSave').click()

# try:
#     time.sleep(1)
#     browser.find_element_by_id(r'req_list_btnTopSubmit_0').click()
# except:
#     time.sleep(1)
#     browser.find_element_by_id(r'req_list_btnTopSubmit_0').click()

input('Press Enter to Exit')
