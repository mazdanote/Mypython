#pthon(Anaconda)とwebdriver.Choromeを使ってスクレイピングのプログラムを自作しようとしたが全くついてゆけませんでした。やりたいことは明確なのに時間だけが過ぎてしまいます。一般的には簡単な部類のプログラミングだと思われますが今の自分に作ることは難しいです。
#mizuho銀行の宝くじ"ナンバーズ3"の1回目～直近の回の全データを取得したいです。
#取得していただきたいデーターは↓「 '回別'（第1回）　'当選日'（1994年10月7日）　'抽選数字'(191) 」
#上記のデーターを自動取得後に、さらに自動でCSV形式でアウトプットされデーターとして使えるところまでお願いしたいです。

import csv
import urllib
import time
from bs4 import BeautifulSoup

url = 'https://dubai.dubizzle.com/motors/used-cars/?page=1'  # 取得先URL
num_pages = 3  # 取得ページ数
request_interval = 1  # ページ取得間隔

data = []
for i in range(0, num_pages + 1):
    url = urllib.parse.urljoin(url, '?page=0'+str(i))
    print('getting page... ', url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    # 自分の環境では、lxml が使えなかったので、以下の 'html.parser' を使いました。
    # soup = BeautifulSoup(html, 'html.parser')
    a_elems = soup.select('div.item-name > a')

    for item_elems in soup.select('div.list-item-wrapper'):
        # 年代、走行距離
        li_elems = item_elems.select('ul.features > li')
        year = li_elems[0].text.replace('Year: ', '')  # 年代
        km = li_elems[1].text.replace('Kilometers: ', '')  # 走行距離
        # メーカー、種類
        breads = item_elems.select('p.breadcrumbs')[0].text
        breads = [s.replace('\u202a', '').strip() for s in breads.split('>‪')]  # \u202a は消す
        maker = breads[1]
        car_type = breads[2]
        # 値段
        price_elem = item_elems.select('div.price')[0]
        price = price_elem.text.replace(',', '').replace('AED', '').strip()  # , と AED は消す
        # リンク
        a_elem = item_elems.select('h3 a')[0]
        car_url = urllib.parse.urljoin(url, a_elem.get('href'))
        title = a_elem.text.strip()

        data.append({
            'year': year, 
            'km': km, 
            'maker': maker, 
            'type': car_type, 
            'price': price, 
            'title': title, 
            'url': car_url
        })

with open('output.csv', 'w', encoding='utf-8') as f:
    # 列の出力順序を規定
    fields = ['title', 'url', 'maker', 'type', 'year', 'km', 'price']

    writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()  # ヘッダー出力
    writer.writerows(data)  # データ出力
print('complete')