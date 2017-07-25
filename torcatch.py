from future.builtins import input
#*************************************************************#	
															  #
#***********Work Area ****************************************#
from selenium import webdriver
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import random
import sys

class Proxy(object):

	link = ''

	def __init__(self):

		self.link = 'https://hide.me/en/proxy'

	def openLink(self,driver):
		
		driver.get(self.link);	

	def searchLink(self,driver,link):
				
		urlBox = driver.find_element_by_id('u')
		urlBox.send_keys(link)
		submit = driver.find_element_by_id('hide_register_save')
		submit.click()
		#driver.save_screenshot(str(random.randint(1,1000000))+".jpg")


class To1337(object):

	link = ''
	pageList = []
	pageLinkList = []
	visitpageList = []

	soup = BeautifulSoup('','lxml')   

	def __init__(self):

		self.link = '1337x.to'

	def searchLink(self,driver,fileName):
		
		textBox = driver.find_element_by_id('autocomplete')

		textBox.send_keys(fileName)

		submit = driver.find_element_by_xpath("//button[@class='btn btn-search']")

		submit.click()
		

	def parseSearchPage(self,driver,page):

		itemId = 0

		if page not in self.visitpageList:

			itemList = []
			finalLinks = []

			self.visitpageList.append(page)

			self.soup  = BeautifulSoup(driver.page_source, 'lxml')

			#data =  (self.soup.prettify()).encode('ascii', 'ignore').decode('ascii') 

			table = self.soup.find('table')

			tbody = table.find('tbody')

			trows = [rows for rows in tbody if rows != None and len(rows)!=1]

			for row in trows:
				links = row.find_all('a',href=True)
				finalLinks.append(links[1]['href'])	

			self.pageLinkList.append(finalLinks)	

			print('')

			#driver.save_screenshot(str(random.randint(1,1000000))+".jpg")

			table = self.soup.find('table')

			tbody = table.find('tbody')

			trows = [rows for rows in tbody if rows != None and len(rows)!=1]

			for row in trows:
				itemList.append(row.text.replace(' ','').split())

			self.pageList.append(itemList)	

			print('{:^5}|{:^30}|{:^5}|{:^10}|{:^10}'.format('ID','Name','Leech','Date','Size/Seed'))
			print('-'*80)

			for item in self.pageList[self.visitpageList.index(page)]:
				print('{:^5}|{:^30}|{:^5}|{:^10}|{:^10}'.format(itemId,item[0][:30],item[2],item[3],item[4]))
				print('-'*80)
				itemId += 1	

		else:

			pagepos = self.visitpageList.index(page)

			print('{:^5}|{:^30}|{:^5}|{:^10}|{:^10}'.format('ID','Name','Leech','Date','Size/Seed'))
			print('-'*80)

			for item in self.pageList[pagepos]:
				print('{:^5}|{:^30}|{:^5}|{:^10}|{:^10}'.format(itemId,item[0][:30],item[2],item[3],item[4]))
				print('-'*80)
				itemId += 1			

		info = int(input('\n\nEnter ID or Page Number  : '))		

		if info>=0 and info<=19:

			while True:
				try:

					link = 'https://nl.hideproxy.me'+self.pageLinkList[self.visitpageList.index(page)][info]

					driver.get(link)

					#driver.save_screenshot(str(random.randint(1,1000000))+".jpg")
					# mlink = soup.find('ul',attrs={'class':'download-links-dontblock btn-wrap-list'})

					# print(mlink.li.a['href'])

					clickB = driver.find_element_by_xpath('//ul[@class="download-links-dontblock btn-wrap-list"]/li/a')

					clickB.click()

					#driver.save_screenshot(str(random.randint(1,1000000))+".jpg")

					soup = BeautifulSoup(driver.page_source,'lxml')

					mlink = soup.find('p',attrs={'style':'text-align:right'})

					mtext = (((mlink.text).replace(' ','')).replace('\n',''))

					startPos = mtext.find('magnet') 

					print('')
					print('')
					with open('magnet.txt','w') as file:
						file.write('Download Magnet Link\n-------- ------ ----\n\n'+mtext[startPos:len(mtext)-1])

					print('Check magnet.txt file ... press any key to exit')	

					break

				except:
					print('Reconnecting Please Wait..')	





if __name__ == '__main__':
	

	sys.stdout.write('\n\nWait...\n\n')

	driver = webdriver.PhantomJS("phantomjs.exe")
	fileName = input('Enter File name to search : ')
	#fileName =  'despicable me'

	print('Searching...\n')

	try:

		while True:

			try:

				proxyObj = Proxy()

				proxyObj.openLink(driver)

				to1337Obj = To1337()

				proxyObj.searchLink(driver, to1337Obj.link)

				to1337Obj.searchLink(driver, fileName)

				to1337Obj.parseSearchPage(driver,1)

				break

			except:
				#driver.save_screenshot(str(random.randint(1,1000000))+".jpg")				
				driver.close()
				driver.quit()
				print('Reconnecting Please Wait..')	

	except:
		raise

	finally:
		driver.close()
		driver.quit()	

input('Thank you for using ...[ prajwal_15 :) ]')
#***Always at end***********#
						    #
#***************************#