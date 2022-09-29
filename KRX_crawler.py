import datetime
import requests
from bs4 import BeautifulSoup
URL='https://kind.krx.co.kr/disclosure/disclosurebystocktype.do'

data={
    'method': 'searchDisclosureByStockTypeEtfSub',
    'forward': 'disclosurebystocktype_etf_sub',
    'currentPageSize': '15',
    'pageIndex': '1',
    'orderMode': '1',
    'orderStat':'D',
    'etfIsuSrtCd': '',
    'reportCd': '',
    'reportTmp': '',
    'etfIsuSrtNm':'', 
    'reportNm': '신규 상장',
    'fromDate': '2022-08-05',
    'toDate': datetime.date.today(),
}
res=requests.post(URL, data=data)
soup=BeautifulSoup(res.text, 'html.parser')
results = soup.select('.list.type-00.tmt30')

final_result  = []

for result in results:
    date = result.select('.txc')[1].text.split(' ')[0]
    name = result.select_one('#etfisusum').text.strip()
    description = result.select('td > a')[1].text
    stock_result = {
    '날짜': date,
    '종목': name,
    '변경사항': description
    }
    final_result.append(stock_result)
    
    
temp=[]
for result in final_result:
    message_to_send=result['날짜']+' '+result['종목']+' '+result['변경사항']
    temp.append(message_to_send)
temp

concat_data='\n'.join(temp)

import telegram
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

key, value = config.rstrip().split('=')

bot=telegram.Bot(token)

updates = bot.get_updates()
chat_id = updates[-1].message.chat.id

#마지막 메시지를 확인한다
updates[-1].message.text

#한개로 합쳐서 전송하는 방법
bot.send_message(group_chatid,concat_data)