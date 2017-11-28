from selenium import webdriver

phantomjs_path = r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe"

browser = webdriver.PhantomJS(executable_path=phantomjs_path)
browser.implicitly_wait(3)

browser.get("https://www.google.com")
r = browser.execute_script("return 100 + 50")
print(r)
browser.quit()