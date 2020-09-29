import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import json


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


def printLines(message):
    line = ("-"*35).center(messageMargin)

    print(line)

    if type(message) == list:
        for i in message:
            print(i.center(messageMargin))
    else:
        message = message.center(messageMargin)
        print(message)

    print(line)


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
    
    dollarPrices = dict()
    pages = list()
    for div in data:
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

    return dollarPrices

def calculateAverage(dollarPricesData):
    pricesList = list()

    for pageName in dollarPricesData:
        if pageName != 'AirTM' and pageName != 'PayPal':
            price = dollarPricesData[pageName]
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
