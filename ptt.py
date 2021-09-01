import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/PttHot')  #使用get取得網址
soup = BeautifulSoup(r.text, 'html.parser') #套用Beautifulsoup擷取內容 html解析器

# for span in soup.find_all('span', class_='listTitle') #透過class 找span
for span in soup.select('#list span.listTitle'): #使用select可以得到一樣的結果(

    #url = root_url + span.find('a').get('href')#or 使用屬性['href'](字典的功能 )
    href = span.find('a').get('href') #取得網頁連結
    if href =='796-59l9':
    	break

    url = root_url + href
    title = span.text #尋找標題
    
    print(f'{title}\n{url}') 
#print([s.text for s in spans])

