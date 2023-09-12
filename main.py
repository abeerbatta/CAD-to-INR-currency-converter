import pywhatkit
import schedule
import requests
import datetime
import time


def job():
    now = datetime.datetime.now()
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=INR&base=CAD"
    payload = {}
    headers = {
        "apikey": "0S6jhnnMhO2z2KguhjrR04DPgyif6zG2"
    }

    r = requests.request("GET", url, headers=headers, data=payload)
    # status_code = r.status_code
    a = r.text
    inr_string = str(a)
    print(inr_string)
    pywhatkit.sendwhatmsg("+919650695014", inr_string, now.hour, now.minute + 1)


schedule.every().day.at("12:19").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
