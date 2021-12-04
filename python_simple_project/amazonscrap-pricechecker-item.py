import requests
from bs4 import BeautifulSoup
import smtplib

# url = "https://www.amazon.co.uk/Apple-Airpods-Wireless-Charging-latest/dp/B07PYM8FB8/ref=sr_1_6?keywords=airpods&qid=1581244893&sr=8-6"
url = "https://www.amazon.co.uk/OnePlus-Buds-Pro-headphones-Cancellation-White/dp/B07XW425NC/ref=sr_1_1?crid=1KWZIIOZ7KSNW&keywords=airpods%2Bpro&qid=1638612493&sprefix=airpods%2Caps%2C1174&sr=8-1&th=1" #the url specific of product item that you want to scrap in amazon web
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
price_value = 147 #this is the amount that you want the item to drop to in price. This is maximum budget that you will able to purchase the item.
email_address = "youremailaddress@gmail.com"#this is the account the python will interact with to send an email when the price drops to the specified
password = "youremailpassword" #youremailpassword
receiver_email = "youranotheremail@gmail.com" #the e-mail address that will receive the notification that the price has dropped to the range you're tracking

def trackPrices():
    price = float(getPrice())
    if price > price_value:
        diff = int(price - price_value)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()

#TODO: Enabling security settings for gmail to interact with Python so that you can send emails through python via your gmail account
#TODO:Get the price for the item that you are tracking
def getPrice():
    #TODO: Store the request information
    page = requests.get(url, headers = headers)
    #TODO: Store the page content
    soup = BeautifulSoup(page.content, 'html.parser')
    #TODO: Extracting parts of the captured page content
    #strip all the blank space
    title = soup.find(id='productTitle').get_text().strip()
    get_price = soup.find("span",{"class":"a-offscreen"}) #depends on the html structures yaw
    price = get_price.text.strip()[1:4] #just the numbers
    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price has Dropped!"
    mailtext = 'Subject:' + subject + '\n\n' + url
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(email_address, password)
    server.sendmail(email_address, receiver_email, mailtext)

if __name__ == "__main__":
    trackPrices()
