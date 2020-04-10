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
    line = ("_"*35).center(messageMargin)

    print(line)

    if type(message) == list:
        for i in message:
            print(i.center(messageMargin))
    else:
        message = message.center(messageMargin)
        print(message)

    print(line)


def getDollarPrices():

    data = soup.find_all("div", class_="module-moneda")
    exceptions = ['Mesas de Cambio',
                  '100% Banco',
                  'BBVA Provincial',
                  'BNC',
                  'Bancamiga',
                  'BanCaribe',
                  'Banco Activo',
                  'Banco Exterior',
                  'Banco Mercantil',
                  'Banplus',
                  'BVC',
                  'Banco de Venezuela',
                  'Banesco',
                  'Citibank',
                  'Otras Instituciones',
                  'Banco Plaza',
                  'Italcambio',
                  'Remesas Zoom',
                  'Insular',
                  'Cotizaciones',
                  'MoviCambios']
    dollarPrices = dict()
    pages = list()
    for div in data:
        pageName = div.find("p1")
        if (pageName):
            pageName = pageName.text
            pages.append(pageName)
            if (pageName not in exceptions):
                pagePrice = div.find("p2").text
                dollarPrices[pageName] = pagePrice

    # Uncomment to see an array with all page names
    #
    # print(pages)

    # W Uncomment to generate json file (you must import json)
    #
    # with open('dollarPrices.json', 'w') as f:
    #     json.dump(dollarPrices, f)

    return dollarPrices


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
    if pageName != 'Dolar Promedio':
        message = formatParameters.format(pageName, dollarPrices[pageName])
        print(message.center(messageMargin))


# Footer
average = dollarPrices['Dolar Promedio']
averageMessage = formatParameters.format("Promedio", average)
printLines(averageMessage)
