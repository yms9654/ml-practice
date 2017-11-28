from selenium import webdriver

phantomjs_path = r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe"

url = "http://www.naver.com"

browser = webdriver.PhantomJS(executable_path=phantomjs_path)
browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("Website.png")
browser.quit()