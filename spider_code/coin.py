import json
import pymysql
import requests
from bs4 import BeautifulSoup as bs

def conn():
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="encryption_currency",
        charset="utf8mb4",
    )
    return con
    # soup = bs(re)

def insert(con, item):
    cur = con.cursor()
    sql = """
    insert coin (ID, name, symbol, date, time_high, time_low, open, high, low, close, volume, market_cap)
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, tuple(item.values()))
    con.commit()

# 解析json格式数据，并进行数据清洗，时间缺失值补充为交易关闭时间(大约投2-3种币有缺失)
def unpack_json(json_data):
    data = json_data['data']
    # 数字货币的名字
    name = data['name']
    # 数字货币的缩写
    symbol = data['symbol']
    # 报价,价格数组集合
    quotes = data['quotes']
    for quote in quotes:
        date = quote['timeClose'].split('T')[0]
        if 'timeHigh' in quote:
            time_high = str(quote['timeHigh'])
        else:
            time_high = str(quote['timeClose'])
        time_high = time_high.replace("T"," ")
        time_high = time_high.replace(".000Z","")
        time_high = time_high.replace(".999Z","")
        if 'timeLow' in quote:
            time_low = str(quote['timeLow'])
        else:
            time_low = str(quote['timeClose'])
        time_low = time_low.replace("T"," ")
        time_low = time_low.replace(".000Z","")
        time_low = time_low.replace(".999Z","")
        # 价格数据
        q = quote['quote']
        open = q['open']
        high = q['high']
        low = q['low']
        close = q['close']
        # 成交量
        volume = q['volume']
        # 市值
        market_cap = q['marketCap']
        # 定义item
        item = {}
        item['ID'] = 0
        item['name'] = name
        item['symbol'] = symbol
        item['date'] = date
        item['time_high'] = time_high
        item['time_low'] = time_low
        item['open'] = open
        item['high'] = high
        item['low'] = low
        item['close'] = close
        item['volume'] = volume
        item['market_cap'] = market_cap
        yield item

if __name__ == '__main__':
    id_dic = {'BTC':1,'ETH':1027,'USDT':825,'BNB':1839,'ADA':2010,'XRP':52,'DOGE':74,'USDC':3408,'DOT':6636,'UNI':7083,'BUSD':4687,'BCH':1831,'LTC':2,'SOL':5426,'LINK':1975,'WBTC':3717,'MATIC':3890,'THETA':2416,'ETC':1321,\
    'XLM':512,'DAI':4943,'ICP':8916,'VET':3077,'FIL':2280,'TRX':1958,'EOS':1765,'AAVE':7278,'XMR':328,'LUNA':4172,'CRO':3625,'SHIB':5994,'CAKE':7186,'ATOM':3794,'FTT':4195,'LEO':3957,'ALGO':4030,'MKR':1518,'BSV':3602,\
        'BTCB':4023,'XTZ':2011,'KLAY':4256,'NEO':1376,'AMP':6945,'COMP':5692,'MIOTA':1720,'AVAX':5805,'GRT':6719,'UST':7129,'TFUEL':3822,'KSM':5034,'DCR':1168,'EGLD':6892,\
        'BTT':3718,'HT':2502,'HBAR':4642,'TUSD':2563,'WAVES':1274,'CHZ':4066,'STX':4847,'SNX':2586,'CEL':2700,'RUNE':4157,'DASH':131,'ZEC':1437,'YFI':5864,'MANA':1966,\
            'XDC':2634,'HNT':5665,'XEM':873,'ENJ':2130,'KCS':2087,'AXS':6783,'SUSHI':6758,'TEL':2394,'HOT':2682,'QNT':3155,'PAX':3330,'NEXO':2694,'FLOW':4558,'NEAR':6535,\
                'MDX':8335,'ZIL':2469,'BAT':1697,'ONE':3945,'BTG':2083,'CELO':5567,'BNT':1727,'ZEN':1698,'CRV':6538,'QTUM':1684,'ZRX':1896,'OKB':3897,'CHSB':2499,'SC':1042,\
                    'ONT':2566,'NANO':1567,'DGB':109,'FTM':3513,'AR':5632,'ICX':2099}
    con = conn()
    # url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=2010&convertId=2781&timeStart=1215792000&timeEnd=1626019200"
    for key,value in id_dic.items():
        url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={value}&convertId=2781&timeStart=1215792000&timeEnd=1626019200"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
        }
        # print(url)
        response = requests.get(url,headers=headers)
        soup = bs(response.text, "lxml")
        data = soup.select("p")#把ul.rank.list下的li全部爬取下来
        str_data = data[0].get_text()
        json_data = json.loads(str_data)
        for item in unpack_json(json_data):
            # with open(f"data/{key}.txt","a") as f:
            #     f.write(str(item))
            #     f.write('\n')
            insert(con, item)
