import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
URL ="https://www.amazon.com/s?k=bluetooth+speakers&crid=3NXFI5NOKI3TS&sprefix=Blue%2Caps%2C570&ref=nb_sb_ss_ts-doa-p_2_4"
import lxml
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
}
MY_EMAIL ="munasinghehiruka@gmail.com"
PASSWORD ="Google Company"
response = requests.get(url=URL,headers=headers)

website_html = response.text
#print(website_html)
soup = BeautifulSoup(website_html,"lxml")
#print(soup.prettify())

#Getting the price of the product
heading = soup.find(name="span",class_="a-price-whole").getText()
price = heading.split("$")[0]
product_price = float(price)
print(product_price)

#Getting the title of the product
title = soup.find(name="span",class_="a-size-medium a-color-base a-text-normal").getText().strip()
print(title)

# Sending email
if product_price<25:
    message =f"{title} is now ${heading}"
    with SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n{message}\n{URL}"
        )
