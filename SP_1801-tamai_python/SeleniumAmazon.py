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
CHEAP_COFFEE_URL = "https://www.amazon.co.jp/gp/product/B00XMUZGJ0/ref=s9u_simh_gw_i1?ie=UTF8&pd_rd_i=B00XMUZGJ0&pd_rd_r=932b0d93-d4ed-11e8-a829-192d104beea6&pd_rd_w=YH9SK&pd_rd_wg=5OBC5&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=&pf_rd_r=MCMB102TNC4XZTRD0ZJ3&pf_rd_t=36701&pf_rd_p=7d4cee6a-0149-45bb-a2b2-9b4531af080e&pf_rd_i=desktop"
EXPENSIVE_COFFEE_URL = "https://www.amazon.co.jp/gp/product/B00WR6B02W?pf_rd_p=8c88536d-9977-47bb-9a78-f021ab673f14&pf_rd_r=CYHYJDS48K9ZQATQB78W"
#仮貯金額
SAVINGS = 1000

#ブラウザ起動、サイトにアクセス
#金額が少なければ安いコーヒー豆、多ければ高いコーヒー豆のページにアクセス
if SAVINGS >= 1000 and SAVINGS < 3000 :
  driver = webdriver.Chrome()
  driver.get(CHEAP_COFFEE_URL)
elif SAVINGS >= 3000 :
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
