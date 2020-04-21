import requests, bs4, re, time
from bs4 import BeautifulSoup
import smtplib 
import time
# r = requests.get("https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN")

def sensex():
    r = requests.get("https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN")
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    price = (soup.find_all('div',{"class": "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text).replace(",",".")
    convprice = float(price[0:6])
    if(convprice < 28.000):
        send_mail()
    # if(convprice > 30.000):
    #     send_mail()
        
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("emailid","password")

    subject = "Sensex has fallen below 28,000"
    body = "Check by how many points has it fallen https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "emailid",
        "emailidyouwanttosendnotificationto",
        msg
    )
    print("EMAIL HAS BEEN SENT")

# sensex()

    server.quit()

while(True):
    sensex()
    time.sleep(29700)



