from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

driver.get('https://selenium.dev')



def inputQuit(x):
    if x == 'qqq':
        driver.quit()
    else:
        x = input("Waiting to quit(qqq):")
        inputQuit(x)

x = 'not'

inputQuit(x)