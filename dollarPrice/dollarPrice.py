import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://exchangemonitor.net/ve'
MARGIN = 50

def customDateFormat(date):
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


def printLines(message, margin):
    line = ("-"*35).center(margin)

    print(line)

    if type(message) == list:
        for i in message:
            print(i.center(margin))
    else:
        message = message.center(margin)
        print(message)

    print(line)


def getDollarPrices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find_all('div', class_='c-nombre')
    validPages = (
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
    dollarPrices = dict()

    for div in data:
        pageName = div.find("h2", class_="nombre").text
        if (pageName == 'Monitor Dolar Venezuela'):
            pageName = 'Monitor Dolar'
        if (pageName in validPages):
            pagePrice = div.find("p", class_="precio").text
            pagePrice = float(pagePrice.replace('.','').replace(',', '.'))
            dollarPrices[pageName] = pagePrice

    return dollarPrices

def calculateAverage(dollarPricesData):
    pricesList = list()

    for pageName in dollarPricesData:
        if pageName != 'AirTM' and pageName != 'PayPal':
            price = dollarPricesData[pageName]
            pricesList.append(price)

    average = round(sum(pricesList) / len(pricesList), 2)
    return average

def formatNumber(number):
    number = format(number, '.2f')
    integerPart = number.split('.')[0]
    integerPart = format(int(integerPart), ',').replace(',', ' ')
    decimalPart = number.split('.')[1]
    formattedNumber = integerPart + "," + decimalPart
    return formattedNumber

def printDollarPricesTable():
    dollarPrices = getDollarPrices(URL)
    formatParameters = "{:<20} : {:>10}"

    # Header
    today = datetime.now()
    date = customDateFormat(today)
    title = "Precio del dólar"
    printLines([title, date], MARGIN)

    # Dollar prices table
    for pageName in dollarPrices:
        dollarPrice = dollarPrices[pageName]
        formattedDollarPrice = formatNumber(dollarPrice)
        message = formatParameters.format(pageName, formattedDollarPrice)
        print(message.center(MARGIN))

    # Footer
    average = calculateAverage(dollarPrices)
    formattedAverage = formatNumber(average)
    averageMessage = formatParameters.format("Promedio", formattedAverage)
    printLines(averageMessage, MARGIN)

if __name__ == '__main__' :
    printDollarPricesTable()
