# coding:utf-8

"""
プログラム説明：
　貯金額に応じてコーヒー豆をAmazonから自動購入
　クレカを登録している必要がある
"""

#seleniumのパスを渡し、エラー：cannot import name seleniumを対策
import sys
sys.path.append('//usr/local/lib/python3.7/site-packages')

from selenium import webdriver

#アカウント
ID = "g2118023@fun.ac.jp"
PASSWORD = "amazon2118"
#URL
CHEAP_COFFEE_URL = "https://www.amazon.co.jp/%E5%8A%A0%E8%97%A4%E7%8F%88%E7%90%B2%E5%BA%97-%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%87%E3%83%B3%E3%83%96%E3%83%AC%E3%83%B3%E3%83%89-%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC-500g-%EF%BC%9C%E6%8C%BD%E3%81%8D%E5%85%B7%E5%90%88%EF%BC%9A%E8%B1%86%E3%81%AE%E3%81%BE%E3%81%BE%EF%BC%9E/dp/B00XMUZGJ0/ref=sr_1_12?rps=1&ie=UTF8&qid=1540052717&sr=8-12&keywords=%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC%E8%B1%86%E3%80%80500g&refinements=p_76%3A2227292051"
EXPENSIVE_COFFEE_URL = "https://www.amazon.co.jp/Juan-Valdez-%E3%83%95%E3%82%A2%E3%83%B3%E3%83%BB%E3%83%90%E3%83%AB%E3%83%87%E3%82%B9-%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC%E8%B1%86%E3%80%90%E3%83%8A%E3%83%AA%E3%83%BC%E3%83%8B%E3%83%A7%E3%80%91%E3%82%B7%E3%83%B3%E3%82%B0%E3%83%AB%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%B3-%E3%82%B3%E3%83%AD%E3%83%B3%E3%83%93%E3%82%A2%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC/dp/B00WR6B02W/ref=sr_1_60?rps=1&ie=UTF8&qid=1540052811&sr=8-60&keywords=%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC%E8%B1%86%E3%80%80500g&refinements=p_76%3A2227292051"
#仮貯金額
SAVINGS = 1000

#ブラウザ起動、サイトにアクセス
#金額が少なければ安いコーヒー豆、多ければ高いコーヒー豆のページにアクセス
if SAVINGS >= 1000 and SAVINGS < 4500 :
  driver = webdriver.Chrome()
  driver.get(CHEAP_COFFEE_URL)
elif SAVINGS >= 4500 :
  driver = webdriver.Chrome()
  driver.get(EXPENSIVE_COFFEE_URL)
else :
  driver.quit()

#カートに入れる
driver.find_element_by_name("submit.add-to-cart").click()

#カート画面に移動
driver.get("https://www.amazon.co.jp/gp/cart/view.html/ref=nav_cart")
driver.find_element_by_name("proceedToCheckout").click()

#待機
driver.implicitly_wait(3)

#ログイン
#driver.find_element_by_xpath("//a[@id='nav-link-accountList']/span").click()
driver.find_element_by_id("ap_email").send_keys("yourmailaddress@example")
driver.find_element_by_id("ap_password").send_keys("yourpassword")
driver.find_element_by_id("signInSubmit").click()

#注文。危険なのでコメントアウト
#driver.find_element_by_name("placeYourOrder1")[0].click()
driver.save_screenshot("AmazonScreenshot.png")
driver.quit()
