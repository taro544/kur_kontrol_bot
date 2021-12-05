import time
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import signal

api_key = '4UDXO21HX6QAZ911'
first_currency = "USD"
second_currency = "TRY"
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
def handler(signum, frame):
    cls()
    while True:
        cls()
        res = input("Cikis yapmak istiyor musunuz ? y/n ")
        if res == 'y':
            cls()
            exit(1)
        elif res == 'n':
            cls()
            print("Lutfen bekleyin")
            break
        else:
            print("Lutfen dogru harfi girin")
            time.sleep(2)
            continue

signal.signal(signal.SIGINT, handler)



def oran_hesaplama(url):
    my_request = urllib.request.urlopen(url)
    my_HTML = my_request.read().decode("utf8")
    soup = BeautifulSoup(my_HTML, 'html.parser')
    x = soup.get_text()
    old_string = x
    new_string = old_string.replace('{',' ')
    new_string1 = new_string.replace('}',' ')
    new_string2 = new_string1.replace('"',' ')
    new_string3 = new_string2.replace(',',' ')
    new_string4 = new_string3.split()
    if "Exchange" in new_string4:
        Exchange1 =  new_string4.index("Exchange")
        del new_string4[Exchange1]
        Exchange2 =  new_string4.index("Exchange")
        Oran = new_string4[Exchange2+3]
        #Oranf = float(Oran)

        return Oran
    else:
        return 0
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1=first_currency,sayi2=second_currency,api_key=api_key)

while True:
    x = oran_hesaplama(url)
    if float(x) >= 14:
        cls()
        print("1 " +""+ first_currency + " = " +" " + x + second_currency)
        print("izmir marsi")
        break
    elif x == 0:
        cls()
        print("Limit bitti")
        time.sleep(100)
    else:
        cls()
        print("1 " +" "+ first_currency + " = " + x + " "+second_currency)
        time.sleep(100)
        continue
