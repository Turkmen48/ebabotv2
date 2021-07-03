from selenium import webdriver
import time
import os
import sys
class ebabot():
    def giris(self):
        self.browserprofile=webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option('prefs',{'intl.accpet_languages':'en,en_US'})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserprofile)
        self.girisurl="https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp"
        self.canli_dersurl="https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.772/index.html#/main/livesessionview?tab=liveLessons&pageNumber=1&pageSize=25"
        self.tc="tc"
        self.sifre="sifre"
        self.browser.get(self.girisurl)
        self.tcarea=self.browser.find_element_by_xpath("//*[@id='tckn']").send_keys(self.tc)
        self.passarea=self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[3]/div/input").send_keys(self.sifre)
        time.sleep(1)
        self.submit=self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button").click()
        time.sleep(3)
        self.browser.get(self.canli_dersurl)
        time.sleep(3)
    def tikla(self):
        self.tikla=self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div[2]/div/table/tbody/tr/td/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div[2]/div[1]").click()
        time.sleep(3)
    def bot(self):

        self.katil=self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[3]/div").get_attribute("class")
        if self.katil=="btn btn-md ng-binding btn-success disabled":
            print("katıl kapalı")
            time.sleep(10)
            self.browser.refresh()
            time.sleep(10)
            return False
        else:
            print("katıl açık")
            time.sleep(5)
            return True
    def derse_gir(self):
        print("derse girildi")
    def kappa(self):
        self.browser.close()



bot=ebabot()
bot.giris()
bot.tikla()
while True:
    bot.bot()
    if bot.bot==True:
        print("katıl aççık")
        break
    else:
        print("katıl kapalı")
        time.sleep(10)
bot.derse_gir()
bot.kappa()
os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
