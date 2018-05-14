#! /usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from time import sleep
import datetime

browser = webdriver.Chrome(
    r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

def findBook(url):
    browser.get(url)
    sleep(1)
    url = browser.find_element_by_class_name('reding').get_attribute('href')
    charpter = 1 # get charpeter
    return copyText(url,charpter)

def copyText(url,charpter):
    temp = []
    for i in range(charpter):
        browser.get(url) 
        text = browser.find_element_by_class_name('text').text
        temp.append(text)
        i = i+1
        print("the %s finished" % i)
        sleep(1)
        url = browser.find_element_by_xpath(".//*[@type='next']").get_attribute('href')
    return temp

def getBooks():
    browser.get('http://wap.yc.ireader.com.cn/')
    sleep(1)
    lis = browser.find_element_by_class_name('f2').find_elements_by_tag_name('li')
    books = []
    for li in lis:
        link = [[],[]]
        link[0] = li.find_element_by_tag_name('a').get_attribute('href')
        link[1] = li.find_element_by_tag_name('a').get_attribute('title')
        has = True
        for book in books:
            if(book[1] == link[1]):
                has = False
                continue
        if(has == True):
            books.append(link)
    return books

def main():
    starttime = datetime.datetime.now()
    books = getBooks()
    # name = "汉乡"
    # books.append(name)
    print(books)
    for book in books:
        text = findBook(book[0])
        # print("bookname:%s,text:%s" % (book[1],text))
        file = r'e:/code/python/temp/%s.txt' % book[1]
        with open(file,"w",encoding='utf-8') as f:
            f.write(("%s" % (text)))
    endtime = datetime.datetime.now()
    print ('It took %ds to sort the size of these items. The result is as below:' %(endtime - starttime).seconds)


main()

