from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from lesson_07.base import base
class LoginTest(base):
    def username(self,nameid):
        self.nameid=nameid
        return self.by_id(self.nameid)
    def password(self,passwordid):
        return self.by_id(passwordid)
    def submit(self,submitid):
        return self.by_id(submitid)
    def source(self,source_css):
        return self.by_css(source_css)
    def des(self,des_css):
        return base.by_css(des_css)
    def slide_moudle(self,source_css,des_css):
        source=self.by_css(source_css)
        des=self.by_css(des_css);
        ActionChains(self.driver).drag_and_drop_by_offset(source, des.size["width"], -des.size["height"]).perform()

    def login(self,name,password):
        self.username("nloginname").send_keys(name);
        self.password("npwd").send_keys(password)
        self.slide_moudle("#sliderddnormal > div.cpt-drop-box > div.cpt-drop-btn","#sliderddnormal > div.cpt-drop-box > div.cpt-bg-bar")
        time.sleep(20)
        self.submit("nsubmit").click();
        time.sleep(20)

