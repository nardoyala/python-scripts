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


<<<<<<< HEAD
def printLines(message, margin):
    line = ("-"*35).center(margin)
=======
def printLines(message):
    line = ("-"*35).center(messageMargin)
>>>>>>> 6cea424355d60c0fa95c2ebb66efef773e354f74

    print(line)

    if type(message) == list:
        for i in message:
            print(i.center(margin))
    else:
        message = message.center(margin)
        print(message)

    print(line)


<<<<<<< HEAD
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
=======
def getDollarPrices():

    data = soup.find_all("div", class_="c-nombre")
    validPages = ['AirTM',
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
                  'Yadio']
    
>>>>>>> 6cea424355d60c0fa95c2ebb66efef773e354f74
    dollarPrices = dict()

    for div in data:
<<<<<<< HEAD
        pageName = div.find("h2", class_="nombre").text
        if (pageName == 'Monitor Dolar Venezuela'):
            pageName = 'Monitor Dolar'
        if (pageName in validPages):
            pagePrice = div.find("p", class_="precio").text
            pagePrice = float(pagePrice.replace('.','').replace(',', '.'))
            dollarPrices[pageName] = pagePrice
=======
        pageName = div.find("h2", class_="nombre")
        if (pageName):
            pageName = pageName.text
            pages.append(pageName)
            if (pageName in validPages):
                pagePrice = div.find("p", class_="precio").text
                dollarPrices[pageName] = pagePrice

    # Uncomment to see an array with all page names
    #
    # print(pages)

    # Uncomment to generate json file (you must import json)
    #
    # with open('dollarPrices.json', 'w') as f:
    #     json.dump(dollarPrices, f)
>>>>>>> 6cea424355d60c0fa95c2ebb66efef773e354f74

    return dollarPrices

def calculateAverage(dollarPricesData):
    pricesList = list()

    for pageName in dollarPricesData:
        if pageName != 'AirTM' and pageName != 'PayPal':
            price = dollarPricesData[pageName]
<<<<<<< HEAD
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
=======
            formattedPrice = float(price.replace('.','').replace(',', '.'))
            pricesList.append(formattedPrice)

    average = str(round(sum(pricesList) / len(pricesList), 2))
    averageTuple = average.split('.')
    averageTuple[0] = str('{:,}'.format(int(averageTuple[0])).replace(',','.'))
    formattedAverage =  ','.join(averageTuple)
    return formattedAverage

response = requests.get('https://exchangemonitor.net/ve')
soup = BeautifulSoup(response.text, 'html.parser')

messageMargin = 50

# Header
today = datetime.now()
date = customDateFormat(today)
title = "Precio del dólar"
printLines([title, date])

# Dollar prices table
dollarPrices = getDollarPrices()
formatParameters = "{:<20} : {:>10}"

for pageName in dollarPrices:
    if pageName != 'ExchangeMonitor.net':
        message = formatParameters.format(pageName, dollarPrices[pageName])
        print(message.center(messageMargin))


# Footer
average = calculateAverage(dollarPrices)
averageMessage = formatParameters.format("Promedio", average)
printLines(averageMessage)
>>>>>>> 6cea424355d60c0fa95c2ebb66efef773e354f74
