from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# *************** STEP 1 ****************


# Starting with Login Page

#declared a variable driver and used it to store a chrome driver
# ChromeDriverManager().install() fetches the latest chrome driver binaries and installs
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://twitter.com/login') 


# *************** STEP 2 ****************

# now we are going to automate the login process:
# assign your login cridentiatl
email = "akashkumarsingh11032001@gmail.com"
passward = "Akash#2001"

# *************** STEP 3 ****************

# XPaths will be used here to select the element with which our automation script should interact

emailField = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')

passwordField = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

loginButton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')

# *************** STEP 4 ****************

# connecting field with there data (email -> emailFiled and so on)
# send_keys() method to stimulate the process of writing something in a TextField
# The click() method used in the loginButton is used to stimulate the process of clicking a button!
emailField.send_keys(email)
passwordField.send_keys(passward)

time.sleep(1)

loginButton.click()