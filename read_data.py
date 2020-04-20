import requests
from bs4 import BeautifulSoup

unitPriceUrl = 'https://www.asb.co.nz/iFrames/latest_unit_prices.asp'
params = {
    'currentDay': '7',
    'currentMonth': '4',
    'currentYear': '2020'
}
comparison_table = {'Balanced Fund':0,
                    'Conservative Fund':1,
                    'Conservative Plus Fund':2,
                    'Global Property Shares Fund':3,
                    'Growth Fund':4,
                    'Moderate Fund':5,
                    'Positive Impact Fund':6,
                    'World Fixed Interest Fund':7,
                    'World Shares Fund':8
                    }
fund_prices = []


def read_data(page_html):
    bs_obj = BeautifulSoup(page_html.content, features='html.parser')
    contents = bs_obj.find_all('div', class_='content')

    for content in contents:
        fund_price = content.get_text()
        fund_prices.append(fund_price)

    for fund_name, fund_no in comparison_table.items():
        print(fund_name, ': ', fund_prices[fund_no])


html = requests.post(unitPriceUrl, data=params)
read_data(html)
