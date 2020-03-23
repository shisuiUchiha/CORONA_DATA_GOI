#corona data scraped from gov.in. STAY SAFE AND HEALTHY
from bs4 import BeautifulSoup
import requests

html=requests.get("https://www.mygov.in/covid-19/").text
soup=BeautifulSoup(html,"html.parser")
#print (soup.prettify())
data_words=[]
data_num=[]
mydivs=soup.findAll("div",{"class": "info_label"})
myspans=soup.findAll("span",{"class": "icount"})
myth_divs=soup.findAll("div",{"class": "myth_text"})
help_divs=soup.findAll("div",{"class": "progress-text-area"})

print("IMPORTANT NUMBERS OF INDIA SCRAPED FROM mygov.in/covid-19\n")
for i in range(len(mydivs)):
	print (mydivs[i].get_text(),myspans[i].get_text())
	print("\n")
	
print("IMPORTANT MYTHS REGARDING CORONA VIRUS\n")

for myths in myth_divs:
	print(myths.get_text())
	print("\n")
print("IMPORTANT HELPLINE AND EMAIL CONTACTS OF GOVERNMENT OF INDIA\n")
for helpline in help_divs:
	print(helpline.find("p").get_text())
	print(helpline.find("strong").get_text())
	print("\n")

last_updated=soup.findAll("div",{"class": "ad_img server_info"})

for last in last_updated:
	print(last.get_text())
