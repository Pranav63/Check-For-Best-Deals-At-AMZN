# Check for the prices change everyday for a particular amazon product
import math 
import sklearn 
import matplotlib
import numpy as np 
import pandas as pd
import requests 
import bs4
import urllib
from bs4 import BeautifulSoup
import smtplib # simple mail protocol (enable to send email)
import time

def price_check():
	url = "https://www.amazon.com/all-new-Echo/dp/B07XZQN2C1/ref=sxbs_sxwds-deals?cv_ct_cx=echo&keywords=echo&pd_rd_i=B07NFTVP7P&pd_rd_r=b739222a-b668-42c1-895d-2eaadf75bd95&pd_rd_w=3EhTb&pd_rd_wg=2cugQ&pf_rd_p=0d9ff078-075d-4295-b9e1-6a735b26fa6f&pf_rd_r=KKXMPPV01BVEY7N5VBEV&qid=1578087378&smid=ATVPDKIKX0DER&th=1"

	headers ={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

	page = requests.get(url, headers=headers) 

	soup1 = BeautifulSoup(page.content,"html.parser")

	soup2= BeautifulSoup(soup1.prettify(),"html.parser")
# 	Product Id can be checked through an inspect element on your browser
	price=soup2.find(id="priceblock_ourprice").get_text() 
	title=soup2.find(id="productTitle").get_text()

	convert_float=float(price[1:3])

	if convert_float < 85:
		emailsend()

	print(title.strip())
	print(convert_float)



def emailsend():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('your_email_address','vrvhecpcdgpyemco')

	subject = " Check the price , we just got a low one :)"

	body = "Check this amzn Link https://www.amazon.com/all-new-Echo/dp/B07XZQN2C1/ref=sxbs_sxwds-deals?cv_ct_cx=echo&keywords=echo&pd_rd_i=B07NFTVP7P&pd_rd_r=b739222a-b668-42c1-895d-2eaadf75bd95&pd_rd_w=3EhTb&pd_rd_wg=2cugQ&pf_rd_p=0d9ff078-075d-4295-b9e1-6a735b26fa6f&pf_rd_r=KKXMPPV01BVEY7N5VBEV&qid=1578087378&smid=ATVPDKIKX0DER&th=1"

	msg = f"Subject : {subject}\n\n{body}"

	server.sendmail(
		'from_email_Address',	'to_email_address',
		msg

		)
	print("Email has been sent dude , check")

while(True):
	price_check()
	#check everyday for the new prices:)
	time.sleep(86400)
