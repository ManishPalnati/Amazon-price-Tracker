import requests
from bs4 import BeautifulSoup 
import os 
import smtplib 
from email.message import EmailMessage 
import time 
 
email_id = os.environ.get("EMAIL_ADDR") 
email_pass = os.environ.get("EMAIL_PASS") 
 
URL = "https://www.amazon.in/generation-smart-speaker-powerful-Alexa/dp/B084KSRC9X/ref=sr_1_13?crid=1W0966MVIC07A&dib=eyJ2IjoiMSJ9.H75bGx4NvDWoLVAmp-SBBgUrAX6DaOKkhk1YjUuxaal_wwDMufanOdcbSqySGy33n3Lbbkk1xLEnpe9a82t7QMOYetW3MAhGA60MRKyMbay0MRWkZjOLQOdLmjmUMCdklv_CtTYKz46VRKWN8nR5OmFeEcpQkRTcOVTGDjHAbrDjGznmqJTeCnrCbrW41LSJSMz1SvSVKQIbmG9nQCMrukdnbJV0uTqGZ63VhJ6jdWA.jMYaVAU_OESSC8nkcZgf9mbXovK7hJn2DW6zmlZQSmk&dib_tag=se&keywords=echo+speaker&qid=1713704193&sprefix=echo+speake%2Caps%2C208&sr=8-13" 
 
def check_price(): 
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'} 
 
    page = requests.get(URL, headers=headers) 
    soup = BeautifulSoup(page.content, 'html.parser') 
 
    title = soup.find(class_="a-size-large product-title-word-break").get_text() 
    price = soup.find(class_="a-price-whole").get_text() 
    converted_price = int(price[:5].replace(",","")) 
    print(title.strip()) 
    print(converted_price) 
     
 
    if converted_price < 2799: 
        send_mail() 
 
def send_mail(): 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() 
    server.starttls() 
    server.ehlo() 
     
    server.login('rithwikponnam1869@gmail.com','rvozinrhpsoncfzo') 
 
    subject = 'Price fell down!' 
    body = 'Check the amazon link https://www.amazon.in/generation-smart-speaker-powerful-Alexa/dp/B084KSRC9X/ref=sr_1_13?crid=1W0966MVIC07A&dib=eyJ2IjoiMSJ9.H75bGx4NvDWoLVAmp-SBBgUrAX6DaOKkhk1YjUuxaal_wwDMufanOdcbSqySGy33n3Lbbkk1xLEnpe9a82t7QMOYetW3MAhGA60MRKyMbay0MRWkZjOLQOdLmjmUMCdklv_CtTYKz46VRKWN8nR5OmFeEcpQkRTcOVTGDjHAbrDjGznmqJTeCnrCbrW41LSJSMz1SvSVKQIbmG9nQCMrukdnbJV0uTqGZ63VhJ6jdWA.jMYaVAU_OESSC8nkcZgf9mbXovK7hJn2DW6zmlZQSmk&dib_tag=se&keywords=echo+speaker&qid=1713704193&sprefix=echo+speake%2Caps%2C208&sr=8-13' 
     
    msg = f"Subject: {subject}\n\n{body}" 
    server.sendmail( 
        'rithwikponnam1869@gmail.com', 
        'rithwik1869@gmail.com', 
        msg 
    ) 
    print('HEY EMAIL HAS BEEN SENT!') 
     
    server.quit() 
     
while(True): 
    check_price() 
    time.sleep(60*60) 
 
