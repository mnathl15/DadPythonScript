import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter




page = urllib.request.urlopen("file:///C:/Users/thele/PycharmProjects/History_Project/History.html").read()

soup = BeautifulSoup(page,"html.parser")

links = soup.find_all("tbody",class_="job")


#historyJobs is the tab for Past Jobs

#Gets the number of jobs listed
num_jobs =int(soup.find('li',{'id':'historyJobsTab'}).find('span',class_='legend work').get_text());
#Gets the confirmation numbers
conf_nums = soup.find('div',{'id':'historyJobs'}).find_all('span',class_='confNum')

names = soup.find('div',{'id':'historyJobs'}).find_all("span",class_="name")
titles = soup.find('div',{'id':'historyJobs'}).find_all("span",class_="title")


#Gets specific details such as district,time,dates, etc...
detail_tag = soup.find('div',{'id':'historyJobs'}).find_all(lambda tag: tag.name == "tr" and tag.get("class") == ["detail"])



districts = [None] * len(detail_tag)
locations = [None] * len(detail_tag)
times = [None] * len(detail_tag)
types = [None] * len(detail_tag)
dates = [None] * len(detail_tag)

#iterates through detail tag to find each event
for i in range(0,len(detail_tag)):
  districts[i] = (detail_tag[i].find("div",class_="tenantName"))
  locations[i] = (detail_tag[i].find("div",class_="locationName"))
  dates[i] = (detail_tag[i].find("td",class_="date"))
  types[i] = (detail_tag[i].find("td",class_="duration"))
  times[i] = (detail_tag[i].find("td",class_="times"))



workbook = xlsxwriter.Workbook('C:/Users/thele/PycharmProjects/History_Project/Schedule_History.xlsx')



worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)
worksheet.set_column('B:B',20)
worksheet.set_column('C:C',20)
worksheet.set_column('D:D',20)
worksheet.set_column('E:E',20)
worksheet.set_column('F:F',20)
worksheet.set_column('G:G',20)


worksheet.write('A1','Name')
worksheet.write('B1','Position')
worksheet.write('C1','Date')
worksheet.write('D1','Times')
worksheet.write('E1','Type')
worksheet.write('F1','District')
worksheet.write('G1','Location')
worksheet.write('H1','Confirmation Numbers')
worksheet.write('I1','Amount Owed')
worksheet.write('J1','Amount Paid')
worksheet.write('K1','Date Paid')

for i in range(0,num_jobs):
    worksheet.write(i+1,0,names[i].get_text())
    worksheet.write(i+1, 1, titles[i].get_text())
    worksheet.write(i+1,7,conf_nums[i].get_text())

for i in range(0,num_jobs):
    worksheet.write(i+1, 2, dates[i].get_text())
    worksheet.write(i+1, 3, times[i].get_text())
    worksheet.write(i+1, 4, types[i].get_text())
    worksheet.write(i+1, 5, districts[i].get_text())
    worksheet.write(i+1, 6, locations[i].get_text())



workbook.close()