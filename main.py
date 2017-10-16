

from selenium import webdriver
from captcha_solver import CaptchaSolver

browser = webdriver.Firefox()
browser.get("https://www.irctc.co.in/eticketing/loginHome.jsf")


username = "username"
passwd = "password"

userID=browser.find_element_by_class_name("loginUserId")
userID.send_keys(username)

password= browser.find_element_by_class_name("loginPassword")
password.send_keys(passwd)

reload_captcha=browser.find_element_by_class_name("nlpRefresh")
reload_captcha.click()

captcha_image=browser.find_element_by_id("nlpImgContainer")