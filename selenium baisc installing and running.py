# Install selenium through spyder
# install chrome driver using 
# "https://sites.google.com/a/chromium.org/chromedriver/"
# check your chrome version and install acording to it.
# After you download the webdriver from chrome place it where you run .py files or your project environment
# and install it

import selenium

from selenium import webdriver

driver=webdriver.Chrome()
# After running above command a chrome browser will be open in the state of
# " chrome is being controlled by automated software"

# If the above command didnot run or giving you an error use the below it will also work

import os

driver = webdriver.Chrome(os.getcwd()+"\chromedriver.exe") 
# The same outcome as the line 5

# Now we can open a browser using webdriver from python

driver.get("https://www.youtube.com/")
# Chrome browser will open with "youtbe.com"
