from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys






# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. Firefox – http://www.ynet.co.il
my_website = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64/chromedriver"))
my_website.get("http://www.walla.co.il")

my_website2 = webdriver.Firefox(service=Service("/Users/gilspiegel/Downloads/geckodriver2"))
my_website2.get("http://www.ynet.co.il")


# 2. In one of the browsers you have open, do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you created in clause 1
my_website = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64/chromedriver"))
title = my_website.title
my_website.refresh()
if my_website.title == title:
    print("same")


# Open a few browsers, locate any element, does the element has the same locator in the other browser?
#Anwser
#/html/body/div[12]/div/div/div[1]/div[5]/div[4]/div/div/div/div/div/div[1]/a/h1/span //chrome
#/html/body/div[12]/div/div/div[1]/div[5]/div[4]/div/div/div/div/div/div[1]/a/h1/span //firfox
#Yes different browser with same elements have the same xpath


# 4. Create a test with the following:
# a. Open Google Translate web page
# b. Write anything in Hebrew in the text area
my_website = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
my_website.get("https://translate.google.com/")
my_website.find_element(By.XPATH, ('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')).click()
input_text = my_website.find_element(By.XPATH, ('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')).send_keys("שלום")
my_website.find_element(By.XPATH, ('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')).click()

# 5. Open Youtube web page
# a. Type a name of a song
# b. Click on search.

youtube = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
youtube.get("https://www.youtube.com/")
search_bar = youtube.find_element(By.XPATH, '//input[@id="search"]')
search_bar.click()
search_bar.send_keys("the blaze territory")
search_button = youtube.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
search_button.send_keys(Keys.RETURN)


# 6. Open Chrome browser on Google Translate website: https://translate.google.com/
# a. Find translation text field (the one you send keys to) with 3 different locators and
# print the WebElement you created.
translate = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
translate.get("https://translate.google.com/")

print('\nXPATH:\n//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
print('Name locator:\naria-label: "Source text"')
print("CSS:\n#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea")

# 7. Open Chrome browser on Facebook website https://www.facebook.com/
# a. Login into Facebook (No need to send me credentials).
facebook = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
facebook.get("https://www.facebook.com/")
email_bar = facebook.find_element(By.XPATH, '//input[@id="email"]')
email_bar.click()
email_bar.send_keys("gils339")
pass_bar = facebook.find_element(By.XPATH, '//input[@id="pass"]')
pass_bar.click()
pass_bar.send_keys("0515235436")
login_button = facebook.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
login_button.send_keys(Keys.RETURN)


# Challenges:
# 8. Open Chrome browser on any webpage:
# a. Delete all cookies from browser.
# b. Make sure all cookies are deleted by printing all cookies stored in the browser.

delete_cookies = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
delete_cookies.delete_all_cookies()
cookies = delete_cookies.get_cookies()
if cookies == []:
    print("no cookies for you")

# 9. Open any browser on "Github" website https://github.com/
# a. Enter “Selenium” keyword in search textfield
# b. Press Enter to search (through code - of course).

github = webdriver.Chrome(service=Service("/Users/gilspiegel/Downloads/chromedriver_mac_arm64"))
github.get('https://www.github.com/')
search = github.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]')
search.click()
search.send_keys("selenium")
search.send_keys(Keys.RETURN)

