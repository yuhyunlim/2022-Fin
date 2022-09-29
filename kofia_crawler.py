from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\choig\Desktop\workspace\chromedriver.exe")
#사이트에 접속
driver.get("https://freesis.kofia.or.kr/")
time.sleep(9) 
driver.switch_to.frame('main')
driver.find_element(By.XPATH, '//*[@id="TopMenuSub"]/ul/li[5]/a/img').click()
time.sleep(3) 

#내부 항목으로 들어가기
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[5]/div/div/div[3]/div/div/div/div[5]/div[2]/div[1]/div').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[5]/div/div/div[3]/div/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[5]/div/div/div[3]/div/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div').click()
time.sleep(5)

#엑셀 파일 다운로드 버튼 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/div[5]/div/div[2]/div/div/div/div[1]/div/div[6]/div/div/div[10]/div/div[1]/div/div[4]/div/div/div[6]').click()
time.slee(3)

#텔레그램으로 전송하기
import telegram
import datetime
today=datetime.date.today()
#토큰으로 봇에 접근
telegram_config={}
with open('./telegram_config','r') as f:
    configs=f.readlines()
    for config in configs:
        key, value=config.rstrip().split('=')
        telegram_config[key]=value
token=telegram_config['token']
my_chatid=telegram_config['chatID'] #내 봇방에 보내는 키
group_chatid=telegram_config['groupID'] #단톡방에 접근하는 키

bot=telegram.Bot(token)
updates = bot.get_updates()
bot.sendDocument(my_chatid, open(r'C:\Users\choig\Downloads\집합투자기구구분.xlsx','rb'))
bot.sendMessage(my_chatid, '오늘자 금투협 자료입니다')
