import requests
from bs4 import BeautifulSoup
from datetime import datetime

def replaceMultiple(mainString, toBeReplaces, newString):
  for elem in toBeReplaces:
    if len(newString) == 1:
      if elem in mainString:
        mainString = mainString.replace(elem, newString)
    else:
      if elem in mainString:
        toBeReplacesIndex = toBeReplaces.index(elem)
        newStringIndex = toBeReplacesIndex
        mainString = mainString.replace(elem, newString[newStringIndex])
  return  mainString

def formatNumber(number):
  decimalPart = str(round(number - int(number), 2))
  decimalPart = decimalPart.replace(".",",")
  number = str(int(number))
  numberList = []
  numberFormatted = ''
  counter = 0

  for i in reversed(number):
    if counter < 3:
      numberList.append(i)
      counter = counter + 1
    if counter == 3:
      numberList.append(".")
      counter = 0

  for i in reversed(numberList):
    numberFormatted = numberFormatted + i
  
  if numberFormatted[0] == ".":
    numberFormatted = numberFormatted.replace(".","",1)
    
  if len(decimalPart) != 4:
    decimalPart = "0,00"
    
  for i in decimalPart[1:]:
    numberFormatted = numberFormatted + i


  return numberFormatted

def customDateFormat(date):
  months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  day = date.day
  month = months[date.month - 1]
  year = date.year

  message = "{} de {} del {}".format(day,month,year)
  return message

def printLines(message):
  line = ("_"*35).center(messageMargin)

  print (line)

  if type(message) == list:
    for i in message:
     print (i.center(messageMargin))
  else:
    message = message.center(messageMargin)
    print(message)
    
  print (line)

def getDollarPrices():

  # Header
  today = datetime.now()
  date = customDateFormat(today)
  title = "Precio del dólar"
  printLines([title,date])


  # Dollar prices table
  rangeOfPages = [i for i in range(12,24) if i != 22]
  dollarTotalSum = 0
  numberOfPages = 0

  for i in rangeOfPages:
    data = soup.find(id = i)
    pageName = data.p1.get_text()
    dollarPrice = data.p2.get_text()

    message = "{:<20} : {:>10}".format(pageName,dollarPrice)
    print(message.center(messageMargin))
    
    dollarPrice = replaceMultiple(dollarPrice, [".",","],["","."])

    numberOfPages = numberOfPages + 1
    dollarTotalSum = dollarTotalSum + float(dollarPrice)

  # Footer
  average = dollarTotalSum/numberOfPages
  average = formatNumber(average)
  averageMessage = "{:<20} : {:>10}".format("Promedio",average)
  printLines(averageMessage)


response = requests.get('https://exchangemonitor.net/ve')
soup = BeautifulSoup(response.text, 'html.parser')

messageMargin = 50

getDollarPrices()