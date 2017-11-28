from selenium import webdriver
USER = ""
PASS = ""

phantomjs_path = r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe"

browser = webdriver.PhantomJS(executable_path=phantomjs_path)
browser.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

products = browser.find_elements_by_css_selector("div.p_info span")
print(products)
for product in products:
    print("-", product.text)

browser.quit()