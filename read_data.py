import requests
from datetime import datetime, timedelta
import pytz
import time
from bs4 import BeautifulSoup

unit_price_url = 'https://www.asb.co.nz/iFrames/latest_unit_prices.asp'
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


def read_data(date_params):
    html = requests.post(unit_price_url, data=date_params)
    bs_obj = BeautifulSoup(html.content, features='html.parser')
    contents = bs_obj.find_all('div', class_='content')
    fund_prices = []

    for content in contents:
        fund_price = content.get_text()
        fund_prices.append(fund_price)

    for fund_name, fund_no in comparison_table.items():
        print(fund_name, ': ', fund_prices[fund_no])


def read_date_data(data_date):
    day = data_date.strftime('%d')
    month = data_date.strftime('%m')
    year = data_date.strftime('%Y')

    date_params={
        'currentDay': day,
        'currentMonth': month,
        'currentYear': year
    }

    print('{}-{}-{}'.format(year, month, day))
    read_data(date_params)


def read_period_data(start_date):
    today = datetime.now(pytz.timezone('Pacific/Auckland'))
    begin = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = today.date()

    for i in range((end - begin).days + 1):
        data_date = begin + timedelta(days=i)
        read_date_data(data_date)
        time.sleep(5)


read_period_data('2020-04-16')
