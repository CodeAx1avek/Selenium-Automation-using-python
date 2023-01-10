#First You Have to Downlaod AnyEditor To Run Python Code
#So First Go to your chrome check your chrome Version 
#And Donwlaod chromedriver accourding to your chrome version...Just Search On google Chromedriver
#Now MAke New Folder And Add On It And Now MAke Test.py file And Start Your Journey In Automation
#Open CMD terminal And Install - pip install selenium
###########AvekGaming-CodeAx1############

from selenium import webdriver #Importand module
import time  #for Waiting on Video And Watching
import random    #For Random Minute to Watch Video

driver = webdriver.Chrome(executable_path="chromedriver.exe") #we have chromedrive.exe in our folder Nice


for i in range(5):  #We Will Watch Our Video Again Again for five time According to you
    sleep_time = random.randint(10,15)   #we maked a variable which contain time with random second
    print("video is running for {} time".format(i))  #it will say how many time we have played video
    driver.get("https://www.youtube.com/watch?v=wEYJXPdzbgw") #1st Video  -You Can Add Your youtube Link
    time.sleep(sleep_time)  
    print(driver.title)
    driver.get("https://www.youtube.com/watch?v=Y-VwsmMRjFU") #second video -You Can Add Your youtube Link
    print(driver.title)
    time.sleep(sleep_time)
    driver.get("https://www.youtube.com/watch?v=xXxnMH7d7Pg")  #3rd video  - You Can Add Your youtube Link
    print(driver.title)
    time.sleep(sleep_time)
driver.quit()
