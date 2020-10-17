import requests
from bs4 import BeautifulSoup
from datetime import datetime

def custom_date_format(date):
    months = ["Enero",
              "Febrero",
              "Marzo",
              "Abril",
              "Mayo",
              "Junio",
              "Julio",
              "Agosto",
              "Septiembre",
              "Octubre",
              "Noviembre",
              "Diciembre"]
    day = date.day
    month = months[date.month - 1]
    year = date.year

    message = "{} de {} de {}".format(day, month, year)
    return message


def print_lines(message, margin):
    line = ("-"*35).center(margin)

    print(line)

    if type(message) == list:
        for i in message:
            print(i.center(margin))
    else:
        message = message.center(margin)
        print(message)

    print(line)


def get_dollar_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find_all('div', class_='c-nombre')
    valid_pages = (
                    'AirTM',
                    'BolivarCucuta',
                    'CucutaDivisas',
                    'DolarToday',
                    'DolarToday (BTC)',
                    'DolarTrue',
                    'Dolar Promedio',
                    'DolarSatochi',
                    'ExchangeMonitor.net',
                    'LocalBitcoins',
                    'Mkambio',
                    'Monitor Dolar',
                    'PayPal',
                    'Yadio'
    )
    dollar_prices = dict()

    for div in data:
        page_name = div.find("h2", class_="nombre").text
        if (page_name == 'Monitor Dolar Venezuela'):
            page_name = 'Monitor Dolar'
        if (page_name in valid_pages):
            page_price = div.find("p", class_="precio").text
            page_price = float(page_price.replace('.','').replace(',', '.'))
            dollar_prices[page_name] = page_price

    return dollar_prices

def calculate_average(dollar_prices_data):
    prices_list = list()

    for page_name, dollar_price in dollar_prices_data.items():
        if page_name != 'AirTM' and page_name != 'PayPal':
            prices_list.append(dollar_price)

    average = round(sum(prices_list) / len(prices_list), 2)
    return average

def format_number(number):
    number = format(number, '.2f')
    integer_part = number.split('.')[0]
    integer_part = format(int(integer_part), ',').replace(',', ' ')
    decimal_part = number.split('.')[1]
    formatted_number = integer_part + "," + decimal_part
    return formatted_number

def run():
    URL = 'https://exchangemonitor.net/ve'
    MESSAGE_MARGIN = 50
    FORMAT_PARAMETERS = "{:<20} : {:>10}"
    dollar_prices = get_dollar_prices(URL)

    # Header
    today = datetime.now()
    date = custom_date_format(today)
    title = "Precio del dólar"
    print_lines([title, date], MESSAGE_MARGIN)

    # Dollar prices table
    for page_name, dollar_price in dollar_prices.items():
        formatted_dollar_price = format_number(dollar_price)
        message = FORMAT_PARAMETERS.format(page_name, formatted_dollar_price)
        print(message.center(MESSAGE_MARGIN))

    # Footer
    average = calculate_average(dollar_prices)
    formatted_average = format_number(average)
    average_message = FORMAT_PARAMETERS.format("Promedio", formatted_average)
    print_lines(average_message, MESSAGE_MARGIN)

if __name__ == '__main__' :
    run()
